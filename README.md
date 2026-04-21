# finaegis.github.io

Source for the FinAegis open-source portfolio at <https://finaegis.github.io/>.

Single static page, no framework, no build step. Deploys from `main` via GitHub Pages.

## What this is (and isn't)

This is a **developer-facing index** of FinAegis's public open-source projects. It is not a marketing site — FinAegis has those at <https://finaegis.org/> and <https://aegisbrightsmark.com/>.

Full positioning and constraints in [`CLAUDE.md`](CLAUDE.md); detailed spec in [`requirements.md`](requirements.md).

## Local preview

```
python3 -m http.server 8000
# then open http://localhost:8000
```

No install step.

## Contributing

Adding a new FinAegis public project: edit `index.html` (or `projects.json`, depending on which option the current implementation uses — see [`requirements.md#6`](requirements.md#6-tech-choices--decide-during-implementation)), commit, open a PR. Verify the repo is public and has a description before listing it.

## License

MIT. Site content and code.
