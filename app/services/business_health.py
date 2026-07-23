def calculate_business_health(kpis):
    """
    Calculate overall business health score.
    """

    score = 100

    # Churn Impact
    if kpis["churn_rate"] > 30:
        score -= 30
    elif kpis["churn_rate"] > 20:
        score -= 15

    # Tenure Impact
    if kpis["average_tenure"] < 24:
        score -= 15

    # Revenue Impact
    if kpis["average_monthly"] < 50:
        score -= 10

    if score >= 90:
        status = "Excellent 🟢"

    elif score >= 75:
        status = "Good 🟢"

    elif score >= 60:
        status = "Needs Attention 🟡"

    else:
        status = "Critical 🔴"

    return {
        "score": score,
        "status": status,
    }