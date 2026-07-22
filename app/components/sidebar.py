import streamlit as st


def show_sidebar():
    """
    Displays the application sidebar.
    """

    with st.sidebar:

        st.header("📂 Navigation")

        st.markdown("### Current Module")

        st.success("✅ Data Upload")

        st.write("⏳ Data Profiling")
        st.write("⏳ Dashboard")
        st.write("⏳ AI Insights")

        st.divider()

        st.caption("Version 1.0")