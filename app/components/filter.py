import streamlit as st


def show_filters(df):
    """
    Display enterprise business filters.
    """

    st.sidebar.header("🎛️ Business Filters")

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

    senior = st.sidebar.multiselect(
        "Senior Citizen",
        sorted(df["SeniorCitizen"].dropna().unique())
    )

    partner = st.sidebar.multiselect(
        "Partner",
        sorted(df["Partner"].dropna().unique())
    )

    dependents = st.sidebar.multiselect(
        "Dependents",
        sorted(df["Dependents"].dropna().unique())
    )

    tenure_range = st.sidebar.slider(
        "Tenure (Months)",
        int(df["tenure"].min()),
        int(df["tenure"].max()),
        (
            int(df["tenure"].min()),
            int(df["tenure"].max())
        )
    )

    monthly_range = st.sidebar.slider(
        "Monthly Charges ($)",
        float(df["MonthlyCharges"].min()),
        float(df["MonthlyCharges"].max()),
        (
            float(df["MonthlyCharges"].min()),
            float(df["MonthlyCharges"].max())
        )
    )

    return {
        "gender": gender,
        "contract": contract,
        "payment": payment,
        "internet": internet,
        "churn": churn,
        "senior": senior,
        "partner": partner,
        "dependents": dependents,
        "tenure": tenure_range,
        "monthly": monthly_range,
    }