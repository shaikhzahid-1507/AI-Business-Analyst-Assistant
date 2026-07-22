import streamlit as st
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
from services.filter import apply_filters

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
        return

    try:
        # -----------------------------
        # Load Data
        # -----------------------------
        df = load_data(uploaded_file)

        # -----------------------------
        # Filters
        # -----------------------------
        filters = show_filters(df)
        filtered_df = apply_filters(df, filters)

        st.success("✅ File uploaded successfully!")

        # -----------------------------
        # Dataset Preview
        # -----------------------------
        st.subheader("Dataset Preview")
        st.dataframe(filtered_df.head())

        # -----------------------------
        # Data Profiling
        # -----------------------------
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

        kpis = business_kpis(filtered_df)
        show_business_kpis(kpis)

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            churn_df = churn_distribution(filtered_df)
            show_churn_chart(churn_df)

        with col2:
            contract_df = contract_distribution(filtered_df)
            show_contract_chart(contract_df)

        col3, col4 = st.columns(2)

        with col3:
            charges = monthly_charges(filtered_df)
            show_monthly_charges(charges)

        with col4:
            payment_df = payment_distribution(filtered_df)
            show_payment_chart(payment_df)

        col5, col6 = st.columns(2)

        with col5:
            tenure = tenure_distribution(filtered_df)
            show_tenure_chart(tenure)

        with col6:
            st.info("🚀 Revenue Analytics Coming Soon")

        # -----------------------------
        # AI Business Insights
        # -----------------------------
        insights = generate_business_insights(filtered_df)
        show_business_insights(insights)

        # -----------------------------
        # Executive Business Summary
        # -----------------------------
        summary = generate_executive_summary(filtered_df)
        show_executive_summary(summary)

        # -----------------------------
        # Smart Business Recommendations
        # -----------------------------
        recommendations = generate_recommendations(filtered_df)
        show_recommendations(recommendations)

        # -----------------------------
        # Business Risk Assessment
        # -----------------------------
        risk = detect_business_risk(filtered_df)
        show_business_risk(risk)

        # -----------------------------
        # Business Growth Opportunities
        # -----------------------------
        opportunities = detect_business_opportunities(filtered_df)
        show_business_opportunities(opportunities)
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")

if __name__ == "__main__":
    main()