def answer_business_question(question, df, kpis):
    """
    Rule-based AI assistant.
    """

    question = question.lower()

    if "churn" in question:

        churn = kpis["churn_rate"]

        if churn >= 30:

            return (
                f"The churn rate is {churn:.2f}%, which is considered high.\n\n"
                "Recommended actions:\n"
                "- Improve customer support\n"
                "- Introduce loyalty programs\n"
                "- Review contract plans"
            )

        return (
            f"The churn rate is {churn:.2f}% and appears to be under control."
        )

    elif "revenue" in question:

        revenue = kpis["average_monthly"]

        return (
            f"The average monthly revenue per customer is ${revenue:.2f}.\n\n"
            "Potential improvements:\n"
            "- Upsell premium plans\n"
            "- Cross-sell additional services\n"
            "- Increase customer retention"
        )

    elif "customer" in question:

        total = kpis["total_customers"]

        return (
            f"The dataset currently contains {total:,} customers."
        )

    elif "tenure" in question:

        tenure = kpis["average_tenure"]

        return (
            f"The average customer tenure is {tenure:.2f} months."
        )

    elif "summary" in question:

        return (
            "Business Summary\n\n"
            f"• Customers : {kpis['total_customers']:,}\n"
            f"• Churn Rate : {kpis['churn_rate']:.2f}%\n"
            f"• Avg Monthly Charges : ${kpis['average_monthly']:.2f}\n"
            f"• Avg Tenure : {kpis['average_tenure']:.2f} months"
        )

    return (
        "I couldn't understand your question.\n\n"
        "Try asking:\n"
        "• Why is churn high?\n"
        "• Revenue summary\n"
        "• Customer summary\n"
        "• Business summary\n"
        "• Average tenure"
    )