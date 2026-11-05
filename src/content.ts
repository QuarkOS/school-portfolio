/**
 * All visitor-facing copy and links live here.
 * Edit this file (then `npm run build`) instead of hunting through components.
 *
 * EN is the default. DE is the language-toggle locale, matching emilioschwaiger.com.
 * Download counts are a snapshot — update `villagerDownloads` when CurseForge moves.
 */

export const site = {
  url: "https://schoolportfolio.emilioschwaiger.com",
  liveUrl: "https://emilioschwaiger.com",
  title: "Emilio Schwaiger",
  description: {
    en: "Emilio Schwaiger, software engineer. Multi-agent AI workflows. Summer 2027 internships / new-grad screens, Europe/Vienna.",
    de: "Emilio Schwaiger, Softwareentwickler. Multi-Agent-KI-Workflows. Sommer 2027 Praktikum / Berufseinstieg, Europa/Wien.",
  },
} as const;

export const person = {
  name: "Emilio Schwaiger",
  email: "schwaiger.emilio@gmail.com",
  githubUser: "QuarkOS",
  githubUrl: "https://github.com/QuarkOS",
  githubId: 111038444,
  xUrl: "https://x.com/EmilioSchwaiger",
  xHandle: "@EmilioSchwaiger",
  linkedinUrl: "https://www.linkedin.com/in/emilio-schwaiger-429948328/",
  npmUrl: "https://www.npmjs.com/~quarkos",
  amariUrl: "https://www.amari.at/",
  avatarAlt: "GitHub and X avatar: a silver tabby cat with its tongue out.",
} as const;

/** CurseForge snapshot used on the live homepage at port time. */
export const villagerDownloads = 1433;

export const links = {
  villagerReroller: "https://www.curseforge.com/minecraft/mc-mods/reroll-helper",
  writing: {
    "how-i-actually-use-ai-pt-1":
      "https://x.com/EmilioSchwaiger/status/2105918007419564045",
    "grok-bot-setup-after-1-month":
      "https://x.com/EmilioSchwaiger/status/2104310932671451636",
    "2-week-experience-with-grok-bot":
      "https://x.com/EmilioSchwaiger/status/2094566892207747487",
  },
  cv: {
    en: { href: "/cv.pdf", download: "Emilio-Schwaiger-CV.pdf" },
    de: { href: "/lebenslauf.pdf", download: "Emilio-Schwaiger-Lebenslauf.pdf" },
  },
} as const;

export function formatDownloads(n: number, locale: "en" | "de"): string {
  const formatted = n.toLocaleString(locale === "de" ? "de-DE" : "en-US");
  return locale === "de" ? `${formatted} Downloads` : `${formatted} downloads`;
}

