import streamlit as st


def show_business_insights(insights):
    """
    Display AI-generated business insights.
    """

    st.divider()
    st.header("🤖 AI Business Insights")

    st.info(
        "These insights are automatically generated based on the filtered dataset."
    )

    for insight in insights:
        st.markdown(f"- {insight}")