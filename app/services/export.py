import pandas as pd


def dataframe_to_csv(df):
    """
    Convert a DataFrame into CSV bytes.
    """

    return df.to_csv(index=False).encode("utf-8")