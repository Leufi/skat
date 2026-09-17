#!/usr/bin/env python3
"""One-page CV PDF for the portfolio download button."""
from pathlib import Path
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import ListFlowable, ListItem, Paragraph, SimpleDocTemplate, Spacer

OUT = Path(__file__).resolve().parents[1] / "samuel-kofi-agyei-tuffour-cv.pdf"
INK = HexColor("#1a1f2b")
MUTE = HexColor("#5a6478")
GREEN = HexColor("#0a7a56")


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle("name", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=16, textColor=INK, leading=20, spaceAfter=2),
        "role": ParagraphStyle("role", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=10, textColor=GREEN, leading=13, spaceAfter=6),
        "meta": ParagraphStyle("meta", parent=base["Normal"], fontName="Helvetica", fontSize=8.5, textColor=MUTE, leading=12, spaceAfter=10),
        "h": ParagraphStyle("h", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=9, textColor=GREEN, leading=12, spaceBefore=8, spaceAfter=3, tracking=0.6),
        "body": ParagraphStyle("body", parent=base["Normal"], fontName="Helvetica", fontSize=8.6, textColor=INK, leading=11.4),
        "job": ParagraphStyle("job", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=9, textColor=INK, leading=12, spaceBefore=4),
        "when": ParagraphStyle("when", parent=base["Normal"], fontName="Helvetica", fontSize=8, textColor=MUTE, leading=11, spaceAfter=1),
        "li": ParagraphStyle("li", parent=base["Normal"], fontName="Helvetica", fontSize=8.5, textColor=INK, leading=11.2),
    }


def bullets(items, s):
    return ListFlowable(
        [ListItem(Paragraph(i, s["li"]), leftIndent=10, bulletColor=GREEN) for i in items],
        bulletType="bullet",
        leftIndent=12,
        bulletFontName="Helvetica",
        bulletFontSize=8,
        spaceBefore=1,
        spaceAfter=2,
    )


def main():
    s = styles()
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=12 * mm,
        title="Samuel Kofi Agyei-Tuffour — IT Security & Identity Engineer CV",
        author="Samuel Kofi Agyei-Tuffour",
    )
    story = [
        Paragraph("Samuel Kofi Agyei-Tuffour", s["name"]),
        Paragraph("IT Security &amp; Identity Engineer · Entra ID · IAM", s["role"]),
        Paragraph(
            "Rotterdam, Netherlands · kofileumas@gmail.com · linkedin.com/in/s-k-agyei-tuffour<br/>"
            "Open to IT security and identity / IAM roles in the Netherlands",
            s["meta"],
        ),
        Paragraph("PROFILE", s["h"]),
        Paragraph(
            "IT security and identity engineer. I came into this after a bank my father's firm "
            "guarded was hit through a compromised identity. Telecom diploma, then computer "
            "science (identity and access control), then a cybersecurity master's on IAM and GRC. "
            "SevenX was part-time while I was still in school. After a year in the Hunt&amp;Hackett "
            "SOC I moved to SysOps, where I own the IT security of Entra ID, Azure, Intune, "
            "SharePoint, Atlassian, and 1Password — access reviews, joiner / mover / "
            "leaver. SC-100 (2026), AZ-500 (2025).",
            s["body"],
        ),
        Paragraph("EXPERIENCE", s["h"]),
        Paragraph("SysOps Engineer — Hunt&amp;Hackett", s["job"]),
        Paragraph("The Hague, NL · Jan 2025 – Present", s["when"]),
        bullets(
            [
                "One of two on SysOps. Own the IT security of Entra ID, Azure, Intune, SharePoint, Atlassian, and 1Password — including access reviews.",
                "Conditional Access, PIM, and Entra ID Governance so least privilege is the default, not a cleanup project.",
                "IAM automation platform (Django, Graph API) that cut access-review effort by 25%.",
                "Passwordless (YubiKey) and Intune-managed workspaces; 15% lower identity risk metrics.",
            ],
            s,
        ),
        Paragraph("SOC Engineer — Hunt&amp;Hackett", s["job"]),
        Paragraph("The Hague, NL · Jan 2024 – Dec 2024", s["when"]),
        bullets(
            [
                "Microsoft 365 and Azure incidents: identity misuse, bad access, how people actually got into the tenant.",
                "Tuned detections so identity misuse was visible — 12% better detection efficiency, 20% fewer false positives.",
            ],
            s,
        ),
        Paragraph("IT Security Analyst — SevenX", s["job"]),
        Paragraph("Kigali, Rwanda · Feb 2021 – Aug 2023 · part-time / internship", s["when"]),
        bullets(
            [
                "Day-to-day IT security: access control, identity provisioning, and who could use which systems.",
                "Internal security audits, then stayed with the findings until they were fixed.",
                "Access policy and training for 30+ colleagues; compliance went up after that.",
            ],
            s,
        ),
        Paragraph("SELECTED WORK", s["h"]),
        bullets(
            [
                "<b>Access Register</b> — Who can open which Entra app, including group-granted access, plus leftover M365 accounts.",
                "<b>grurpID</b> — JML platform for employee account lifecycle and access; 25% less manual IAM effort.",
                "<b>ExitScan</b> — Leaver offboarding and orphaned-account detection across downstream apps.",
                "<b>AuditVault</b> — ISO 27001 evidence packs from identity logs.",
            ],
            s,
        ),
        Paragraph("SKILLS", s["h"]),
        Paragraph(
            "<b>Identity:</b> Entra ID, PIM, Conditional Access, FIDO2, JML, access reviews, IAM / IGA.<br/>"
            "<b>IT security:</b> Microsoft 365, Intune, SharePoint permissions, Atlassian, 1Password.<br/>"
            "<b>Automation:</b> Python, Django, Microsoft Graph API, Logic Apps.<br/>"
            "<b>Audits:</b> ISO 27001, SOC 2, evidence from identity logs.",
            s["body"],
        ),
        Paragraph("EDUCATION &amp; CERTIFICATIONS", s["h"]),
        bullets(
            [
                "MSc Cybersecurity — National Forensic Sciences University, India (scholarship; IAM and GRC)",
                "BSc (Hons) Computer Science — PDM University, India (identity and access control)",
                "Diploma, Telecommunication Engineering — GCTU, Ghana",
                "Systemic Design — Digital Society School, Netherlands",
                "Microsoft Certified: Cybersecurity Architect Expert (SC-100), 2026",
                "Microsoft Certified: Azure Security Engineer Associate (AZ-500), 2025",
            ],
            s,
        ),
    ]
    doc.build(story)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
