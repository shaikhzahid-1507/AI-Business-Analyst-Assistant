import streamlit as st


def show_header():
    """
    Displays the application header.
    """

    st.title("🤖 AI Business Analyst Assistant")

    st.markdown(
        """
        Welcome to the **AI Business Analyst Assistant**.

        Upload your business dataset and let AI help you:
        - 📊 Explore your data
        - 📈 Generate insights
        - 📉 Create visualizations
        - 💡 Answer business questions
        """
    )

    st.divider()