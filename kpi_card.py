import streamlit as st


def show_kpi_card(title, value, icon):
    """
    Display a modern KPI card.
    """

    st.markdown(
        f"""
        <div style="
            background:white;
            padding:20px;
            border-radius:15px;
            border:1px solid #E2E8F0;
            box-shadow:0 4px 12px rgba(0,0,0,0.08);
            text-align:center;
            margin-bottom:15px;
        ">
            <div style="font-size:32px;">{icon}</div>
            <div style="
                font-size:16px;
                color:#64748B;
                font-weight:600;
                margin-top:8px;
            ">
                {title}
            </div>

            <div style="
                font-size:34px;
                font-weight:bold;
                color:#1E293B;
                margin-top:10px;
            ">
                {value}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )