import pandas as pd


def generate_executive_summary(df: pd.DataFrame):
    """
    Generate an executive business summary.
    """

    total_customers = len(df)

    churn_rate = (df["Churn"] == "Yes").mean() * 100

    avg_monthly = df["MonthlyCharges"].mean()

    avg_tenure = df["tenure"].mean()

    top_contract = df["Contract"].value_counts().idxmax()

    top_payment = df["PaymentMethod"].value_counts().idxmax()

    top_internet = df["InternetService"].value_counts().idxmax()

    summary = f"""
This dashboard analyzes **{total_customers:,} customers**.

The current **churn rate is {churn_rate:.2f}%**, indicating a {'high' if churn_rate > 40 else 'moderate' if churn_rate > 20 else 'low'} level of customer churn.

The average monthly charge is **${avg_monthly:.2f}**, while the average customer tenure is **{avg_tenure:.1f} months**.

Most customers use **{top_contract}** contracts, **{top_payment}** as their payment method, and **{top_internet}** internet service.
"""

    return summary