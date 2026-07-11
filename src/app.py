import streamlit as st

st.set_page_config(
    page_title="ResearchViz",
    page_icon=":bar_chart:",
    layout="centered"
)

st.title("ResearchViz")

st.subheader("Automatic CSV cleaning & visualization Tool for Researchers")

st.write(
    """
    Upload your csv dataset and let ResearchViz automatically:
    - Clean your dataset
    - Analyze your data
    - Generate visualizations
    - Create a professional PDF report"""
)

uploaded_file = st.file_uploader("Choose a csv file", type="csv")

