import pandas as pd


def profile_data(df: pd.DataFrame):
    """
    Generate basic profiling information for a dataset.
    """

    profile = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "memory_usage_mb": round(
            df.memory_usage(deep=True).sum() / (1024 ** 2), 2
        ),
        "numeric_columns": len(
            df.select_dtypes(include=["number"]).columns
        ),
        "categorical_columns": len(
            df.select_dtypes(include=["object", "category"]).columns
        ),
    }

    return profile


def missing_values_summary(df):
    """
    Return missing values count and percentage for each column.
    """

    missing = df.isnull().sum()

    percentage = (missing / len(df) * 100).round(2)

    summary = pd.DataFrame(
        {
            "Column": missing.index,
            "Missing Values": missing.values,
            "Missing %": percentage.values,
        }
    )

    summary = summary[summary["Missing Values"] > 0]

    summary = summary.sort_values(
        by="Missing Values",
        ascending=False
    ).reset_index(drop=True)

    return summary


def data_type_summary(df):
    """
    Return summary of data types.
    """

    summary = (
        df.dtypes.astype(str)
        .value_counts()
        .reset_index()
    )

    summary.columns = [
        "Data Type",
        "Count",
    ]

    # Convert to normal Python strings
    summary["Data Type"] = summary["Data Type"].astype(str)

    return summary
    summary.columns = [
        "Data Type",
        "Count"
    ]

    return summary
def descriptive_statistics(df):
    """
    Return descriptive statistics for numerical columns.
    """

    stats = (
        df.describe()
        .transpose()
        .round(2)
        .reset_index()
    )

    stats.rename(
        columns={"index": "Column"},
        inplace=True,
    )

    return stats
def categorical_summary(df):
    """
    Return summary for categorical columns.
    """

    categorical_columns = [
        col
        for col in df.select_dtypes(
            include=["object", "category"]
        ).columns
        if "id" not in col.lower()
    ]

    summary = []

    for column in categorical_columns:

        mode = df[column].mode()

        if len(mode) > 0:
            most_frequent = mode.iloc[0]
            frequency = df[column].value_counts().iloc[0]
        else:
            most_frequent = "-"
            frequency = 0

        summary.append({
            "Column": column,
            "Unique Values": df[column].nunique(),
            "Most Frequent": most_frequent,
            "Frequency": frequency,
        })

    return pd.DataFrame(summary)
def correlation_matrix(df):
    """
    Return correlation matrix for numerical columns.
    """

    numeric_df = df.select_dtypes(include=["number"])

    correlation = numeric_df.corr().round(2)

    return correlation
def numeric_columns(df):
    """
    Return all numeric columns.
    """

    return df.select_dtypes(include=["number"]).columns.tolist()