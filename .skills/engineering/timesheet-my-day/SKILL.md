---
name: timesheet-my-day
description: >-
  Reconstruct a person's work day (or week) from their connected tools — Google
  Calendar, Gmail, Google Drive, Slack, Confluence — and map each
  activity to the HaloPSA tickets they are assigned to, producing a ready-to-enter
  timesheet with start/finish times, descriptions, ticket mappings, and clearly flagged
  gaps. Use this whenever someone wants to fill in or
  catch up on timesheets, reconstruct what they did on a given day or week, work out
  where their hours went, log time to HaloPSA, or says things like "help me do my
  timesheet", "what did I work on yesterday", "map my activities to tickets",
  "account for my 8 hours", or "I can't remember what I did this week". Trigger even
  if they never say the word "timesheet" but are clearly trying to recall and
  attribute their working time to tickets or projects.
metadata:
  author: The Instillery
  version: "1.1.0"
---

# Timesheet: My Day

## Why this exists

People in billable/ticket-tracked roles (consultants, MSP engineers, project delivery)
can't reliably recall, at the end of a back-to-back day, what they did or which ticket it
belongs to — but their calendar, sent email, edited documents, chat and browsing history
are a factual record. This skill stitches those signals into a proposed timesheet mapped
to tickets the person is assigned to, so they review and enter it in minutes instead of
reconstructing from memory.

The output is a **proposal to review and adjust**, not a system of record. Be honest about
uncertainty (offer alternative tickets, or a ⚠️ no-fit marker, rather than forcing a match)
instead of inventing tidy attributions.

## Workflow overview

1. Confirm the day/period to reconstruct.
2. Connector check — detect what's connected, show the status, then continue with whatever
   is available (no prompt).
3. Establish the person's identity and timezone.
4. Pull activity from every connected source for that period.
5. Pull the person's tickets — assigned, opened/actioned on the day, and any referenced.
6. Map each activity to a ticket (or offer alternatives / flag no fit).
7. Output the timesheet table — that's the deliverable; end there.

---

## Step 1 — Confirm the day (ask this first)

Before anything else, confirm which period to reconstruct. Show today's date and
day-of-week for reference, then offer these choices **in this order**:

1. **Today**
2. **Yesterday**
3. **Last working day** — the most recent completed weekday before today (Mon–Fri),
   skipping weekends and public holidays. Run on a Saturday or Monday it resolves to the
   previous Friday; use a holidays calendar to skip stat days if one is connected. This
   often coincides with "yesterday" but differs after a weekend or holiday, which is why
   it's a separate option.
4. **A specific date** (or range) the person types in.

Most runs are a single day. Weekly/multi-day ranges are fine if asked — just note the
per-day reconstruction is more approximate across a longer range.

**Resolve dates and "now" in the person's local timezone — never UTC or server time.** Get
their timezone/offset from the calendar (Step 3) *before* interpreting
"today"/"yesterday"/"last working day".

**Compute the current local time reliably — do not trust the shell clock.** On Windows /
Git Bash, `date` (even `TZ='Pacific/Auckland' date`) often returns **UTC mislabelled as
local** — e.g. it prints `09:42 GMT` when it is really `21:42` NZST. Instead, take UTC-now
and apply the person's *current* offset read from a **timezone-aware source** — a calendar
event's `dateTime` offset (e.g. `+12:00`) is ideal — rather than a hardcoded guess, since the
offset shifts with daylight saving (NZ is +12 NZST / +13 NZDT). Then **sanity-check AM vs
PM**: 09:42 and 21:42 flip whether the working day is still in progress or already finished,
so if the AM/PM looks wrong for the context you have almost certainly got a UTC/local
mix-up — recompute before saying anything about the day.

State the resolved date back to them (e.g. "Friday 28 Aug 2026") so a wrong pick is caught
immediately. For **Today**, reconstruct up to the current *local* time and caveat it as
in-progress only if it is genuinely still within the working day — once the working day is
over (evening), treat it as essentially complete, not partial.

## Step 2 — Connector check

The expected sources are **Calendar, Email, Files/Docs, Chat (Slack), Wiki (Confluence via
Atlassian Rovo), and HaloPSA (PSA/ticketing)**. Detect them up front — it changes what you
can produce, and the person may want to connect something first (finding out afterwards
that "most of my work is in Slack" wastes the run).

Tool schemas may be deferred — discover them with `ToolSearch`. Server IDs are opaque,
per-environment hashes, so **identify connectors by capability, not a hardcoded ID**.
[references/connectors.md](references/connectors.md) has the tool signatures per source,
the exact connector name to cite when one is missing, and how to tell connected from
needs-authorisation from not-connected.

One detection rule that's easy to get wrong:

