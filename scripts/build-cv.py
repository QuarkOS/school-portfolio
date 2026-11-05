#!/usr/bin/env python3
"""Rebuild EN/DE CVs from the live portfolio PDFs, without a phone number."""

from pathlib import Path

from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUT = Path(__file__).resolve().parents[1] / "public"

LINKS = {
    "linkedin": "https://www.linkedin.com/in/emilio-schwaiger-429948328/",
    "github": "https://github.com/QuarkOS",
    "portfolio": "https://emilioschwaiger.com",
    "cairn": "https://github.com/QuarkOS/Cairn",
    "pifusion": "https://github.com/QuarkOS/Pi-Fusion",
}


def styles():
    base = getSampleStyleSheet()
    s = {
        "name": ParagraphStyle(
            "Name",
            parent=base["Title"],
            fontName="Times-Bold",
            fontSize=22,
            leading=26,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=9.5,
            leading=12,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "role": ParagraphStyle(
            "Role",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=12,
            leading=15,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "summary": ParagraphStyle(
            "Summary",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=10,
            leading=13,
            alignment=TA_JUSTIFY,
            spaceAfter=10,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=12,
            leading=15,
            spaceBefore=8,
            spaceAfter=2,
            borderPadding=0,
        ),
        "jobTitle": ParagraphStyle(
            "JobTitle",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=10.5,
            leading=13,
        ),
        "jobMeta": ParagraphStyle(
            "JobMeta",
            parent=base["Normal"],
            fontName="Times-Italic",
            fontSize=10,
            leading=13,
        ),
        "date": ParagraphStyle(
            "Date",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=10,
            leading=13,
            alignment=TA_RIGHT,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=10,
            leading=13,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=10,
            leading=13,
        ),
        "projTitle": ParagraphStyle(
            "ProjTitle",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=10.5,
            leading=13,
            spaceBefore=4,
        ),
        "skillLabel": ParagraphStyle(
            "SkillLabel",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=10,
            leading=13,
        ),
        "skillBody": ParagraphStyle(
            "SkillBody",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=10,
            leading=13,
        ),
    }
    return s


def rule():
    t = Table([[""]], colWidths=[170 * mm], rowHeights=[0.6])
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 1, "black")]))
    return t


def job(s, title, dates, italic, bullets):
    head = Table(
        [
            [
                Paragraph(title, s["jobTitle"]),
                Paragraph(dates, s["date"]),
            ]
        ],
        colWidths=[130 * mm, 40 * mm],
    )
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    items = [
        ListItem(Paragraph(b, s["bullet"]), leftIndent=8, bulletColor="black")
        for b in bullets
    ]
    return [
        head,
        Paragraph(italic, s["jobMeta"]),
        ListFlowable(items, bulletType="bullet", start="circle", leftIndent=14, bulletFontSize=8),
        Spacer(1, 4),
    ]


def skill_row(s, label, body):
    t = Table(
        [[Paragraph(label, s["skillLabel"]), Paragraph(body, s["skillBody"])]],
        colWidths=[32 * mm, 138 * mm],
    )
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ]
        )
    )
    return t


def contact_line(place, email):
    return (
        f"{place} | {email} | "
        f'<link href="{LINKS["linkedin"]}"><u>LinkedIn</u></link> | '
        f'<link href="{LINKS["github"]}"><u>GitHub</u></link> | '
        f'<link href="{LINKS["portfolio"]}"><u>Portfolio</u></link>'
    )


