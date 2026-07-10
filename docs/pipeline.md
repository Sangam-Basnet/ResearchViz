# **ResearchViz Processing Pipeline** 

## **Stage 1 - File upload:**

### Purpose
To accept a csv file from the researcher

### Input: 
CSV file selected by the user

### Output:
validated file ready for processing 

### Possible failures:
- wrong file type
- Empty file
- Corrupted csv
- too large filesize

### Responsible module:
file_handler.py


## **Stage 2 - Load and Validate Dataset**

## Purpose
Read the uploaded CSV file into memory and verify that it is suitable for further processing.

## Why
Before cleaning or analyzing the dataset, the application must ensure that the uploaded file is a valid and readable CSV. This prevents errors later in the pipeline and guarantees that subsequent modules receive a valid Pandas DataFrame.

## Input
CSV file uploaded by the user.

## Output
Validated Pandas DataFrame ready for data cleaning.

## Validation Operations
- Verify the uploaded file is a CSV.
- Read the CSV into a Pandas DataFrame.
- Detect and handle file encoding.
- Verify the delimiter is valid.
- Ensure the dataset is not empty.
- Ensure column headers exist.
- Check for duplicate column names.
- Verify the dataset can be parsed successfully.

## Possible Failures
- Unsupported file type.
- Corrupted CSV file.
- Encoding errors (e.g., UTF-16 instead of UTF-8).
- Incorrect delimiter.
- Missing or malformed headers.
- Empty dataset.
- Duplicate column names.
- File cannot be parsed.

## Responsible Module
file_handler.py


## **Stage 3 - Clean Dataset:**

### Purpose:
To prepare the dataset for analysis by removing common quality issues.

### why:
Raw datasets often contain duplicate records, inconsistent column names, empty rows, and missing values. Cleaning improves data quality and reduces errors during analysis.

### Input:
Validates Pandas DataFrame.

### Output:
Cleaned Pandas DataFrame.

### Cleaning Operations:
- Remove duplicate rows
- Remove completely empty rows and columns
- Standardize column names
- Detect missing values
- Generate cleaning summary

### Possible failures:
- Memory limitations on very large datasets
- Unsupported data types
- Unsupported formatting issues

### Responsible Module
cleaner.py


## **Stage 4 - Analyze Dataset**

### Purpose
EXtract useful statistical information from the cleaned dataset.

### why:
Researchers need a quick understanding of their data before performing deeper analysis.

### Input:
Cleaned Pandas DataFrame.

### Output:
Statistical summary and analysis resuts.

### Analysis Operation:
- Number of rows and columns
- Data Types
- Missing value summary
- Descriptive statistics
- correlation analysis
- Numeric and categorical column detection

### Possible Failures
- Dataset contains no analyzable columns
- Numerical calculations fail because of invalid values.

### Responsible Module
analyzer.py


## **Stage 5 - Generate Visualization**

### Purpose:
Create graphical representation of the analyzed dataset.

### Why:
Visualizations help researchers identify trends, relationships, distractions, and anomalies much faster than raw tables.

### Input:
cleaned DataFrame and analysis results.

### Output:
Charts saved for report generation.

### Generated Visualizations:
- Histogram
- Box Plot
- Correlation Heatmap
- Missing Value Chart
- Bar Charts
- Scatter Plot (when applicable)

### Possible Failures
- No numeric columns available
- Insufficient data for a specific chart
- Figure generation errors

### REsponsible Module
visualizer.py


## **Stage 6 - Generate PDF Report**

### Purpose
Combine all analysis results and visualizations into a professional report.

### Why:
Researchers should recieve a single document that sumarizes the dataset instead of multiple separate files.

### Input:
Analysis results and generated visualizations.

### Output:
visual_report.pdf

### Report Contents
- Dataset overview
- Cleaning summary
- visualizations
- Key observations

### Possible Failures
- PDF generation failure
- Missing visulaization files
- Report formattinfg errors

### REsponsible Module
report_generator.py


## **Stage 7 - Export Cleaned Dataset**

### Purpose
Save the cleaned dataset as a downloadable csv file.

### Why:
Researchers may want to continue their work using the cleaned data in other tools.

### Input:
Cleaned Pandas DataFrame.

### Output:
cleaned_dataset.csv

### Possible Failures:
- File writing permission denied
- Disk Storage unavailable
- Invalid output location

### Responsible Module:
file_handler.py


## **Stage 8 - Download Results**

### Purpose:
Allow the researcher to download the generated files.

### Why:
The final objective of the application is to deliver the cleaned dataset and visual report to the user.

### Input:
Generated output files.

### Output:
Download files:
- cleaned_dataset.csv
- visual_report.pdf

### Possible Failures 
- Download interruption 
- Missing output files
- File corruption

### Responsible Module
app.py