- **HaloPSA must be the PRODUCTION instance.** A dev/sandbox Halo is useless for logging
  real time. Inspect the instance — ticket links, `get_user_info`, any returned URL — for
  markers like `dev-`, `sandbox`, `test`, or `uat` in the hostname (e.g.
  `dev-agent.theinstillery.com`). If the connected Halo is a dev instance, **mark HaloPSA
  as Not connected**, and add a note that the *dev* connector is connected but production
  is not. Do not map or log against a dev instance.

### Report status, then continue

Show a short status list (Connected ✓ / Needs authorisation ⚠️ / Not connected ✗). For
every source that is **not connected or needs authorisation, name the exact connector to
add** so the person can fix it for next time — e.g. the Slack connector is listed as
**"Slack"** (see references/connectors.md for the others). If the connector directory /
registry tools are available (`suggest_connectors`), surface one-click **Connect** buttons.
This status list is where missing sources are surfaced — there's no separate gaps section
later.

Then **just continue** with whatever's connected — don't pause or ask how to proceed. A
missing source simply means its evidence won't appear, which the status list already makes
clear. If production HaloPSA isn't connected (only dev, or none), say plainly that ticket
mapping will be indicative and not safe to log, then carry on building from the other
sources.

## Step 3 — Establish identity & timezone

Confirm who you are reconstructing for and their working timezone before pulling
time-bound data (if you didn't already resolve the timezone when interpreting the day in
Step 1), so both the relative-date logic and every timestamp land in the right local time:
- From HaloPSA (production), get the current user's name/email (e.g. a `get_user_info` tool).
- From the calendar connector, list calendars to read the primary calendar's timezone.

Treat that local timezone as the anchor: resolve "today"/"now" against it, and convert all
activity timestamps into it in the final table.

## Step 4 — Pull activity from each available source

For the scoped period, pull from every **connected** source. Typical signals:
- **Calendar** — meetings attended (title, time, attendees, description). This is the
  backbone of the day's structure.
- **Email** — messages *sent* by the person (what they actioned, who they dealt with).
  Note that calendar-invite accept/decline emails are low-value noise.
- **Files/Docs** — documents created / edited / viewed, with modified-by-me timestamps.
  Often the strongest signal for heads-down work that has no meeting.
- **Chat (Slack)** — messages/threads the person sent.
- **Wiki (Confluence, via Atlassian Rovo)** — Confluence pages the person **created,
  updated, or viewed** in the period. A page they *created or edited* is a strong
  heads-down signal (query by `creator`/`contributor = currentUser()`); a page they only
  *viewed* is weaker context. (Rovo may also expose Jira, but Confluence pages are the
  primary timesheet signal here.) See references/connectors.md for the CQL patterns.

Large results may be written to a file by the tool harness — parse them
(PowerShell `ConvertFrom-Json`, `jq`, or Python) rather than giving up. Convert every
timestamp to the person's local timezone. Watch for events whose stored offset differs
from their display timezone; recurring-event instance IDs (e.g. a `...T020000Z` suffix)
encode the true UTC start and are a reliable cross-check.

**Known blind spot — RMM / hands-on device work.** Remote-monitoring and remote-session
tools (e.g. ConnectWise Automate/ScreenConnect) are deliberately **not** connected here
for customer-access and security reasons, and hands-on device troubleshooting leaves
little digital trace. Don't try to infer this work or suggest connecting an RMM. If the
person's day plausibly included it, prompt them once to add those blocks manually.

## Step 5 — Pull the person's tickets (assigned, day-activity, and referenced)

Gather the person's tickets from Halo, then enrich. Prefer the **production** instance; if
only a dev/sandbox instance is connected, still pull for reference but warn results may be
**stale or incomplete** (dev often lags production) — don't read emptiness as "nothing
done", and never log against it.

**Mind the connector's permissions.** Production connectors are usually scoped tighter than
dev. In particular `get_assigned_tickets` tends to return a **flat, capped array with no
pagination** — treat it as a *starting set of active/primary assignments, not the
exhaustive list*. Don't try to page it, and don't assume a ticket is un-assigned just
because it's absent. Reach the rest with `search_tickets` and `get_one_ticket` (which can
read tickets the person isn't assigned to, provided they have access).

1. **Assigned tickets.** Call `get_assigned_tickets` for the baseline set of active
   assignments — the primary mapping targets. Take it as a starting point, not the full
   picture.
2. **Tickets they opened or interacted with on the day.** Best-effort: a
   "tickets/actions logged by technician" report (or similar) can surface what they created
   or actioned that date. Under reduced permissions these reports often return **empty, or
   only other agents' data** — if so, don't force it; fall back to search + the assigned +
   referenced sets. When it *does* return the person's data it's the best allocation
   signal, so cross-reference it against Step 4.
3. **Referenced tickets.** Activity often names its ticket explicitly — a **ticket number
   embedded in a filename, email subject, or meeting title** (e.g. `4877498 - Enable -
   MSP RFP`). Verify each with `get_one_ticket`; if it returns "not found / no access", the
   person can't see it — treat it as weak/unmapped (⚠️, explain in Notes). When activity
   points at a client but no ticket number, `search_tickets` by client/keyword — this
   matters more now that the assigned list is capped.

Some report tools are preset (no date/agent parameters) and return large org-wide dumps —
often written to a file — that truncate (oldest-first ones lose recent dates; newest-first
ones like the time-logged report only reach back a few days), or come back empty under
reduced permissions. Parse the file and filter to the person + day; if you can't isolate the
day's data, say so rather than guessing, and rely on `get_assigned_tickets` +
`search_tickets` + referenced tickets.

## Step 6 — Map activities to tickets

Match on client name, ticket subject keywords, and embedded ticket numbers. Gauge how
confident each mapping is and surface it **in how you present the ticket** (Step 7) — a
single clear suggestion when sure, stacked alternatives when unsure, or a ⚠️ no-fit marker.
There is no confidence or notes column:
- **Strong** — an explicit, verifiable link (ticket number embedded in the artifact, a
  meeting unambiguously tied to a ticket's client + topic, or a ticket the person actually
  opened/actioned that day per Step 5) **and** the person is the assigned agent. Suggest the
  one ticket plainly.
- **Tentative** — a thematic match, inferred rather than explicit. Suggest it; if a second
  ticket is also plausible, **list both** (best guess first) so the person can pick.
- **Weak / unmapped** — ambiguous, or the best match is a ticket the person isn't assigned
  to / can't access. If there's a plausible candidate, still list it as a suggestion; if
  nothing fits, show **`⚠️ no suitable ticket`** with a brief category hint.

Rules that make the output trustworthy and match how people actually book time:
- **Include internal / non-billable meetings** (team meetings, award ceremonies, all-hands,
  1:1s). Map these to the literal text **"Internal Meeting"** rather than a specific ticket.
- **Exclude personal calendar entries** (school runs, lunch, medical, social invites,
  declined events). Judge by the content of the entry, not by who's on it.
- **Split unrelated tasks that share a time block into separate rows**, even if their
  times overlap — e.g. if someone updated an unrelated webinar doc in the middle of a long
  build session, that's its own row. One row = one coherent piece of work mapping to one
  ticket (overlapping times across rows are fine).
- Don't fabricate precise durations for heads-down evening/weekend work you can only see
  through file-save timestamps — represent it as a block and flag that continuous effort
  is uncertain so the person can trim it.
- **Check what's already logged for the day — from a source that actually works.** Two
  tools are wrong for this and will mislead you: `get_one_ticket` (its `actions` field is
  *available actions*, not time charges) and a per-agent "actions logged by technician"
  report (frequently returns an empty `[]` even when time exists). Use instead:
  - **Daily total (reliable):** a **daily-utilisation / per-agent daily-hours report** lists
    every agent's booked hours per weekday, is small and **not truncated**, and includes the
    person — use it to get **how many hours they've already logged for the target day**. This
    is the dependable check; do it first.
  - **Per-ticket split (best-effort):** a **Technician Time Logged report** (`Who` /
    `Ticket Number` / `Time Taken`) gives the per-ticket breakdown, but it's a large org-wide
    **newest-first** dump that truncates after a few days — so the person can be absent from
    the readable slice even when their daily total is clearly non-zero. Parse the file and
    filter to `Who` = the person; if they're not in it, you have the total but not the split.

  Then:
  - If the daily total shows they've **already logged most/all of the day**, say so plainly
    (Step 7) and treat the reconstruction as a **cross-check / gap-fill**, not a fresh set of
    entries to add. Don't re-propose a full day of logging over the top of it.
  - Mark a row **`✓ already logged`** only when you actually matched its entry in the
    per-ticket report. If you have only the daily total, don't guess per-row — surface the
    logged total under the table and leave rows unmarked.
  - **Top-up** — where a ticket shows some time but less than the activity, note the shortfall.

### Get the ticket ID right, not just the category

Two failure modes to design against — both about naming a real ticket ID rather than a
vague bucket:

