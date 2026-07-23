from io import BytesIO
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)


def generate_business_report(
    kpis,
    summary,
    insights,
    recommendations,
    risk,
    opportunities,
):
    """
    Generate Complete Business Report PDF.
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    # ----------------------------
    # Title
    # ----------------------------

    story.append(
        Paragraph(
            "<b>AI Business Analyst Assistant</b>",
            styles["Title"],
        )
    )

    story.append(
        Paragraph(
            "Complete Business Analysis Report",
            styles["Heading2"],
        )
    )

    story.append(Spacer(1, 20))

    # ----------------------------
    # KPIs
    # ----------------------------

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

    # ----------------------------
    # Executive Summary
    # ----------------------------

    story.append(
        Paragraph("<b>Executive Summary</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(summary, styles["BodyText"])
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph("<b>AI Business Insights</b>", styles["Heading2"])
    )

    if isinstance(insights, list):
        for item in insights:
            story.append(
                Paragraph(f"• {item}", styles["BodyText"])
            )
    else:
        story.append(
            Paragraph(str(insights), styles["BodyText"])
        )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph("<b>Business Recommendations</b>", styles["Heading2"])
    )

    if isinstance(recommendations, list):
        for item in recommendations:
            story.append(
                Paragraph(f"• {item}", styles["BodyText"])
            )
    else:
        story.append(
            Paragraph(str(recommendations), styles["BodyText"])
        )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph("<b>Risk Assessment</b>", styles["Heading2"])
    )

    if isinstance(risk, list):
        for item in risk:
            story.append(
                Paragraph(f"• {item}", styles["BodyText"])
            )
    else:
        story.append(
            Paragraph(str(risk), styles["BodyText"])
        )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph("<b>Growth Opportunities</b>", styles["Heading2"])
    )

    if isinstance(opportunities, list):
        for item in opportunities:
            story.append(
                Paragraph(f"• {item}", styles["BodyText"])
            )
    else:
        story.append(
            Paragraph(str(opportunities), styles["BodyText"])
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