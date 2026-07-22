import streamlit as st


def show_recommendations(recommendations):
    """
    Display actionable business recommendations.
    """

    st.divider()
    st.header("💡 Smart Business Recommendations")

    st.success(
        "These recommendations are automatically generated from the filtered dataset."
    )

    for recommendation in recommendations:
        st.markdown(f"- {recommendation}")