import streamlit as st


def show_business_risk(risk):
    """
    Display the overall business risk level.
    """

    st.divider()
    st.header("⚠️ Business Risk Assessment")

    level = risk["level"]
    icon = risk["icon"]
    message = risk["message"]

    if level == "High":
        st.error(f"{icon} **{level} Risk**\n\n{message}")

    elif level == "Medium":
        st.warning(f"{icon} **{level} Risk**\n\n{message}")

    else:
        st.success(f"{icon} **{level} Risk**\n\n{message}")