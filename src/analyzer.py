"""
analyzer.py

Responsible for analyzing a cleaned pandas DataFrame.

This module does not:
- Read files
- Clean data
- Create visulaizations
- Generate reports
"""

import pandas as pd

def dataset_shape(df: pd.DataFrame) -> dict:
    """ Return number of rows and columns."""
    return{
        "rows": df.shape[0],
        "columns": df.shape[1],
    }


# def memory_usage(df: pd.DataFrame) -> float:
#     """ Return memory usage in MB."""
#     memory = df.memory_usage(deep=True).sum()
#     return round(memory / (1024**1024), 2)

def memory_usage(df: pd.DataFrame) -> float:
    """Return memory usage in MB."""

    print("========== MEMORY DEBUG ==========")
    print("TYPE:", type(df))
    print("SHAPE:", df.shape)

    memory = df.memory_usage(index=True, deep=True)

    print(memory)

    total = int(memory.sum())

    print("TOTAL:", total)

    return round(total / (1024 * 1024), 2)


def column_names(df: pd.DataFrame) -> list:
    """ Return all column names."""
    return list(df.columns)


def data_types(df: pd.DataFrame) -> dict:
    """ Return data type of each column."""
    return df.dtypes.astype(str).to_dict()


def missing_values(df: pd.DataFrame) -> dict:
    """ Return missing values per column."""
    return df.isnull().sum().to_dict()


def duplicate_rows(df: pd.DataFrame) -> int:
    """ Return number of duplicate rows."""
    return int(df.duplicated().sum())


def numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    """ Return summary statistics for numeric columns."""
    return df.describe().T


def categorical_summary(df: pd.DataFrame):
    """Return summary statistics for categorical columns."""

    categorical = df.select_dtypes(include=["object", "category"])

    if categorical.empty:
        return None

    return categorical.describe().T


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """ Return correlation matrix """
    numeric = df.select_dtypes(include = "number")
    
    if numeric.shape[1] < 2:
        return None
    
    return numeric.corr()


def analyze_dataframe(df: pd.DataFrame) -> dict:
    """Execute complete analysis pipeline."""

    corr = correlation_matrix(df)
    cat = categorical_summary(df)

    return {
        "shape": dataset_shape(df),
        "memory_usage_MB": memory_usage(df),
        "column_names": column_names(df),
        "data_types": data_types(df),
        "missing_values": missing_values(df),
        "duplicate_rows": duplicate_rows(df),
        "numeric_summary": numeric_summary(df).to_dict(),
        "categorical_summary": (
        cat.to_dict() if cat is not None else None
        ),
        "correlation_matrix": (
            corr.to_dict() if corr is not None else None
        ),
    }