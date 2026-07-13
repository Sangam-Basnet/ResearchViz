"""
file_handler.py

Responsible for:
1. Validating uploaded files
2. Detecting CSV delimeter
3. Reading CSV safely
4. Validating the loaded DataFrame

This module does not clean or analyze data.
"""

from io import StringIO
import csv
import pandas as pd

ALLOWED_EXTENSIONS = {".csv"}

def validate_extension(filename: str) -> bool:
    """
    Check whether the uploaded file has a suppported extension.
    """

    filename = filename.lower()

    return any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS)


def detect_delimeter(sample: str) -> str:
    """
    Detect the delimeter used in a csv file.
    """

    try: 
        dialect = csv.Sniffer().sniff(sample)
        return dialect.delimeter
    
    except csv.Error:
        return ","
    

def validate_dataframe(df: pd.DataFrame) -> None:
    """
    Validate the loaded DataFrame.
    Raises ValueError if validation fails.
    """

    if df.empty:
        raise ValueError("Dataset is empty.")
    
    if df.columns.empty:
        raise ValueError("No column headers found.")
    
    if len(df.columns) == 0:
        raise ValueError("Dataset contains zero columns.")
    

def load_csv(uploaded_file) -> pd.DataFrame:
    """
    Reads an uploaded csv file and returns a pandas DataFrame.
    
    Parameters
    ----------
    uploaded_file : Streamlit UploadedFile
    
    Returns
    -------
    pandas.DataFrame
    """

    if uploaded_file is None:
        raise ValueError("No file uploaded.")
    
    if  not validate_extension(uploaded_file.name):
        raise ValueError("Only CSV files are supported.")
    
    try:

        file_bytes = uploaded_file.getvalue()
        text = file_bytes.decode("utf-8")

    except UnicodeDecodeError:

        try:

            text = file_bytes.decode("latin-1")

        except Exception as e:
            raise ValueError("Unable to decode the uploaded file.") from e
        
    sample = text[:2048]

    delimeter = detect_delimeter(sample)

    try:

        df = pd.read_csv(
            StringIO(text),
            delimeter=delimeter,
        )

    except Exception as e:

        raise ValueError(f"Unable to read csv file: {e}") from e
    
    validate_dataframe(df)

    return df

    

