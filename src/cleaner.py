"""
cleaner.py

Responsible for cleaning a pandas DataFrame.

This module Does Not:
- Read files
- Analyze data
- Create visualizations
- Generate reports
"""

import pandas as pd
import numpy as np

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert column names to a consistent format.
    """

    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


def replace_empty_strings(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert empty strings into NaN.
    """

    df.replace(r"^\s*$", np.nan, regex=True, inplace=True)

    return df


def remove_duplicates(df: pd.DataFrame):
    """
    Remove duplicate rows.
    Returns dataframe and number of removed rows.
    """

    before = len(df)

    df = df.drop_duplicates()

    removed = before - len(df)

    return df, removed


def remove_empty_rows(df: pd.DataFrame):
    """
    Remove rows where every value is missing.
    """

    before = len(df)

    df = df.dropna(how="all")

    removed = before - len(df)

    return df, removed


def cleaning_summary(
        original_rows: int,
        final_rows: int,
        duplicates_removed: int,
        empty_rows_removed: int,
):
    """
    Return a dictionary summmarizing the cleaning process.
    """
    return {
        "original_rows": original_rows,
        "final_rows": final_rows,
        "duplicates_removed": duplicates_removed,
        "empty_rows_removed": empty_rows_removed
    }


def clean_dataframe(df: pd.DataFrame):
    """
    Execute the complete cleaning pipeline.
    """

    original_rows = len(df)

    df = standardize_column_names(df)
    df = replace_empty_strings(df)

    df, duplicates_removed = remove_duplicates(df)
    df, empty_rows_removed = remove_empty_rows(df)

    summary = cleaning_summary(
        original_rows,
        len(df),
        duplicates_removed,
        empty_rows_removed,
    )

    return df, summary