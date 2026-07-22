import streamlit as st


def upload_file():
    """
    Display a file uploader and return the uploaded file.
    """

    st.subheader("📂 Upload Your Dataset")

    uploaded_file = st.file_uploader(
        label="Choose a CSV or Excel file",
        type=["csv", "xlsx"]
    )

    return uploaded_file