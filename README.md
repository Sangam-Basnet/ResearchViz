# ResearchViz

ResearchViz is a Python-based desktop application for processing research datasets. It automates the workflow of cleaning, analyzing, visualizing, and generating professional PDF reports from CSV datasets through an interactive Streamlit interface.

---

## Features

- CSV dataset validation and loading
- Automatic data cleaning
- Dataset statistics and summary generation
- Missing value analysis
- Duplicate detection
- Data type analysis
- Correlation matrix generation
- Automatic visualization generation
- Professional PDF report generation
- Interactive Streamlit interface

---

## Technology Stack

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- ReportLab

---

## Project Structure

```text
ResearchViz/
│
├── assets/
│   └── styles.css
│
├── src/
│   ├── app.py
│   ├── ui.py
│   ├── file_handler.py
│   ├── cleaner.py
│   ├── analyzer.py
│   ├── visualizer.py
│   ├── report_generator.py
│   └── pdf_generator.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Processing Pipeline

```text
CSV Dataset
      │
      ▼
File Validation
      │
      ▼
Data Cleaning
      │
      ▼
Dataset Analysis
      │
      ▼
Visualization Generation
      │
      ▼
PDF Report Generation
      │
      ▼
Download Report
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/ResearchViz.git
```

Move into the project directory.

```bash
cd ResearchViz
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
streamlit run src/app.py
```

---

## Live Demo

Streamlit Community Cloud

> Add deployment URL here after deployment.

---

## Running Locally

The Streamlit deployment is intended for demonstration purposes.

For sensitive or confidential datasets, it is recommended to run the application locally.

---

## Output

ResearchViz generates:

- Cleaned dataset
- Dataset analysis
- Statistical summaries
- Visualizations
- Professional PDF report

---

## Future Enhancements

- Excel (.xlsx) support
- Interactive visualizations
- Additional statistical tests
- Multiple report templates
- Export to Word and HTML

---

## License

This project is licensed under the MIT License.

---

## Author

**Sangam Basnet**
