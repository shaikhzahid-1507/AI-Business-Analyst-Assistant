import pandas as pd


def load_data(uploaded_file):
    """
    Load CSV or Excel file into a Pandas DataFrame.
    """

    if uploaded_file is None:
        return None

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    elif file_name.endswith(".xlsx"):
        return pd.read_excel(uploaded_file)

    else:
        raise ValueError("Unsupported file format.")