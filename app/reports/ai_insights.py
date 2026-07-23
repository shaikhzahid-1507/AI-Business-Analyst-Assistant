from io import BytesIO
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)


def generate_ai_insights_pdf(insights):
    """
    Generate AI Insights PDF.
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>AI Business Analyst Assistant</b>",
            styles["Title"],
        )
    )

    story.append(
        Paragraph(
            "AI Business Insights Report",
            styles["Heading2"],
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "<b>Business Insights</b>",
            styles["Heading2"],
        )
    )

    # Handle either a list of insights or a single string
    if isinstance(insights, list):
        for insight in insights:
            story.append(
                Paragraph(
                    f"• {insight}",
                    styles["BodyText"],
                )
            )
    else:
        story.append(
            Paragraph(
                str(insights),
                styles["BodyText"],
            )
        )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d %B %Y')}",
            styles["Italic"],
        )
    )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf