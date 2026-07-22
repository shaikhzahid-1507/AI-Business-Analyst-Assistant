import pandas as pd


# ==========================================================
# BUSINESS KPIs
# ==========================================================

def business_kpis(df: pd.DataFrame):
    """
    Generate business KPI metrics.
    """

    total_customers = len(df)

    average_monthly = round(
        df["MonthlyCharges"].mean(),
        2
    )

    average_tenure = round(
        df["tenure"].mean(),
        2
    )

    churn_rate = round(
        (df["Churn"] == "Yes").mean() * 100,
        2
    )

    return {
        "total_customers": total_customers,
        "average_monthly": average_monthly,
        "average_tenure": average_tenure,
        "churn_rate": churn_rate,
    }


# ==========================================================
# CHURN
# ==========================================================

def churn_distribution(df):
    """
    Return churn distribution.
    """

    churn = (
        df["Churn"]
        .value_counts()
        .reset_index()
    )

    churn.columns = [
        "Churn",
        "Customers"
    ]

    return churn


# ==========================================================
# MONTHLY CHARGES
# ==========================================================

def monthly_charges(df):
    """
    Return Monthly Charges column.
    """

    return df["MonthlyCharges"]


# ==========================================================
# CONTRACT
# ==========================================================

def contract_distribution(df):
    """
    Return contract distribution.
    """

    contract = (
        df["Contract"]
        .value_counts()
        .reset_index()
    )

    contract.columns = [
        "Contract",
        "Customers"
    ]

    return contract


# ==========================================================
# PAYMENT METHOD
# ==========================================================

# ==========================================================
# PAYMENT METHOD
# ==========================================================

def payment_distribution(df):
    """
    Return payment method distribution.
    """

    payment = (
        df["PaymentMethod"]
        .value_counts()
        .reset_index()
    )

    payment.columns = [
        "Payment Method",
        "Customers"
    ]

    return payment


# ==========================================================
# TENURE
# ==========================================================

def tenure_distribution(df):
    """
    Return Tenure column.
    """

    return df["tenure"]