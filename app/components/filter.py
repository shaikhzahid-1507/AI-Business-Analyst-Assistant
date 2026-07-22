import streamlit as st


def show_filters(df):
    """
    Display sidebar filters.
    """

    st.sidebar.header("🎛️ Dashboard Filters")

    gender = st.sidebar.multiselect(
        "Gender",
        sorted(df["gender"].dropna().unique())
    )

    contract = st.sidebar.multiselect(
        "Contract",
        sorted(df["Contract"].dropna().unique())
    )

    payment = st.sidebar.multiselect(
        "Payment Method",
        sorted(df["PaymentMethod"].dropna().unique())
    )

    internet = st.sidebar.multiselect(
        "Internet Service",
        sorted(df["InternetService"].dropna().unique())
    )

    churn = st.sidebar.multiselect(
        "Churn",
        sorted(df["Churn"].dropna().unique())
    )

    return {
        "gender": gender,
        "contract": contract,
        "payment": payment,
        "internet": internet,
        "churn": churn,
    }