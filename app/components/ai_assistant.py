import streamlit as st


def show_ai_assistant():
    """
    Display AI Decision Assistant.
    """

    st.divider()

    st.header("🤖 AI Decision Assistant")

    st.caption(
        "Ask questions about your business dataset."
    )

    question = st.text_input(
        "Business Question",
        placeholder="Example: Why is customer churn high?"
    )

    return question