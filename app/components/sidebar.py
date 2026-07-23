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
        st.markdown("""
- 📤 Upload Dataset
- 🔍 Data Profiling
- 📊 Business Dashboard
- 🤖 AI Insights
- 📑 Executive Summary
- 💡 Recommendations
- ⚠️ Risk Assessment
- 🚀 Growth Opportunities
""")

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

        st.caption("""
Developed by Zahid Shaikh

🤖 AI Business Analyst Assistant

Version 1.0
""")