import streamlit as st

from components.header import show_header
from components.sidebar import show_sidebar
from components.uploader import upload_file
from services.data_loader import load_data


def main():
    st.set_page_config(
        page_title="AI Business Analyst Assistant",
        page_icon="🤖",
        layout="wide"
    )

    show_sidebar()
    show_header()

    uploaded_file = upload_file()

    if uploaded_file is not None:
        try:
            df = load_data(uploaded_file)

            st.success("✅ File uploaded successfully!")

            st.write("### Dataset Preview")
            st.dataframe(df.head())

            st.write(f"**Rows:** {df.shape[0]}")
            st.write(f"**Columns:** {df.shape[1]}")

        except Exception as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()