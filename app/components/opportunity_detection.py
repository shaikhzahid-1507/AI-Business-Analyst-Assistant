import streamlit as st


def show_business_opportunities(opportunities):
    """
    Display business growth opportunities.
    """

    st.success(
        "The following opportunities have been identified from the filtered dataset."
    )

    for opportunity in opportunities:
        st.markdown(f"- {opportunity}")