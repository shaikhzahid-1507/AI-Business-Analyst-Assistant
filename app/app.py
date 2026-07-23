import streamlit as st
st.subheader("📂 Dataset Overview")
from components.footer import show_footer
from utils.safe_render import safe_render
from components.ai_assistant import show_ai_assistant
from services.ai_decision import answer_business_question
from services.executive_alerts import generate_executive_alerts
from components.executive_alerts import show_executive_alerts
from services.business_health import calculate_business_health
from components.executive_dashboard import show_executive_dashboard
from components.export import show_export_center
from services.opportunity_detection import detect_business_opportunities
from components.opportunity_detection import show_business_opportunities
from services.risk_detection import detect_business_risk
from components.risk_detection import show_business_risk
from services.recommendations import generate_recommendations
from components.recommendations import show_recommendations
from services.executive_summary import generate_executive_summary
from components.executive_summary import show_executive_summary
from services.insights import generate_business_insights
from components.insights import show_business_insights

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Business Analyst Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Imports
# -----------------------------
from components.header import show_header
from components.sidebar import show_sidebar
from components.uploader import upload_file

from components.filter import show_filters
from services.filters import apply_business_filters

from services.data_loader import load_data

from services.profiler import (
    profile_data,
    missing_values_summary,
    data_type_summary,
    descriptive_statistics,
    categorical_summary,
    correlation_matrix,
    numeric_columns,
)

from components.profiler import (
    show_profile,
    show_missing_values,
    show_data_types,
    show_data_type_chart,
    show_descriptive_statistics,
    show_categorical_summary,
    show_correlation_heatmap,
    show_distribution,
    show_boxplot,
)

from services.dashboard import (
    business_kpis,
    churn_distribution,
    monthly_charges,
    contract_distribution,
    payment_distribution,
    tenure_distribution,
)

from components.dashboard import (
    show_business_kpis,
    show_churn_chart,
    show_monthly_charges,
    show_contract_chart,
    show_payment_chart,
    show_tenure_chart,
)


def main():

    # -----------------------------
    # Header
    # -----------------------------
    show_sidebar()
    show_header()

    uploaded_file = upload_file()

    if uploaded_file is None:

     st.info(
        "👆 Upload a CSV or Excel file to begin your business analysis."
    )

     return

    try:
        with st.spinner("🔄 Processing your dataset..."):

            # -----------------------------
            # Load Data
            # -----------------------------
            df = load_data(uploaded_file)
            # -----------------------------
            # Filters
            # -----------------------------
            filters = show_filters(df)

            filtered_df = apply_business_filters(df, filters)
            if filtered_df.empty:
             st.warning("📭 No records found for the selected filters.")
             st.info("Try changing your filters to see business insights.")
             return

            st.success("✅ Dataset processed successfully!")
            st.toast("Analysis completed successfully! 🎉")

        # -----------------------------
        # Executive Dataset Summary
        # -----------------------------
        st.subheader("📂 Dataset Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                label="📄 Rows",
                value=f"{filtered_df.shape[0]:,}"
            )

        with col2:
            st.metric(
                label="📊 Columns",
                value=filtered_df.shape[1]
            )

        with col3:
            st.metric(
                label="⚠ Missing Values",
                value=int(filtered_df.isnull().sum().sum())
            )

        with col4:
            memory = filtered_df.memory_usage(deep=True).sum() / (1024 * 1024)
            st.metric(
                label="💾 Memory",
                value=f"{memory:.2f} MB"
            )

       
    
        # -----------------------------
        # Dataset Preview
        # -----------------------------
        st.markdown("## 📋 Dataset Preview")
        st.caption("Review the uploaded dataset before performing analytics.")
        st.dataframe(filtered_df.head())

        # -----------------------------
        # Data Profiling
        # -----------------------------
        st.divider()
        st.markdown("## 🔍 Data Profiling")
        st.caption("Understand data quality, structure, distributions, and relationships.")
        profile = profile_data(filtered_df)
        missing_summary = missing_values_summary(filtered_df)
        dtype_summary = data_type_summary(filtered_df)
        stats = descriptive_statistics(filtered_df)
        categorical = categorical_summary(filtered_df)
        correlation = correlation_matrix(filtered_df)
        numeric_cols = numeric_columns(filtered_df)

        show_profile(profile)
        show_missing_values(missing_summary)
        show_data_types(dtype_summary)
        show_data_type_chart(dtype_summary)
        show_descriptive_statistics(stats)
        show_categorical_summary(categorical)
        show_correlation_heatmap(correlation)
        show_distribution(filtered_df, numeric_cols)
        show_boxplot(filtered_df, numeric_cols)

        # -----------------------------
        # Dashboard
        # -----------------------------
        
        st.divider()
        st.markdown("## 📊 Business Dashboard")
        st.caption("Key business metrics and customer analytics.")

        kpis = business_kpis(filtered_df)
        health = calculate_business_health(kpis)
        alerts = generate_executive_alerts(kpis)
        show_business_kpis(kpis)
        safe_render(show_executive_dashboard, health)
        safe_render(show_executive_alerts, alerts)

        summary = generate_executive_summary(filtered_df)

