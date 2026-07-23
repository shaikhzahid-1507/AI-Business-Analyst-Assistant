def generate_executive_alerts(kpis):
    """
    Generate executive business alerts.
    """

    alerts = []

    # -----------------------------
    # Churn
    # -----------------------------
    if kpis["churn_rate"] >= 30:
        alerts.append({
            "level": "error",
            "title": "High Churn Risk",
            "message": "Customer churn is high. Immediate retention strategies are recommended."
        })

    elif kpis["churn_rate"] >= 20:
        alerts.append({
            "level": "warning",
            "title": "Moderate Churn",
            "message": "Customer churn should be monitored carefully."
        })

    else:
        alerts.append({
            "level": "success",
            "title": "Healthy Churn",
            "message": "Customer churn is within an acceptable range."
        })

    # -----------------------------
    # Revenue
    # -----------------------------
    if kpis["average_monthly"] >= 80:
        alerts.append({
            "level": "success",
            "title": "Revenue Performance",
            "message": "Average monthly revenue is performing well."
        })

    elif kpis["average_monthly"] >= 60:
        alerts.append({
            "level": "warning",
            "title": "Revenue Opportunity",
            "message": "Revenue is stable, but upselling opportunities exist."
        })

    else:
        alerts.append({
            "level": "error",
            "title": "Low Revenue",
            "message": "Revenue is below the expected business target."
        })

    # -----------------------------
    # Retention
    # -----------------------------
    if kpis["average_tenure"] >= 36:
        alerts.append({
            "level": "success",
            "title": "Customer Retention",
            "message": "Customers are staying with the company for a healthy duration."
        })

    elif kpis["average_tenure"] >= 24:
        alerts.append({
            "level": "warning",
            "title": "Retention",
            "message": "Retention is average. Loyalty initiatives could improve it."
        })

    else:
        alerts.append({
            "level": "error",
            "title": "Low Retention",
            "message": "Customer tenure is low. Retention strategies should be reviewed."
        })

    return alerts