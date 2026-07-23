import streamlit as st


def show_header():
    """
    Displays a professional application header.
    """

    st.markdown("""
    <div style="
        background: linear-gradient(90deg, #1f77b4, #4f46e5);
        padding: 25px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
    ">
        <h1 style="margin-bottom:5px;">
            🤖 AI Business Analyst Assistant
        </h1>
        <h4 style="margin-top:0px;font-weight:400;">
            Enterprise Customer Analytics Dashboard
        </h4>
        <p style="font-size:16px;margin-top:15px;">
            Analyze customer data, discover business insights, detect risks,
            identify growth opportunities, and generate AI-powered recommendations.
        </p>
    </div>
    """, unsafe_allow_html=True)