# Generate AI insights ONCE
        insights = generate_business_insights(filtered_df)

        recommendations = generate_recommendations(filtered_df)
        risk = detect_business_risk(filtered_df)
        opportunities = detect_business_opportunities(filtered_df)

        safe_render(
    show_export_center,
    filtered_df,
    kpis,
    summary,
    insights,
    recommendations,
    risk,
    opportunities,
)

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            churn_df = churn_distribution(filtered_df)
            safe_render(show_churn_chart, churn_df)

        with col2:
            contract_df = contract_distribution(filtered_df)
            safe_render(show_contract_chart, contract_df)

        col3, col4 = st.columns(2)

        with col3:
            charges = monthly_charges(filtered_df)
            safe_render(show_monthly_charges, charges)

        with col4:
            payment_df = payment_distribution(filtered_df)
            safe_render(show_payment_chart, payment_df)

        col5, col6 = st.columns(2)

        with col5:
            tenure = tenure_distribution(filtered_df)
            safe_render(show_tenure_chart, tenure)

        with col6:
            st.info("🚀 Revenue Analytics Coming Soon")
            
        # -----------------------------
        # AI Business Insights
        # -----------------------------
        st.divider()
        st.markdown("## 🤖 AI Business Insights")
        st.caption("AI-generated insights based on customer behaviour and business performance.")
        safe_render(show_business_insights, insights)

        # -----------------------------
        # Executive Business Summary
        # -----------------------------
        st.divider()
        st.markdown("## 📑 Executive Summary")
        st.caption("A concise overview of the most important business findings.")

        safe_render(show_executive_summary, summary)

        # -----------------------------
        # Smart Business Recommendations
        # -----------------------------
        st.divider()
        st.markdown("## 💡 Business Recommendations")
        st.caption("Suggested actions to improve customer retention and business growth.")

        safe_render(show_recommendations, recommendations)

        # -----------------------------
        # Business Risk Assessment
        # -----------------------------
        st.divider()
        st.markdown("## ⚠️ Risk Assessment")
        st.caption("Potential business risks detected from the uploaded data.")

        safe_render(show_business_risk, risk)

        # -----------------------------
        # Business Growth Opportunities
        # -----------------------------
        st.divider()
        st.markdown("## 🚀 Growth Opportunities")
        st.caption("AI-identified opportunities to improve business performance.")

        safe_render(show_business_opportunities, opportunities)
        question = show_ai_assistant()

        if question:
            answer = answer_business_question(
                question,
                filtered_df,
                kpis,
            )

            st.success(answer)
            show_footer()
    except Exception as e:
        st.error("❌ Unable to process the uploaded dataset.")
        with st.expander("View Technical Details"):
            st.exception(e)

if __name__ == "__main__":
    main()