export const copy = {
  en: {
    skipToWork: "Skip to work",
    nav: {
      language: "Language",
      theme: "Theme",
      themeLight: "Light",
      themeDark: "Dark",
      downloadCv: "Download CV",
    },
    identity: {
      roleBefore: "Previously",
      amari: "Amari Austria",
    },
    hero: {
      line1: "I ship projects from Austria, built with",
      and: "and",
      thing: "My thing is AI, specifically the setup around a model: the agents, skills and checks that make the same model ship better work.",
    },
    work: {
      kicker: "Work",
      items: [
        {
          name: "Villager Reroller",
          dates: "2026",
          href: links.villagerReroller,
          metric: formatDownloads(villagerDownloads, "en"),
          description:
            "Java Minecraft mod that lists villager trades and rerolls the job site until a chosen offer is cheap enough.",
        },
        {
          name: "Capes",
          dates: "2026",
          status: "in development",
          description:
            "Custom capes visible to other mod users, in 2D, animated, wavy and 3D styles. Fabric and Forge.",
        },
        {
          name: "Cosmetics",
          dates: "2026",
          status: "in development",
          description:
            "3D wearables like wings, plus an animated chick pet that sits on your head or shoulder and reacts to in-game events. Fabric and Forge.",
        },
        {
          name: "Amari Austria",
          dates: "2025–2026",
          href: person.amariUrl,
          description:
            "Warehouse system and IT support (2025), Excel/finance automation with Python (2026).",
        },
      ],
    },
    writing: {
      kicker: "Writing",
      items: [
        {
          slug: "how-i-actually-use-ai-pt-1",
          title: "How I Actually Use AI to Build Software (Pt. 1)",
          dates: "Oct 2026",
          href: links.writing["how-i-actually-use-ai-pt-1"],
          description:
            "My setup from idea to shipped code, and why your AI needs a verification layer.",
        },
        {
          slug: "grok-bot-setup-after-1-month",
          title:
            "My Grok Bot setup after 1 month (and how I stopped burning usage)",
          dates: "Sep 2026",
          href: links.writing["grok-bot-setup-after-1-month"],
          description:
            "Delegating to cloud agents, and throwaway verification VMs on my homelab.",
        },
        {
          slug: "2-week-experience-with-grok-bot",
          title: "My 2-Week Experience with Grok Bot",
          dates: "Aug 2026",
          href: links.writing["2-week-experience-with-grok-bot"],
          description:
            "Running 10 bots at once, burning through usage, and what pstack changed.",
        },
      ],
    },
    currently: {
      kicker: "Currently",
      locationLabel: "location",
      location: "Großarl, Austria",
      nowLabel: "now",
      now: "Getting a SpaceXSI event ready, Matura prep, and my Diplomprojekt for Kindersachenbörse Goldegg",
    },
    reach: {
      heading: "After HTL? Let's talk.",
      body: "I finish my Matura in 2027, then do my Zivildienst. After that I'm looking for my first full-time role in AI and agent tooling. Internships and part-time work before then are welcome too.",
    },
    notFound: {
      title: "That page is not here.",
      back: "Back to Emilio Schwaiger.",
      home: "Home",
    },
  },
  de: {
    skipToWork: "Weiter zur Arbeit",
    nav: {
      language: "Sprache",
      theme: "Darstellung",
      themeLight: "Hell",
      themeDark: "Dunkel",
      downloadCv: "Lebenslauf herunterladen",
    },
    identity: {
      roleBefore: "Zuvor",
      amari: "Amari Austria",
    },
    hero: {
      line1: "Ich shippe Projekte aus Österreich, gebaut mit",
      and: "und",
      thing: "Mein Ding ist KI, genauer das Setup rund um ein Modell: die Agents, Skills und Checks, die dasselbe Modell bessere Arbeit abliefern lassen.",
    },
    work: {
      kicker: "Arbeit",
      items: [
        {
          name: "Villager Reroller",
          dates: "2026",
          href: links.villagerReroller,
          metric: formatDownloads(villagerDownloads, "de"),
          description:
            "Java-Minecraft-Mod, die Villager-Trades listet und den Arbeitsplatz neu setzt, bis ein gewähltes Angebot günstig genug ist.",
        },
        {
          name: "Capes",
          dates: "2026",
          status: "in Entwicklung",
          description:
            "Eigene Capes, sichtbar für andere Mod-Nutzer, in 2D, animiert, wellig und 3D. Fabric und Forge.",
        },
        {
          name: "Cosmetics",
          dates: "2026",
          status: "in Entwicklung",
          description:
            "3D-Wearables wie Flügel, plus ein animiertes Küken-Pet, das auf dem Kopf oder der Schulter sitzt und auf Spielereignisse reagiert. Fabric und Forge.",
        },
        {
          name: "Amari Austria",
          dates: "2025–2026",
          href: person.amariUrl,
          description:
            "Lagersystem und IT-Support (2025), Excel-/Finanzautomatisierung mit Python (2026).",
        },
      ],
    },
    writing: {
      kicker: "Schreiben",
      items: [
        {
          slug: "how-i-actually-use-ai-pt-1",
          title: "How I Actually Use AI to Build Software (Pt. 1)",
          dates: "Oct 2026",
          href: links.writing["how-i-actually-use-ai-pt-1"],
          description:
            "Mein Setup von der Idee bis zum fertigen Code, und warum deine KI eine Verifikationsschicht braucht.",
        },
        {
          slug: "grok-bot-setup-after-1-month",
          title:
            "My Grok Bot setup after 1 month (and how I stopped burning usage)",
          dates: "Sep 2026",
          href: links.writing["grok-bot-setup-after-1-month"],
          description:
            "Arbeit an Cloud-Agents abgeben, und Wegwerf-VMs zur Verifikation in meinem Homelab.",
        },
        {
          slug: "2-week-experience-with-grok-bot",
          title: "My 2-Week Experience with Grok Bot",
          dates: "Aug 2026",
          href: links.writing["2-week-experience-with-grok-bot"],
          description:
            "Zehn Bots gleichzeitig, verbrauchte Usage, und was pstack geändert hat.",
        },
      ],
    },
    currently: {
      kicker: "Aktuell",
      locationLabel: "Ort",
      location: "Großarl, Österreich",
      nowLabel: "jetzt",
      now: "Ein SpaceXSI-Event vorbereiten, Matura-Vorbereitung und mein Diplomprojekt für die Kindersachenbörse Goldegg",
    },
    reach: {
      heading: "Nach der HTL? Lass uns reden.",
      body: "Ich mache 2027 meine Matura, danach meinen Zivildienst. Danach suche ich meine erste Vollzeitstelle im Bereich KI und Agent-Tooling. Praktika und Teilzeit davor sind auch willkommen.",
    },
    notFound: {
      title: "Diese Seite gibt es nicht.",
      back: "Zurück zu Emilio Schwaiger.",
      home: "Start",
    },
  },
} as const;

export type WorkItem = (typeof copy.en.work.items)[number];
export type WritingItem = (typeof copy.en.writing.items)[number];