def build_en(path: Path, s):
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=16 * mm,
        bottomMargin=16 * mm,
        title="CV Emilio Schwaiger",
        author="Emilio Schwaiger",
    )
    story = [
        Paragraph("Emilio Schwaiger", s["name"]),
        Paragraph(contact_line("Großarl, Austria", "schwaiger.emilio@gmail.com"), s["contact"]),
        Paragraph("Software Engineer", s["role"]),
        Paragraph(
            "Software engineer building with multi-agent AI (Cursor + Grok Bots). HTL Saalfelden Informatik; Matura expected 2027.",
            s["summary"],
        ),
        Paragraph("INTERNSHIPS", s["h2"]),
        rule(),
        Spacer(1, 6),
        *job(
            s,
            "Bauen &amp; Wohnen",
            "07/2022–08/2022",
            "Carpentry company",
            [
                "Duration: 4 weeks",
                "Tasks: Mix of workshop work and IT projects, including installing a UniFi system to improve the network",
            ],
        ),
        *job(
            s,
            "Bauen &amp; Wohnen",
            "07/2023–08/2023",
            "Carpentry company",
            [
                "Duration: 4 weeks",
                "Tasks: General IT work, including IT support and improvements to existing software",
            ],
        ),
        *job(
            s,
            "Amari Austria GmbH",
            "07/2025–08/2025",
            "Aluminum manufacturer",
            [
                "Duration: 4 weeks",
                "Tasks: Built a warehouse system for automatic allocation and management.",
                "General IT support, employee lists, and license management",
            ],
        ),
        *job(
            s,
            "Amari Austria GmbH",
            "07/2026–08/2026",
            "Aluminum manufacturer",
            [
                "Duration: 4 weeks",
                "Tasks: Excel automation and finance processes with Python and database queries",
            ],
        ),
        Paragraph("PROJECTS", s["h2"]),
        rule(),
        Paragraph("Cairn (Open Source)", s["projTitle"]),
        Paragraph(
            f'Typed facts for AI agents: agents store, recall, and retract knowledge over JSON or MCP, also as a Cursor plugin. TypeScript, Node.js. On npm as @quarkos/cairn (version 0.5.0). <link href="{LINKS["cairn"]}"><u>github.com/QuarkOS/Cairn</u></link>',
            s["body"],
        ),
        Paragraph("Pi-Fusion (Open Source)", s["projTitle"]),
        Paragraph(
            f'Lets multiple AI models deliberate on a task together, as an extension for the Pi Coding Agent. TypeScript, Node.js. On npm as @quarkos/pi-fusion (version 1.0.12). <link href="{LINKS["pifusion"]}"><u>github.com/QuarkOS/Pi-Fusion</u></link>',
            s["body"],
        ),
        Paragraph("QStack", s["projTitle"]),
        Paragraph(
            "Verification on real Ubuntu, Fedora, and Windows VMs — proves changes beyond compile checks.",
            s["body"],
        ),
        Paragraph("Homelab", s["projTitle"]),
        Paragraph(
            f'Self-hosted on Proxmox (LXC) behind Cloudflare Tunnel and Access: <link href="{LINKS["portfolio"]}"><u>Portfolio</u></link>, Factorio blueprint gallery, file upload with Google login, and throwaway VMs for testing.',
            s["body"],
        ),
        Paragraph("EDUCATION", s["h2"]),
        rule(),
        Spacer(1, 4),
        Table(
            [
                [
                    Paragraph("HTL SAALFELDEN", s["jobTitle"]),
                    Paragraph("Salzburg, AT", s["date"]),
                ],
                [
                    Paragraph("Informatik (Matura expected 2027)", s["jobMeta"]),
                    Paragraph("2022–2027", s["date"]),
                ],
            ],
            colWidths=[130 * mm, 40 * mm],
        ),
        Paragraph("Five-year Informatik track at HTL Saalfelden", s["body"]),
        Paragraph(
            "Focus areas: programming, data science &amp; artificial intelligence, databases, and networking",
            s["body"],
        ),
        Paragraph("CERTIFICATES &amp; SKILLS", s["h2"]),
        rule(),
        Spacer(1, 6),
        skill_row(s, "Certificates:", "Introduction To Java – Hyperskill / JetBrains Academy"),
        skill_row(s, "Programming:", "TypeScript, JavaScript, Python, Java, C#, C, GLSL"),
        skill_row(
            s,
            "Web &amp; data:",
            "Node.js, Next.js, React, Auth.js (Google OAuth), SQLite, Drizzle, Microsoft SQL Server, Excel automation",
        ),
        skill_row(
            s,
            "Testing &amp; tools:",
            "Vitest, Playwright, Git, GitHub, npm, Docker, MCP, AI coding agents (Cursor)",
        ),
        skill_row(
            s,
            "Infrastructure:",
            "Linux (Fedora, Debian), Proxmox VE / LXC, Cloudflare Tunnel and Access, systemd, UniFi",
        ),
        skill_row(s, "Languages:", "German (native), English (fluent)"),
    ]
    doc.build(story)


