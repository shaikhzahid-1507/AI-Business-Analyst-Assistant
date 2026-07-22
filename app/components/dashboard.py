import streamlit as st
import plotly.express as px

def show_business_kpis(kpis):
    """
    Display business KPI cards.
    """
    
    st.divider()
    st.header("📊 Business Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👥 Customers",
            f"{kpis['total_customers']:,}"
        )

    with col2:
        st.metric(
            "💰 Avg Monthly",
            f"${kpis['average_monthly']}"
        )

    with col3:
        st.metric(
            "📅 Avg Tenure",
            f"{kpis['average_tenure']} Months"
        )

    with col4:
        st.metric(
            "📈 Churn Rate",
            f"{kpis['churn_rate']}%"
        )


def show_churn_chart(churn_df):
    """
    Display churn breakdown chart.
    """

    st.subheader("📉 Churn Distribution")

    # Accept either a Series (labels) or a DataFrame with label/count columns
    try:
        # If passed a Series, get value counts
        if hasattr(churn_df, "value_counts") and not hasattr(churn_df, "columns"):
            counts = churn_df.value_counts()
            fig = px.pie(values=counts.values, names=counts.index, title="Churn Distribution")
        else:
            # If DataFrame, try common column names
            if "churn" in churn_df.columns:
                counts = churn_df["churn"].value_counts()
                fig = px.pie(values=counts.values, names=counts.index, title="Churn Distribution")
            else:
                # Fallback: try first two columns as labels/values
                cols = list(churn_df.columns)
                fig = px.pie(churn_df, names=cols[0], values=cols[1], title="Churn Distribution")
    except Exception:
        # As a last resort, show empty message
        st.info("No churn data available to display.")
        return

    st.plotly_chart(fig, use_container_width=True)

def show_monthly_charges(charges):
    """
    Display Monthly Charges histogram.
    """

    st.subheader("💰 Monthly Charges Distribution")

    fig = px.histogram(
        x=charges,
        nbins=30,
        title="Monthly Charges",
    )

    fig.update_layout(
        xaxis_title="Monthly Charges",
        yaxis_title="Customers",
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_payment_chart(payment_df):
    """
    Display Payment Method Distribution.
    """

    st.subheader("💳 Payment Method Distribution")

    fig = px.pie(
        payment_df,
        names="Payment Method",
        values="Customers",
        hole=0.45,
        title="Customers by Payment Method"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_tenure_chart(tenure):
    """
    Display Tenure Distribution.
    """

    st.subheader("📅 Customer Tenure Distribution")

    fig = px.histogram(
        x=tenure,
        nbins=30,
        title="Customer Tenure"
    )

    fig.update_layout(
        xaxis_title="Tenure (Months)",
        yaxis_title="Customers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_contract_chart(contract_df):
    """
    Display Contract Type Distribution.
    """

    st.subheader("📄 Contract Type Distribution")

    fig = px.bar(
        contract_df,
        x="Contract",
        y="Customers",
        text="Customers",
        color="Contract",
        title="Customers by Contract Type"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Contract Type",
        yaxis_title="Customers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )