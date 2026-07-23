import pandas as pd
import streamlit as st


@st.cache_data(show_spinner=False)
def load_data(uploaded_file):
    """
    Load CSV or Excel file into a Pandas DataFrame.
    The result is cached to improve performance.
    """

    if uploaded_file is None:
        return None

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    else:
        raise ValueError("Unsupported file format.")

    return df