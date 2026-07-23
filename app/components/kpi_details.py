import streamlit as st


def show_kpi_details(title, value, description):
    """
    Display detailed KPI information.
    """

    with st.expander(f"📊 {title}", expanded=False):

        st.metric(
            label=title,
            value=value,
        )

        st.info(description)