import streamlit as st

from reports.business_report import generate_business_report
from reports.ai_insights import generate_ai_insights_pdf
from reports.executive_summary import generate_executive_summary_pdf
from services.export import dataframe_to_csv


def show_export_center(
    df,
    kpis,
    summary,
    insights,
    recommendations,
    risk,
    opportunities,
):
    """
    Display Export Center.
    """

    st.divider()

    st.markdown("## 📥 Export Center")
    st.caption("Download reports and share your business analysis.")

    # ---------------------------------------
    # Export Filtered Dataset
    # ---------------------------------------
    csv = dataframe_to_csv(df)

    st.download_button(
        label="📊 Download Filtered Dataset (CSV)",
        data=csv,
        file_name="filtered_dataset.csv",
        mime="text/csv",
        use_container_width=True,
        key="download_csv",
    )

    # ---------------------------------------
    # Executive Summary PDF
    # ---------------------------------------
    pdf = generate_executive_summary_pdf(
        kpis,
        summary,
    )

    st.download_button(
        label="📄 Download Executive Summary (PDF)",
        data=pdf,
        file_name="Executive_Summary_Report.pdf",
        mime="application/pdf",
        use_container_width=True,
        key="download_summary_pdf",
    )

    # ---------------------------------------
    # AI Insights PDF
    # ---------------------------------------
    ai_pdf = generate_ai_insights_pdf(insights)

    st.download_button(
        label="🤖 Download AI Insights (PDF)",
        data=ai_pdf,
        file_name="AI_Insights_Report.pdf",
        mime="application/pdf",
        use_container_width=True,
        key="download_ai_pdf",
    )

    # ---------------------------------------
    # Complete Business Report
    # ---------------------------------------
    business_pdf = generate_business_report(
        kpis,
        summary,
        insights,
        recommendations,
        risk,
        opportunities,
    )

    st.download_button(
        label="📈 Download Complete Business Report (PDF)",
        data=business_pdf,
        file_name="Business_Analysis_Report.pdf",
        mime="application/pdf",
        use_container_width=True,
        key="download_business_report_pdf",
    )