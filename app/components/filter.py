import streamlit as st


def show_filters(df):
    """
    Display professional dashboard filters.
    """

    with st.sidebar:
     with st.expander("🎯 Dataset Filters", expanded=True):

        st.subheader("🎯 Dataset Filters")
        st.caption("Filter the dataset to perform focused business analysis.")

        st.markdown("### 👤 Customer")

        gender = st.multiselect(
            "Gender",
            sorted(df["gender"].dropna().unique()),
            placeholder="Select Gender"
        )

        churn = st.multiselect(
            "Churn Status",
            sorted(df["Churn"].dropna().unique()),
            placeholder="Select Churn Status"
        )

        st.markdown("---")

        st.markdown("### 📄 Contract")

        contract = st.multiselect(
            "Contract Type",
            sorted(df["Contract"].dropna().unique()),
            placeholder="Select Contract"
        )

        payment = st.multiselect(
            "Payment Method",
            sorted(df["PaymentMethod"].dropna().unique()),
            placeholder="Select Payment Method"
        )

        internet = st.multiselect(
            "Internet Service",
            sorted(df["InternetService"].dropna().unique()),
            placeholder="Select Internet Service"
        )

    return {
        "gender": gender,
        "contract": contract,
        "payment": payment,
        "internet": internet,
        "churn": churn,
    }