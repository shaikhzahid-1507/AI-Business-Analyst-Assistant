from io import BytesIO
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer


def generate_executive_summary_pdf(kpis, summary):
    """
    Generate Executive Summary PDF.
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
            "Executive Summary Report",
            styles["Heading2"],
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph("<b>Business KPIs</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            f"Total Customers: {kpis['total_customers']}",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            f"Average Monthly Charges: ${kpis['average_monthly']}",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            f"Average Tenure: {kpis['average_tenure']} Months",
            styles["BodyText"],
        )
    )

    story.append(
        Paragraph(
            f"Churn Rate: {kpis['churn_rate']}%",
            styles["BodyText"],
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "<b>Executive Summary</b>",
            styles["Heading2"],
        )
    )

    story.append(
        Paragraph(
            summary,
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