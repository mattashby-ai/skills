# Connector detection reference

The skill depends on several data-source connectors, exposed as MCP tools. **MCP server
IDs are opaque, environment-specific hashes and differ between users** — never hardcode
them. Instead, recognise a connector by the *capability* of the tools it exposes. Tool
schemas are often deferred; discover them with `ToolSearch` (e.g. keyword searches like
`calendar events`, `gmail threads`, `drive files`, `slack messages`, `confluence pages`,
`getConfluencePage searchConfluenceUsingCql`, `assigned tickets`) before deciding a source
is absent. A connector added mid-session may not appear in the deferred-tool snapshot until
a `ToolSearch` surfaces it — probe for it rather than assuming it's absent.

## Source → typical tool signatures + exact connector name

The **"Connector name to look for"** column is what to tell the user to search for in the
connector directory when a source is missing, and what to pass to `suggest_connectors`
(when available) to surface a one-click Connect button.

| Source | What it provides | Tools that indicate it's present (examples) | Connector name to look for |
|---|---|---|---|
| **Calendar** | Meetings attended | `list_events`, `list_calendars`, `search_events` | **Google Calendar** |
| **Email** | Messages the person sent | `search_threads`, `get_thread`, `list_messages` | **Gmail** |
| **Files / Docs** | Docs created / edited / viewed | `list_recent_files`, `search_files`, `read_file_content`, `get_file_metadata` | **Google Drive** |
| **Chat** | Messages/threads sent | `search_messages`, `conversations_history`, `list_channels` | **Slack** |
| **Wiki** | Confluence pages viewed / edited / created (also Jira issues) | `getConfluencePage`, `getPagesInConfluenceSpace`, `searchConfluenceUsingCql`, `atlassianUserInfo`, `getAccessibleAtlassianResources`, plus a generic `search` / `fetch` | **Atlassian Rovo** (Confluence + Jira) |
| **PSA / ticketing** | Assigned tickets + time logging | `get_assigned_tickets`, `get_one_ticket`, `search_tickets`, `get_user_info`, `log_time` | **HaloPSA** (production) |

Match on capability, not exact tool names — a connector may name its tools differently
while doing the same job. Connector display names can change over time; if the registry
tools (`search_mcp_registry`) are available, confirm the current exact name there, then
fall back to the names above.

## HaloPSA: require the PRODUCTION instance

Time logged to a dev/sandbox Halo is worthless, so the connected Halo must be the real
production instance. Check any instance URL you can see — ticket `link` fields,
`get_user_info` output, action links — for dev/test markers in the hostname:

- **The Instillery, specifically:** dev = **`dev-agent.theinstillery.com`**, production =
  **`agent.theinstillery.com`**. The `dev-` hostname prefix is the tell — if it's there,
  it's the dev instance; the bare `agent.` host is production.
- More generally, treat these hostname markers as dev/sandbox: `dev-`, `sandbox`, `test`,
  `uat`, `staging`. Production typically has none of them.

If the connected Halo is a dev instance: **classify HaloPSA as Not connected ✗**, and in
the note say the *dev* connector is connected but production isn't. Do not map or log time
against it. If you genuinely can't tell prod from dev, say so and ask the user to confirm
before logging anything.

**Reduced-permission production connectors.** The production connector is often scoped
tighter than dev, which changes tool behaviour (not whether it's "connected"):
- `get_assigned_tickets` may return a **flat, capped array with no pagination** (e.g. only
  ~5 active/primary assignments) rather than the full assigned list. Treat it as a starting
  set, not exhaustive.
- `get_one_ticket` still reads individual tickets — including ones the person isn't assigned
  to — so it's the reliable way to verify referenced tickets and reach beyond the capped
  list.
- Canned CF reports (e.g. actions-logged-by-technician) may return **empty or other agents'
  data** under the reduced scope. Don't depend on them; lean on `search_tickets` +
  `get_one_ticket`.

## Atlassian Rovo (the Wiki source)

Confluence/Jira access comes through the **Atlassian Rovo** connector. Recognise it by its
tools rather than a fixed name — the tell-tales are `atlassianUserInfo`,
`getAccessibleAtlassianResources`, `getConfluencePage`, `getPagesInConfluenceSpace`,
`getConfluenceSpaces`, and `searchConfluenceUsingCql`. Some Rovo builds also expose Jira
(`getJiraIssue`, `searchJiraIssuesUsingJql`) and a generic `search` / `fetch`, but the
Confluence tools are the ones this skill relies on. Exact tool names vary between Rovo
builds; match on capability.

To reconstruct the day, pull the pages the person **viewed, updated, or created** for that
date. Rovo search is CQL-driven, so:
- **Created by them:** CQL `creator = currentUser() and created >= "<date>"`.
- **Edited/contributed by them:** CQL `contributor = currentUser() and lastModified >= "<date>"`
  (this is the strongest heads-down signal — a page they actually changed).
- **Viewed by them:** best-effort. CQL has no clean "viewed by me" filter; use a
  recently-viewed tool if Rovo exposes one, otherwise treat viewed-only pages as weak
  context, not evidence of billable work.
- Resolve `currentUser()` from `atlassianUserInfo` first, and scope to the person's cloud
  site via `getAccessibleAtlassianResources` if more than one is accessible.

Convert Confluence timestamps to the person's local timezone like every other source, and
map an edited/created page to a ticket the same way as a Drive doc (client name + subject
keywords + any embedded ticket number in the page title).

## Classifying each source

- **Connected ✓** — a matching tool exists and a probe call returns data (or an empty but
  successful result). For HaloPSA, also passes the production check above.
- **Needs authorisation ⚠️** — a matching tool exists but calls fail with an auth /
  permission / "not authorised" / expired-token error. The capability is installed but not
  usable yet; the fix is to (re)authorise it, not to install anything. If
  `suggest_connectors` is available, pass the failed tool's server UUID (from the
  `mcp__{uuid}__{tool}` name) to prompt re-authentication.
- **Not connected ✗** — no tool with the matching capability is present, even after a
  `ToolSearch` — or, for HaloPSA, only a dev instance is connected.

## Notes and gotchas

- **Browsing history is not a tracked source.** It was dropped because there's no useful
  browsing-history data connector: browser-*automation* tools (Playwright, Claude-in-Chrome,
  etc.) can drive a page but can't read local history, and scraping `chrome://history` is
  unreliable and privacy-invasive. Don't add it back or send the user hunting for one.
- **PSA is the pivot.** If the PSA/ticketing connector is missing, unauthorised, or only
  dev, you can still assemble an activity log, but you cannot map to (or log against) real
  tickets — say this clearly and early.
- **Don't over-probe.** One light call per source is enough to distinguish connected from
  unauthorised; you don't need to pull full data just to test presence.
- **RMM / remote-session tools are out of scope.** Systems like ConnectWise
  Automate/ScreenConnect are deliberately not connected (customer-access and security
  implications). Don't recommend connecting them; treat RMM and hands-on device work as a
  manual blind spot the person notes themselves.
- **Adjacent stacks.** This skill was first built around Google Workspace + Slack +
  Confluence + HaloPSA, but the same capability-based detection works for Microsoft 365
  (Outlook/OneDrive/SharePoint/Teams) or another PSA — map the equivalent tools to the same
  source categories, and name the corresponding connector when one is missing.
