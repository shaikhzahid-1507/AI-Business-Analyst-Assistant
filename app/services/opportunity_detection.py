import pandas as pd


def detect_business_opportunities(df: pd.DataFrame):
    """
    Identify business growth opportunities.
    """

    opportunities = []

    avg_tenure = df["tenure"].mean()

    if avg_tenure > 30:
        opportunities.append(
            "🎯 Long customer tenure indicates strong customer loyalty. Consider launching referral programs."
        )

    avg_monthly = df["MonthlyCharges"].mean()

    if avg_monthly > 60:
        opportunities.append(
            "💰 Customers generate healthy monthly revenue. Premium service bundles may increase revenue further."
        )

    contract = df["Contract"].value_counts().idxmax()

    if contract != "Two year":
        opportunities.append(
            "📄 Encourage customers to upgrade to long-term contracts for better retention."
        )

    internet = df["InternetService"].value_counts().idxmax()

    if internet == "Fiber optic":
        opportunities.append(
            "🌐 Fiber Optic customers represent a valuable customer segment. Consider exclusive offers for this group."
        )

    if len(opportunities) == 0:
        opportunities.append(
            "✅ No major business opportunities detected from the current filtered dataset."
        )

    return opportunities