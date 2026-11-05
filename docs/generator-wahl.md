# Generator-Wahl (Astro)

Kurzantworten für die Präsentation. Darf angepasst werden.

## Warum Astro?

Die Live-Seite ist Next.js. Für die HTL-Abgabe braucht es aber **statische Dateien**, nicht einen Node-Server.

Astro mit `output: 'static'` baut genau das: `dist/index.html` plus CSS, JS und Assets. Es bleibt nah an der Live-HTML-Struktur (Sections, Header, Karten), ohne React-Hydration. Locale und Theme sitzen in einem kurzen Script im `<head>` — kein Aufblitzen, kein Hydration-Mismatch.

Alternativen: Eleventy (noch „statischer“, aber mehr Handarbeit am Markup) oder ein händisches HTML. Astro ist der Kompromiss aus „sieht aus wie die Live-Seite“ und „ist eine Dateiablage“.

## Wie habe ich den Generator verwendet?

- Eine Layout-Vorlage (`src/layouts/Layout.astro`) für Head, Fonts, Theme/Locale-Script.
- Eine Seite (`src/pages/index.astro`) plus 404.
- Komponenten nur dort, wo Wiederholung anfällt (Header, Icons).
- **Alle Texte und Links in `src/content.ts`**, nicht in den Komponenten verstreut.
- CSS: Design-Tokens und Utilities der Live-Seite (Farben, Abstände, Syne / IBM Plex), Fonts lokal.

Befehl: `npm run build` → `dist/`.

## Wie füge ich Inhalte hinzu?

1. `src/content.ts` öffnen.
2. Bei Work/Writing ein Objekt in `copy.en` **und** `copy.de` ergänzen (gleicher Index).
3. Link nach `links` oder `person`, falls neu.
4. `npm run build` und im Browser prüfen.

Download-Zahl von Villager Reroller: Konstante `villagerDownloads` oben in derselben Datei.

## UX dieser Methode

- **EN/DE** ohne Reload: beide Sprachen liegen im HTML, CSS blendet die inaktive aus. Das Script liest `localStorage` vor dem ersten Paint.
- **Hell/Dunkel** gleich: `html.dark` plus `color-scheme`, wie live, ohne React.
- **Avatar** nur ab `md` (Tablet/Desktop), am Handy ausgeblendet — wie live.
- Keine Tracker, keine Font-CDNs: die Seite bleibt auch offline aus `dist/` lesbar.
- Mailto direkt auf dem CTA (live setzt das erst nach Hydration auf `#reach`).

Nachteil: Zwei Sprachen im DOM heißen etwas mehr HTML. Für eine One-Pager-Seite ist das egal.

## Was würde ich anders machen?

- Download-Zahl nicht per Hand, sondern ein kleines Update-Skript gegen CurseForge — für die Schule unnötig.
- Echte Astro Content Collections (`src/content/work/*.md`), falls die Seite wächst. Für vier Work-Zeilen und drei Texte ist ein Modul klarer.
- Impressum nur wenn die Lehrperson es verlangt: Name + Großarl, klein im Footer. Live hat keines, deshalb hier auch keines — Parität vor Extra-Blöcken.
- Pixel-Diffs gegen Screenshots der Live-Seite in CI. Hier reicht der visuelle Abgleich.

## Wo hat KI geholfen?

- Live-HTML, CSS-Tokens, EN/DE-Copy und Font-Subsets von emilioschwaiger.com holen.
- Im Live-Lebenslauf stand eine Telefonnummer; für diese Schulversion entfernt (Policy: kein Telefon).
- Astro-Gerüst, bilinguales Markup, Theme-Script und README/diese Datei formulieren.
- Build, Screenshots, Tarball.

Was ich selbst prüfen muss: Copy (SpaceXSI, kein Telefon), Links, EN/DE-Toggle, Hell/Dunkel, Mobile, und ob `dist/` ohne Server-Logik auskommt.
