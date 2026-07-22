import pandas as pd


def generate_business_insights(df: pd.DataFrame):
    """
    Generate business insights from the filtered dataset.
    """

    insights = []

    # -----------------------------
    # Churn Rate
    # -----------------------------
    churn_rate = (df["Churn"] == "Yes").mean() * 100

    if churn_rate > 40:
        insights.append(
            "🔴 High churn rate detected. Immediate customer retention strategies are recommended."
        )
    elif churn_rate > 20:
        insights.append(
            "🟡 Moderate churn rate observed. Customer engagement can be improved."
        )
    else:
        insights.append(
            "🟢 Churn rate is healthy."
        )

    # -----------------------------
    # Contract Analysis
    # -----------------------------
    highest_contract = df["Contract"].value_counts().idxmax()

    insights.append(
        f"📄 Most customers are using **{highest_contract}** contracts."
    )

    # -----------------------------
    # Payment Method
    # -----------------------------
    highest_payment = df["PaymentMethod"].value_counts().idxmax()

    insights.append(
        f"💳 Most customers prefer **{highest_payment}**."
    )

    # -----------------------------
    # Internet Service
    # -----------------------------
    highest_service = df["InternetService"].value_counts().idxmax()

    insights.append(
        f"🌐 Most customers use **{highest_service}** internet."
    )

    # -----------------------------
    # Monthly Charges
    # -----------------------------
    avg_charge = df["MonthlyCharges"].mean()

    insights.append(
        f"💰 Average Monthly Charges: **${avg_charge:.2f}**"
    )

    return insights