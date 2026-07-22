import pandas as pd


def detect_business_risk(df: pd.DataFrame):
    """
    Detect business risk based on churn rate.
    """

    churn_rate = (df["Churn"] == "Yes").mean() * 100

    if churn_rate >= 40:
        return {
            "level": "High",
            "icon": "🔴",
            "message": "Customer churn is critically high. Immediate retention strategies are required."
        }

    elif churn_rate >= 20:
        return {
            "level": "Medium",
            "icon": "🟡",
            "message": "Customer churn is moderate. Improve engagement and monitor high-risk customers."
        }

    else:
        return {
            "level": "Low",
            "icon": "🟢",
            "message": "Customer churn is under control. Continue maintaining customer satisfaction."
        }