from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Image, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.utils import ImageReader


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "story-001.pdf"

SCENES = [
    (
        "Scene 1 - The playground",
        ROOT / "cartoon" / "case001.jpeg",
        [
            "On the **way** to the playground, Miller wears a silly **dress** and plays **tag** and **hide-and-seek**. His friends **pick up** the **rest** of the **balloons** and **add** them to their toy **trucks**.",
            "They run **near** the **slides**, balance on the **boards**, and shoot **hoops**.",
        ],
    ),
    (
        "Scene 2 - The clown show",
        ROOT / "cartoon" / "case002.jpeg",
        [
            "**Far** across the room, a **bat** begins to **glide** **near** a fish **tank** under a bright **ray** of light.",
            "A **clown** in a funny **costume** begins to **juggle**. He decides to **show** us a silly **act**, and then he takes a **bow**.",
        ],
    ),
    (
        "Scene 3 - The beach workshop",
        ROOT / "cartoon" / "case003.jpeg",
        [
            "At the beach, the children use **science** to **dig** for **shells** and **build** sand **castles**.",
            "They **build** a monster from **wood**, **stone**, and **metal**, tie it with **rope**, and place it beside the castles. Their newly **built** monster looks funny but friendly.",
        ],
    ),
    (
        "Scene 4 - Baking and making",
        ROOT / "cartoon" / "case004.jpeg",
        [
            "By **myself**, I **mix** **flour** and **butter** near the **oven**, then **roll** out the dough and **fold** it over.",
            "Finally, I **tear** a sheet of paper, **fold** it into a box, and use **glue** and **tape** to hold it together.",
        ],
    ),
]


def bold_words(text: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)


def fit_image(path: Path, max_width: float, max_height: float) -> Image:
    width, height = ImageReader(str(path)).getSize()
    scale = min(max_width / width, max_height / height)
    return Image(str(path), width=width * scale, height=height * scale)


def add_page_number(canvas, document) -> None:
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#68727c"))
    canvas.drawCentredString(A4[0] / 2, 12 * mm, f"Miller Words - Story 001 - Page {document.page}")
    canvas.restoreState()


styles = getSampleStyleSheet()
title = ParagraphStyle("Title", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=22, leading=26, textColor=colors.HexColor("#24313d"), alignment=TA_CENTER, spaceAfter=4)
intro = ParagraphStyle("Intro", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.5, leading=13, textColor=colors.HexColor("#68727c"), alignment=TA_CENTER, spaceAfter=10)
scene_title = ParagraphStyle("SceneTitle", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=colors.HexColor("#24313d"), spaceAfter=5)
body = ParagraphStyle("Body", parent=styles["BodyText"], fontName="Helvetica", fontSize=10.5, leading=14, textColor=colors.HexColor("#24313d"), spaceAfter=5)


def build() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=13 * mm,
        bottomMargin=18 * mm,
        title="Miller's Amazing Day - Story 001",
        author="Miller Words",
    )
    story = [Paragraph("Miller's Amazing Day", title), Paragraph("Story 001 - Read aloud, then cover the labels and retell each scene.", intro)]
    for index, (heading, image_path, sentences) in enumerate(SCENES):
        block = [Paragraph(heading, scene_title), fit_image(image_path, 178 * mm, 42 * mm)]
        block.extend(Paragraph(bold_words(sentence), body) for sentence in sentences)
        story.append(KeepTogether(block))
        story.append(Spacer(1, 7 * mm))
        if index == 1:
            story.append(PageBreak())
            story.append(Paragraph("Miller's Amazing Day", title))
            story.append(Paragraph("Story 001 - Read aloud, then cover the labels and retell each scene.", intro))
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build()
