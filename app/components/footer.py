import streamlit as st


def show_footer():
    st.divider()

    st.markdown(
        """
        <div style='text-align:center; color:gray; padding:15px;'>
            <b>AI Business Analyst Assistant</b><br>
            Built with ❤️ using Python, Streamlit, Pandas & Plotly<br><br>
            © 2026 Zahid Shaikh
        </div>
        """,
        unsafe_allow_html=True,
    )