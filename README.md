# school-portfolio

Static port of [emilioschwaiger.com](https://emilioschwaiger.com) for **schoolportfolio.emilioschwaiger.com**.

Same layout, type, and copy as the live Next.js site — not a redesign. Built with [Astro](https://astro.build) (`output: 'static'`) so the Abgabe is a folder of HTML/CSS/JS/assets.

Hosted later by Portato from `dist/`. This repo does not set DNS.

## Why Astro

- **`output: 'static'`** produces `dist/` with `index.html` at the root. No Node server, no React hydration (the live site’s locale/theme flash is a hydration concern; this port applies theme and language in a blocking `<head>` script).
- Content sits in **one module** (`src/content.ts`), which is easier to edit for school than a Next.js app router tree.
- EN/DE are both in the HTML; CSS hides the inactive locale. That matches the live toggle without shipping a JS framework.

Eleventy would also have worked. Astro is closer to the live React markup and still emits a static tree.

## Local run

Needs Node 22+.

```bash
npm install
npm run dev
```

Open the URL Astro prints (default `http://localhost:4321`).

```bash
npm run build     # writes dist/
npm run preview   # serves dist/
npm run pack      # build + artifacts/school-portfolio-dist.tar.gz
```

## Edit content

All visitor-facing copy and links: **`src/content.ts`**.

| What | Where |
| --- | --- |
| Name, email, GitHub / X / LinkedIn | `person` |
| Villager Reroller download count | `villagerDownloads` |
| Work / writing / currently / CTA | `copy.en` and `copy.de` |
| CV files | `public/cv.pdf`, `public/lebenslauf.pdf` (live copy **without phone**; regenerate with `python3 scripts/build-cv.py`) |
| Avatar | `public/images/avatar.jpg` (GitHub user `111038444`) |

Then `npm run build`. Do not put a phone number anywhere. Spell **SpaceXSI** (not SpaceXAI). If an Impressum is required: Name + Großarl only.

## Publish static files

1. `npm run build`
2. The folder **`dist/`** is the site (`index.html` at the root).
3. Hand `dist/` (or `artifacts/school-portfolio-dist.tar.gz`) to Portato for `schoolportfolio.emilioschwaiger.com`.

No Umami, Clarity, or other trackers. Fonts are self-hosted under `public/fonts/` (Syne + IBM Plex, OFL). No Google Fonts CDN.

Desktop/mobile screenshots vs the live site are in `artifacts/` (including side-by-side comparisons). `npm run pack` writes `artifacts/school-portfolio-dist.tar.gz` with `index.html` at the archive root.

## Policy this port follows

- Visual + textual match with the live portfolio (EN default, DE toggle).
- No phone number.
- SpaceXSI spelling in Currently.
- No third-party analytics.
- Self-hosted fonts.
- Public GitHub: [QuarkOS/school-portfolio](https://github.com/QuarkOS/school-portfolio).
