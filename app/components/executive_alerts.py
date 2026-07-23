import streamlit as st


def show_executive_alerts(alerts):
    """
    Display executive alerts.
    """

    st.header("🚨 Executive Alerts")

    for alert in alerts:

        if alert["level"] == "success":
            st.success(
                f"**{alert['title']}**\n\n{alert['message']}"
            )

        elif alert["level"] == "warning":
            st.warning(
                f"**{alert['title']}**\n\n{alert['message']}"
            )

        else:
            st.error(
                f"**{alert['title']}**\n\n{alert['message']}"
            )