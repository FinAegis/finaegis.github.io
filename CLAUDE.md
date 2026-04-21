# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Product: FinAegis OSS portfolio

A single-page developer-facing index of FinAegis's public open-source projects, deployed at <https://finaegis.github.io/> via GitHub Pages. Authoritative requirements in [`requirements.md`](requirements.md).

## Positioning — read this before touching copy

This is **not** a marketing site. FinAegis already has two of those:

- <https://finaegis.org/> — product brand (FinAegis core-banking platform).
- <https://aegisbrightsmark.com/> — parent company (services, careers, portfolio).

`finaegis.github.io` exists for a different audience: developers who landed here from a `README.md`, `composer.json`, or `package.json` in one of our public repos, and want to see what else the org ships. Different audience → different content → different tone.

Think `airbnb.io`, `netflix.github.io`, `linkedin.github.io`, `shopify.github.io` — terse, technical, link-heavy. No hero photos, no stock imagery, no testimonials, no sales CTAs. **Prospects go to `finaegis.org` / `aegisbrightsmark.com`; developers stay here.**

## Architecture

**Static single-page site.** No build step, no framework, no backend. One `index.html` with inline CSS, deployed from `main` by GitHub Pages' default action.

- Org-level GitHub Pages: the repo at `FinAegis/finaegis.github.io` serves as the org root (`finaegis.github.io/`). Conventional.
- Project tiles are authored inline in `index.html` (or in a small sidecar JSON that `index.html` reads — [`requirements.md`](requirements.md) has the decision).
- No Tailwind, no Next, no Astro. Plain HTML + one `<style>` block keeps the deploy trivial and the page <20 KB over the wire.

## Hard constraints — do not violate

- **No duplicate of `finaegis.org` or `aegisbrightsmark.com`.** If a section starts feeling like a company pitch, it's in the wrong place — link to the corporate site instead.
- **No external script/font/CSS CDNs.** Inline the CSS. System font stack. Keeps load fast and the privacy story clean.
- **No analytics yet.** If we add it later, disclose on the page.
- **No JavaScript frameworks.** Vanilla only. This site exists to list repos and link to them; shipping React for that is a waste.
- **Public repos only.** Never list private FinAegis repos. Tiles must link to live, public GitHub URLs.

## Coding conventions

- Semantic HTML: `<header>`, `<main>`, `<section>`, `<footer>`, `<article>` for tiles.
- Accessibility: `prefers-color-scheme` dark mode, visible focus states, `alt` on every `<img>`, semantic heading hierarchy.
- Match the Google-blue accent (`#1a73e8` light / `#8ab4f8` dark) already used on <https://finaegis.github.io/defluff/> — visual consistency across FinAegis Pages sites matters.

## Working in this repo

- The repo deploys automatically: pushes to `main` trigger GitHub Pages' default workflow. Preview locally with `python3 -m http.server 8000` from the repo root.
- When adding a new FinAegis public repo to the portfolio, verify the description, license, and status on the repo itself first — don't guess. Use `gh repo view FinAegis/<name>`.
