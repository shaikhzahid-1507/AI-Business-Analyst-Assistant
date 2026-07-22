import pandas as pd


def generate_recommendations(df: pd.DataFrame):
    """
    Generate actionable business recommendations.
    """

    recommendations = []

    churn_rate = (df["Churn"] == "Yes").mean() * 100

    # High churn recommendation
    if churn_rate > 30:
        recommendations.append(
            "🔴 High churn detected. Launch an immediate customer retention campaign."
        )
    elif churn_rate > 20:
        recommendations.append(
            "🟡 Moderate churn detected. Improve customer engagement and loyalty programs."
        )
    else:
        recommendations.append(
            "🟢 Customer churn is under control. Continue monitoring customer satisfaction."
        )

    # Contract recommendation
    top_contract = df["Contract"].value_counts().idxmax()

    if top_contract == "Month-to-month":
        recommendations.append(
            "📄 Encourage Month-to-Month customers to switch to One-Year or Two-Year contracts through discounts or loyalty rewards."
        )

    # Payment recommendation
    top_payment = df["PaymentMethod"].value_counts().idxmax()

    if top_payment == "Electronic check":
        recommendations.append(
            "💳 Promote AutoPay options to reduce payment friction and improve customer retention."
        )

    # Internet recommendation
    top_service = df["InternetService"].value_counts().idxmax()

    if top_service == "Fiber optic":
        recommendations.append(
            "🌐 Monitor Fiber Optic customers closely, as they often represent high-value customers."
        )

    # Revenue recommendation
    avg_monthly = df["MonthlyCharges"].mean()

    if avg_monthly < 50:
        recommendations.append(
            "💰 Explore premium service bundles to increase average monthly revenue."
        )
    else:
        recommendations.append(
            "💰 Maintain current pricing strategy while focusing on customer retention."
        )

    return recommendations