def build_de(path: Path, s):
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=16 * mm,
        bottomMargin=16 * mm,
        title="Lebenslauf Emilio Schwaiger",
        author="Emilio Schwaiger",
    )
    story = [
        Paragraph("Emilio Schwaiger", s["name"]),
        Paragraph(contact_line("Großarl, Österreich", "schwaiger.emilio@gmail.com"), s["contact"]),
        Paragraph("Softwareentwickler", s["role"]),
        Paragraph(
            "Softwareentwickler mit Multi-Agent-KI (Cursor + Grok Bots). Informatik an der HTL Saalfelden; Matura voraussichtlich 2027.",
            s["summary"],
        ),
        Paragraph("PRAKTIKA", s["h2"]),
        rule(),
        Spacer(1, 6),
        *job(
            s,
            "Bauen &amp; Wohnen",
            "07/2022–08/2022",
            "Tischler-Unternehmen",
            [
                "Dauer: 4 Wochen",
                "Tätigkeiten: Kombination von handwerklichen Aufgaben und Informatikprojekten, einschließlich der Installation eines UniFi-Systems zur Verbesserung der Netzwerkstruktur",
            ],
        ),
        *job(
            s,
            "Bauen &amp; Wohnen",
            "07/2023–08/2023",
            "Tischler-Unternehmen",
            [
                "Dauer: 4 Wochen",
                "Tätigkeiten: Allgemeine Informatikaufgaben, inkl. IT-Support und Verbesserungen an den bereits bestehenden Softwarelösungen",
            ],
        ),
        *job(
            s,
            "Amari Austria GmbH",
            "07/2025–08/2025",
            "Aluminiumhersteller",
            [
                "Dauer: 4 Wochen",
                "Tätigkeiten: Lagersystem erstellt für automatische Lagerzuweisung und Verwaltung.",
                "Allgemeinere IT-Support-Aufgaben, Mitarbeiterlisten- und Lizenzverwaltung",
            ],
        ),
        *job(
            s,
            "Amari Austria GmbH",
            "07/2026–08/2026",
            "Aluminiumhersteller",
            [
                "Dauer: 4 Wochen",
                "Tätigkeiten: Excel-Automatisierung und Finanzprozesse mit Python und Datenbankabfragen",
            ],
        ),
        Paragraph("PROJEKTE", s["h2"]),
        rule(),
        Paragraph("Cairn (Open Source)", s["projTitle"]),
        Paragraph(
            f'Typisierte Fakten für KI-Agenten: Agenten speichern, abrufen und widerrufen Wissen über JSON oder MCP, auch als Cursor-Plugin. TypeScript, Node.js. Auf npm als @quarkos/cairn (Version 0.5.0). <link href="{LINKS["cairn"]}"><u>github.com/QuarkOS/Cairn</u></link>',
            s["body"],
        ),
        Paragraph("Pi-Fusion (Open Source)", s["projTitle"]),
        Paragraph(
            f'Lässt mehrere KI-Modelle gemeinsam über eine Aufgabe beraten, als Erweiterung für den Pi Coding Agent. TypeScript, Node.js. Auf npm als @quarkos/pi-fusion (Version 1.0.12). <link href="{LINKS["pifusion"]}"><u>github.com/QuarkOS/Pi-Fusion</u></link>',
            s["body"],
        ),
        Paragraph("QStack", s["projTitle"]),
        Paragraph(
            "Verifikation auf echten Ubuntu-, Fedora- und Windows-VMs — prüft Änderungen über Compile-Checks hinaus.",
            s["body"],
        ),
        Paragraph("Homelab", s["projTitle"]),
        Paragraph(
            f'Selbst gehostet auf Proxmox (LXC) hinter Cloudflare Tunnel und Access: <link href="{LINKS["portfolio"]}"><u>Portfolio</u></link>, Factorio-Blueprint-Galerie, Datei-Upload mit Google-Login und Wegwerf-VMs zum Testen.',
            s["body"],
        ),
        Paragraph("BILDUNG", s["h2"]),
        rule(),
        Spacer(1, 4),
        Table(
            [
                [
                    Paragraph("HTL SAALFELDEN", s["jobTitle"]),
                    Paragraph("Salzburg, AT", s["date"]),
                ],
                [
                    Paragraph("Informatik (Matura voraussichtlich 2027)", s["jobMeta"]),
                    Paragraph("2022–2027", s["date"]),
                ],
            ],
            colWidths=[130 * mm, 40 * mm],
        ),
        Paragraph("Fünfjährige Informatik-Ausbildung an der HTL Saalfelden", s["body"]),
        Paragraph(
            "Schwerpunkte: Programmierung, Data Science &amp; Artificial Intelligence, Datenbanken und Netzwerksysteme",
            s["body"],
        ),
        Paragraph("ZERTIFIKATE &amp; SKILLS", s["h2"]),
        rule(),
        Spacer(1, 6),
        skill_row(s, "Zertifikate:", "Introduction To Java – Hyperskill / JetBrains Academy"),
        skill_row(s, "Programmieren:", "TypeScript, JavaScript, Python, Java, C#, C, GLSL"),
        skill_row(
            s,
            "Web &amp; Daten:",
            "Node.js, Next.js, React, Auth.js (Google OAuth), SQLite, Drizzle, Microsoft SQL Server, Excel-Automatisierung",
        ),
        skill_row(
            s,
            "Testen &amp; Tools:",
            "Vitest, Playwright, Git, GitHub, npm, Docker, MCP, KI-Coding-Agenten (Cursor)",
        ),
        skill_row(
            s,
            "Infrastruktur:",
            "Linux (Fedora, Debian), Proxmox VE / LXC, Cloudflare Tunnel and Access, systemd, UniFi",
        ),
        skill_row(s, "Sprachen:", "Deutsch (Muttersprache), Englisch (Fließend)"),
    ]
    doc.build(story)


def main():
    s = styles()
    en = OUT / "cv.pdf"
    de = OUT / "lebenslauf.pdf"
    build_en(en, s)
    build_de(de, s)
    print("wrote", en, en.stat().st_size)
    print("wrote", de, de.stat().st_size)


if __name__ == "__main__":
    main()
