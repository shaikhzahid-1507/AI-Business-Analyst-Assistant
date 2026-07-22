import streamlit as st


def show_executive_summary(summary):
    """
    Display the executive business summary.
    """

    st.divider()
    st.header("📋 Executive Business Summary")

    st.success(
        "This summary is automatically generated from the filtered dataset."
    )

    st.markdown(summary)