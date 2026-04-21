# FinAegis OSS portfolio — requirements

_Last updated: 2026-04-21_

Authoritative spec for the single-page site served at <https://finaegis.github.io/>. Read [`CLAUDE.md`](CLAUDE.md) first — it covers positioning ("this is not a marketing site") and hard constraints.

## 1. Goal

Give a developer who arrived here from a FinAegis public repo's README a one-page answer to **"what else does FinAegis build, and where's the code?"** — in under 10 seconds, on a 400 KB bandwidth budget, without JavaScript.

Secondary goal: make the two sibling brands (`finaegis.org`, `aegisbrightsmark.com`) discoverable so that non-developers who land here by accident can find the right door.

## 2. Non-goals

- Replace or duplicate `finaegis.org` or `aegisbrightsmark.com`.
- Marketing copy. Feature lists. Customer logos. Testimonials. Case studies.
- Dynamic content requiring a backend or a build step.
- SEO-optimized lead generation. This is a developer utility, not a funnel.
- Listing private repos. Ever.

## 3. Audience

- Developer who saw a FinAegis project in the wild and wants to see the org's other public work.
- Contributor looking for a second project to pick up after landing a PR elsewhere.
- Security researcher auditing the org's open-source surface.

None of these want a sales pitch. All want fast access to repo links, license info, activity status, and the right entry-point per project.

## 4. Content model

### 4.1 Header

- Wordmark "FinAegis" (text, not a logo image — keep it text-scalable).
- One-line framing: _"Open-source work by the team behind `finaegis.org`. Part of [Aegis Brightsmark](https://aegisbrightsmark.com)."_ — or a variant that makes the relationship clear without burying the dev focus.
- Right-aligned links: **Projects** (anchor `#projects`), **GitHub org**, **finaegis.org**, **Aegis Brightsmark**.

### 4.2 Hero / intro (minimal)

Two sentences max, above the project grid. Something like:

> _"Banking infrastructure, AI tools, and developer SDKs. Everything in this index is open-source and welcomes PRs; commercial support flows through [finaegis.org](https://finaegis.org)."_

No headline. No image. No CTA button. The grid IS the CTA.

### 4.3 Project grid — the core of the page

Grid of tiles. Responsive (3 columns → 2 → 1). Each tile is a clickable card linking to the GitHub repo.

**Each tile renders:**

