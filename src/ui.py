import streamlit as st

def render_page():
    st.set_page_config(
        page_titlle="ResearchViz",
        page_icon=":bar_char:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    st.title("ResearchViz")

    st.caption(
        "Ai-Powered Research Dataset Processing Asssistant"
        )
    