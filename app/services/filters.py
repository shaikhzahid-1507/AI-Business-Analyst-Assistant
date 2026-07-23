import pandas as pd


def apply_business_filters(df, filters):
    """
    Apply all business filters.
    """

    filtered_df = df.copy()

    # --------------------------
    # Multi-select filters
    # --------------------------

    if filters["gender"]:
        filtered_df = filtered_df[
            filtered_df["gender"].isin(filters["gender"])
        ]

    if filters["contract"]:
        filtered_df = filtered_df[
            filtered_df["Contract"].isin(filters["contract"])
        ]

    if filters["payment"]:
        filtered_df = filtered_df[
            filtered_df["PaymentMethod"].isin(filters["payment"])
        ]

    if filters["internet"]:
        filtered_df = filtered_df[
            filtered_df["InternetService"].isin(filters["internet"])
        ]

    if filters["churn"]:
        filtered_df = filtered_df[
            filtered_df["Churn"].isin(filters["churn"])
        ]

    if filters["senior"]:
        filtered_df = filtered_df[
            filtered_df["SeniorCitizen"].isin(filters["senior"])
        ]

    if filters["partner"]:
        filtered_df = filtered_df[
            filtered_df["Partner"].isin(filters["partner"])
        ]

    if filters["dependents"]:
        filtered_df = filtered_df[
            filtered_df["Dependents"].isin(filters["dependents"])
        ]

    # --------------------------
    # Range Filters
    # --------------------------

    tenure_min, tenure_max = filters["tenure"]

    filtered_df = filtered_df[
        (filtered_df["tenure"] >= tenure_min)
        &
        (filtered_df["tenure"] <= tenure_max)
    ]

    monthly_min, monthly_max = filters["monthly"]

    filtered_df = filtered_df[
        (filtered_df["MonthlyCharges"] >= monthly_min)
        &
        (filtered_df["MonthlyCharges"] <= monthly_max)
    ]

    return filtered_df