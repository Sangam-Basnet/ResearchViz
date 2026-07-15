from pathlib import Path
import traceback
import streamlit as st
import pandas as pd

from file_handler import load_csv
from cleaner import clean_dataframe
from analyzer import analyze_dataframe
from visualizer import generate_visualizations


# -----------------------------
# Load Custom CSS
# -----------------------------
def load_css():
    css_path = Path(__file__).parent.parent / "assets" / "styles.css"

    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as css:
            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True,
            )


# -----------------------------
# Hero Section
# -----------------------------
def hero_section():

    st.markdown(
        """
        <h1 style='text-align:center;color:#2563EB;font-size:70px;'>
        📊 ResearchViz
        </h1>

        <h3 style='text-align:center;color:gray;'>
        AI-Powered Research Dataset Processing Assistant
        </h3>

        <p style='text-align:center;font-size:20px;color:#666;'>
        Transform raw CSV datasets into clean, analyzed and publication-ready outputs.
        </p>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# Left Card
# -----------------------------
def cleaning_card():

    st.markdown(
        """
<div class="feature-card">

<h3>🧹 Data Cleaning</h3>

<ul>

<li>Remove duplicate records</li>

<li>Handle missing values</li>

<li>Standardize column names</li>

<li>Detect formatting issues</li>

<li>Prepare research dataset</li>

</ul>

</div>
""",
        unsafe_allow_html=True,
    )


# -----------------------------
# Right Card
# -----------------------------
def analysis_card():

    st.markdown(
        """
<div class="feature-card">

<h3>📊 Analysis & Reports</h3>

<ul>

<li>Descriptive Statistics</li>

<li>Correlation Analysis</li>

<li>Automatic Charts</li>

<li>Research Report</li>

<li>Clean CSV Export</li>

</ul>

</div>
""",
        unsafe_allow_html=True,
    )


# -----------------------------
# Upload Section
# -----------------------------
def upload_card():

    st.markdown(
        """
<div class="upload-card">

<h2>Upload Dataset</h2>

<p>
Drag & Drop your CSV file here
</p>

<p>
or
</p>

<p>
Browse from your computer
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"],
        label_visibility="collapsed",
    )

    return uploaded_file


# -----------------------------
# About
# -----------------------------
def about_section():

    st.markdown(
        """
<div class="about-card">

<h2>What does ResearchViz do?</h2>

<p>

ResearchViz eliminates repetitive data preparation work for researchers.

Simply upload a raw CSV dataset and ResearchViz automatically cleans,
analyzes and visualizes your dataset while preparing publication-ready
outputs.

Everything runs locally on your computer.

No cloud.

No external server.

No privacy concerns.

</p>

</div>
""",
        unsafe_allow_html=True,
    )


# -----------------------------
# Status
# -----------------------------
def status_section(uploaded_file):

    st.markdown("## ⚡ Current Status")

    if uploaded_file is None:

        st.info("Waiting for dataset upload...")

    else:

        st.success(f"Dataset '{uploaded_file.name}' uploaded successfully.")


# -----------------------------
# Footer
# -----------------------------
def footer():

    st.markdown(
        """
<div class="footer">

Privacy First • Desktop Optimized • Local Processing • No Data Leaves Your Computer

</div>
""",
        unsafe_allow_html=True,
    )


# -----------------------------
# Main Page
# -----------------------------
def render_page():

    st.set_page_config(
        page_title="ResearchViz",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    load_css()

    hero_section()

    st.write("")

    left, center, right = st.columns([1.2, 1.8, 1.2])

    with left:
        cleaning_card()

    with center:
        uploaded_file = upload_card()

    with right:
        analysis_card()

    st.write("")
    st.write("")

    about_section()

    st.write("")
    st.write("")

    status_section(uploaded_file)
    if uploaded_file is not None:

        try:

            # Read CSV
            df = load_csv(uploaded_file)

            # Clean Dataset
            clean_df, cleaning_summary = clean_dataframe(df)

            # Analyze Dataset
            analysis = analyze_dataframe(clean_df)

            # visualize dataset
            figures = generate_visualizations(clean_df)

            st.success("Dataset processed successfully!")

            st.subheader("Dataset Overview")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Rows",
                analysis["shape"]["rows"],
            )

            col2.metric(
                "Columns",
                analysis["shape"]["columns"],
            )

            col3.metric(
                "Memory (MB)",
                analysis["memory_usage_MB"],
            )

            st.subheader("Cleaning Summary")
            st.json(cleaning_summary)

            st.subheader("Missing Values")
            st.json(analysis["missing_values"])

            st.subheader("Data Types")
            st.json(analysis["data_types"])

            # ---------------
            # visualizations
            # ----------------
            st.subheader("Visualizations")

            for title, figure in figures.items():

                if figure is not None:

                    st.markdown(f"### {title}")

                    st.pyplot(figure)
                
                else:
                    st.info(f"{title}: Not available for this dataset.")

        except Exception:
            st.code(traceback.format_exc())

    st.write("")
    st.write("")

    footer()