- Project name (heading, `<h3>`).
- One-line description (the GitHub repo's description, verbatim — not a rewritten marketing variant).
- Primary language (`TypeScript`, `PHP`, etc.).
- License (`MIT`, `Apache-2.0`, or "Proprietary" with a link to the LICENSE file — check before labelling).
- Star count (optional — omit if 0 to avoid looking anemic; show if ≥ 1).
- Status badge: `Active` / `Beta` / `Preview` / `Archived`. Manual, not derived from `updatedAt`.
- Repo URL (the whole card links here).
- Live/demo URL where one exists (separate inline link, labelled, e.g. "Live →").

**Projects to include (curated — not all public repos belong in the grid):**

| Order | Repo | Live link | Status | Notes |
|---|---|---|---|---|
| 1 | [FinAegis/core-banking-prototype-laravel](https://github.com/FinAegis/core-banking-prototype-laravel) | — | `Active` | 160★. DDD/CQRS/event-sourced. The flagship. |
| 2 | [FinAegis/defluff](https://github.com/FinAegis/defluff) | <https://finaegis.github.io/defluff/> | `Active` | Browser extension + Outlook add-in. MIT. |
| 3 | [FinAegis/cli](https://github.com/FinAegis/cli) | — | `Active` | Zelta CLI. Auto-synced mirror — note that in the tile. |
| 4 | [FinAegis/php-sdk](https://github.com/FinAegis/php-sdk) | — | `Active` | FinAegis PHP SDK. Mirror. |
| 5 | [FinAegis/payment-sdk](https://github.com/FinAegis/payment-sdk) | — | `Active` | Zelta Payment SDK. Mirror. |

**Skip `FinAegis/.github`** — that's the org profile repo, not a project.

**The three "mirror" repos:** they auto-sync from subdirectories of `core-banking-prototype-laravel`. Consider a secondary tier ("SDKs & tooling" subheading) below the two headliners so they don't visually compete with the flagship. The next-session implementer decides the exact grouping — but the mirrors must not dominate the layout.

**Live products without public code (like Zelta at `zelta.app`):** may be mentioned once in prose below the grid, not as a tile. Tiles are for things with a public repo.

### 4.4 Footer

- Copyright line: "© FinAegis · Part of Aegis Brightsmark".
- Inline links: GitHub org, finaegis.org, aegisbrightsmark.com, contact (if we decide on a contact method — email or GitHub Issues).

## 5. Visual direction

- **Accent color:** Google blue `#1a73e8` (light) / `#8ab4f8` (dark). Matches `finaegis.github.io/defluff/`. Consistency across FinAegis Pages sites is a feature, not a coincidence.
- **Font:** system stack only — `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`. No web fonts.
- **Layout:** max-width 960–1040 px container. Generous whitespace. 1 px borders, 8 px radii.
- **Dark mode:** via `prefers-color-scheme`. Background `#202124`, foreground `#e8eaed`, muted `#9aa0a6`, border `#3c4043`.
- **No decorative imagery.** No hero screenshot. No background patterns. The project tiles ARE the visual interest.

**Reference feel:** <https://shopify.github.io/>, <https://netflix.github.io/>, <https://airbnb.io/>. Terse, technical, link-heavy.

## 6. Tech choices — decide during implementation

Two viable paths. Pick one; don't do both.

### 6.1 Static inline (recommended)

Project list authored inline in `index.html`. Adding a project = edit one HTML file + commit. Simple, zero runtime cost, works without JS.

### 6.2 Static + JSON data file

`projects.json` holds the tile list; `index.html` ships a tiny vanilla-JS renderer. Slightly nicer for contribution workflow if the list grows past ~10 projects. Adds a `<script>` tag but no frameworks, no build step.

### 6.3 What NOT to do

- No client-side fetch to GitHub's REST API. Reasons: rate limits (60/hr unauthenticated per IP), flicker on load, adds a dependency on external availability, and the freshness win is marginal (we curate the list anyway).
- No SSG (Astro/Eleventy/etc.) — overkill for a single page.
- No Tailwind. No frameworks. No build step.

## 7. Accessibility & SEO

- Valid semantic HTML. Pass `html-validate` / `axe` / Lighthouse ≥ 95 for both Accessibility and Best Practices on a first run.
- Meta description + `og:title` + `og:description`. No `og:image` unless we author a purpose-built one.
- Add `finaegis.github.io` to Google Search Console if/when the user wants indexing. Reuse the existing `google-site-verification` meta from `finaegis.github.io/defluff/` only if the same GSC property owns the root — otherwise get a fresh verification token.
- Robots: allow all. This is a public index; indexing is the point.

## 8. Deployment

- Repo: `FinAegis/finaegis.github.io` (the convention for org-root Pages sites).
- GitHub Pages → Deploy from `main` branch, `/` root. No build workflow needed — Pages serves `index.html` directly.
- First deploy verification:
  1. After `main` is pushed, check **Settings → Pages** for the deploy status.
  2. Expect HTTPS auto-provisioning; `http://finaegis.github.io/` should 301 to `https://`.
  3. The `/defluff/` subpath on the same origin is served by a different repo (`FinAegis/defluff`) — verify that path still resolves after this repo is live.

## 9. Done criteria

- [ ] Single `index.html` live at `https://finaegis.github.io/`.
- [ ] Five project tiles render, each linking to the correct repo.
- [ ] Live-link row shows `finaegis.github.io/defluff/` on the Defluff tile.
- [ ] Header + footer both link to `finaegis.org` and `aegisbrightsmark.com`.
- [ ] Dark mode works via `prefers-color-scheme`.
- [ ] Page weight under 20 KB over the wire (HTML + inline CSS).
- [ ] Lighthouse ≥ 95 on Accessibility, Best Practices, SEO.
- [ ] `finaegis.github.io/defluff/` still resolves after deploy (regression check).
