import streamlit as st


def safe_render(render_function, *args, **kwargs):
    """
    Safely render any component without crashing the app.
    """
    try:
        render_function(*args, **kwargs)

    except Exception as e:
        st.error(f"⚠ Unable to render component: {render_function.__name__}")

        with st.expander("Technical Details"):
            st.exception(e)