- **If you can name the category, resolve it to a concrete ID.** Recurring non-project work
  (licensing, partnership / practice-lead / marketing, product dev, internal tooling)
  usually lives on the person's standing "bucket" tickets — often prefixed with their
  initials (e.g. "GB Microsoft Licensing assistance", "GB Microsoft Practice Lead
  responsibilities"). If you can name the bucket you can find it: `search_tickets` for it and
  cite the **actual ticket ID**. Never leave a mappable row as a vague "…bucket" when a quick
  search yields the number — the capped assigned list won't contain most of these.
- **Remember the person's buckets across runs.** Keep a small per-person map of recurring
  activity → ticket IDs at **`~/.claude/timesheet-my-day/ticket-map.json`**, e.g.
  `{ "microsoft licensing": 4590845, "practice lead / partnership / webinars": 4581819,
  "cost to serve / managed-service product dev": 4548920 }`. Read it at the start of Step 6
  and map recurring work by ID directly — more reliable than a lucky search. It starts empty
  for a new person and **grows from corrections: whenever the person fixes a mapping, offer
  to add it to the map** so it's right next time.

### Delivery work belongs on the project task, not the presales ticket

For a client's *delivery* activity (design workshops, build/config, implementation
sessions), the right ticket is usually a live **project task**, not the sales artefacts.
Subjects containing **"LoE/SoW", "HLSE", "Pricing", "RFP", "Parent Project"** are presales
or umbrella tickets — time rarely goes there. So:
- Prefer a specific **child project task** over the parent project or the LoE/SoW ticket.
- When a search lands on a parent/umbrella ticket, drill into its **child tasks** — via a
  project-tasks report, the "New Child Ticket created. ID: …" breadcrumbs in ticket history,
  or a follow-up search on the **specific phase/topic** (e.g. "H12" or "Enforce Logon
  Restrictions", not just the client + programme name) — and pick the task that matches the
  activity.
- Search with the activity's **distinctive tokens**, and try more than one term; a broad
  client+programme search often returns only the umbrella ticket and hides the real task.

## Step 7 — Build the timesheet table (the deliverable)

Output a single table in the person's local timezone. Use **exactly** these columns:

```
| # | Start–Finish | Hrs | What you did | Suggested Halo ticket |
```

- **What you did** — write this so the person can **paste it straight into the Halo time
  entry** as the work description. Make it **customer-facing and outcome-focused**: what was
  achieved or progressed, in plain past tense, concise. **Do not mention the sources** you
  reconstructed it from (calendar, email, documents, wiki, chat) or internal tooling — those
  mean nothing to the customer and shouldn't appear in a ticket note. Mirror the person's own
  past time-entry notes for tone and length where you can read examples (e.g. a ticket's
  action history); otherwise keep to a short achievement statement.
  - Good: "Facilitated the H12 design workshop and agreed the approach for enforcing logon
    restrictions; captured actions and next steps."
  - Good: "Drafted the Phase 3 Statement of Work and reviewed third-party requirements."
  - Avoid: "Edited the H12 scope doc and joined the Teams call" — names tools, not outcomes.
- **Suggested Halo ticket** — hyperlink the ID and put the **ticket name beside it**:
  `[<id>](<link>) – <ticket name>`, with the ID as the visible link text (use the `link`
  field the Halo tools return; never paste the raw URL). **If more than one ticket is a
  plausible home, list them stacked** — best guess first, each on its own line, each
  hyperlinked with its name — so the person can pick the right one. Use `Internal Meeting` for
  non-billable time. If nothing fits, put **`⚠️ no suitable ticket`** plus a 2–4 word category
  hint. Append **`✓ already logged`** only when you verified the entry is already booked.
- Escape or remove any `|` characters inside cell text (e.g. a ticket named
  "Power Performer | Awards") so they don't break the table columns.

Below the table, keep it to just the totals — **no "areas to check", per-row recap, gaps,
or advice sections:**
- **Total reconstructed hours ≈ X** (for `⚠️ top up` rows count only the shortfall).
- **Already logged in Halo: Z h** for this day (from the daily-utilisation check), so about
  **X − Z** still to add or verify. Omit this line only if no logged figure could be read.

---

### Read-only: never write to HaloPSA

This skill is **strictly read-only against Halo**. It reads (identity, assigned tickets,
ticket lookups, searches, reports) to build the proposed timesheet, and **never writes to
Halo under any circumstances.**

Do not call any mutating Halo tool — logging time (`log_time`), adding notes or actions
(`add_note_to_ticket`, `action_ticket`), creating/assigning/updating tickets
(`create_ticket`, `assign_to_me`, `log_service_request`, `apply_suggestion`), or anything
similar — **even if such tools are available, the connector has write permission, or the
person explicitly asks you to.** There is no confirmation that unlocks writing here; the
answer is always no.

The deliverable is the table, for the person to enter into Halo themselves. If asked to log
or write anything, decline and explain the skill is read-only by design, then hand over the
table (or a CSV export) for them to enter manually. Entering time is a deliberate human
step, kept out of this tool on purpose.
