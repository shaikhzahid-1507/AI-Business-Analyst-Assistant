import pandas as pd


def apply_filters(df: pd.DataFrame, filters: dict):
    """
    Apply sidebar filters to the dataset.
    """

    filtered_df = df.copy()

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

    return filtered_df