import streamlit as st


def show_sidebar():
    """
    Displays the professional application sidebar.
    """

    with st.sidebar:

        # ---------------------------------
        # Logo / Branding
        # ---------------------------------
        st.markdown(
            """
            # 🤖 AI Business Analyst
            ### Enterprise Dashboard
            """,
        )

        st.markdown("---")

        # ---------------------------------
        # Navigation
        # ---------------------------------
        st.subheader("🧭 Navigation")
        st.write("📤 Upload Dataset")
        st.write("🔍 Data Profiling")
        st.write("📊 Business Dashboard")
        st.write("🤖 AI Insights")
        st.write("📑 Executive Summary")
        st.write("💡 Recommendations")
        st.write("⚠️ Risk Assessment")
        st.write("🚀 Growth Opportunities")

        st.info(
    "Upload a dataset and use the filters below to explore your business data."
)

        st.markdown("---")

        # ---------------------------------
        # Dataset Filters
        # ---------------------------------
        

        # ---------------------------------
        # Footer
        # ---------------------------------
        st.markdown("---")

        st.markdown("---")

st.caption(
"""
👨‍💻 Developed by Zahid Shaikh

🤖 AI Business Analyst Assistant

© 2026 | Version 1.0
"""
)