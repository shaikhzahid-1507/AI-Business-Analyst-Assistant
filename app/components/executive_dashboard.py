import streamlit as st


def show_executive_dashboard(health):
    """
    Display executive business overview.
    """

    st.header("📈 Executive Overview")

    col1, col2 = st.columns([3, 2])

    with col1:

        st.metric(
            "Business Health Score",
            f"{health['score']}/100"
        )

        st.progress(
            health["score"] / 100
        )

    with col2:

        st.success(
            f"Overall Status\n\n{health['status']}"
        )