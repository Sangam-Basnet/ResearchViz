"""
Visualizer.py

Responsible for creating visualizations from a cleaned DataFrame.

This module does not:
- Read files
- clean data
- analyze data
- generate reports
"""

import pandas as pd
import matplotlib.pyplot as plt

def create_missing_values_chart(df: pd.DataFrame):
    """
    Create a bar chart showing missing values
    in every column
    """

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if missing.empty:
        return None
    
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(
        missing.index,
        missing.values,
    )

    ax.set_title("Missing Values by columns")
    ax.set_xlabel("Columns")
    ax.set_ylabel("Missing Values")

    plt.xticks(rotation=45)

    plt.tight_layout()

    return fig


def create_correlation_heatmap(df: pd.DataFrame):
    """
    Create a correlation heatmap
    for numeric columns.
    """

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        return None
    
    corr = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(8, 6))

    image = ax.imshow(
        corr,
        aspect="auto",
    )

    plt.colorbar(
        image,
        ax=ax,
    )

    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(
        corr.columns,
        rotation=45,
        ha="right",
    )

    ax.set_yticks(range(len(corr.columns)))
    ax.set_yticklabels(corr.columns)

    ax.set_title("Correlation Heatmap")

    plt.tight_layout()

    return fig


def create_histograms(df: pd.DataFrame):
    """
    Create histogram(s) for all numeric columns.
    """

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        return None
    
    num_cols = len(numeric_df.columns)

    fig, axes = plt.subplots(
        num_cols,
        1,
        figsize=(8, 4 * num-cols),
    )

    if num_cols == 1:
        axes = [axes]

    for ax, column in zip(
        ax,
        numeric_df.columns,
    ):
        ax.hist(
            numeric_df[column],
            bins = 20,
        )

        ax.set_title(
            f"{column} Distribution"
        )

        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")

    plt.tight_layout()

    return fig

def create_boxplots(df: pd.DataFrame):
    """
    Create boxplots for all numeric columns.
    """

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        return None
    
    fig, ax = plt.subplots(
        figsize=(10, 6),
    )

    ax.boxplot(
        numeric_df.values,
        tick_labels=numeric_df.columns,
    )

    plt.xticks(
        rotation=45,
        ha="right",
    )

    ax.set_title(
        "Boxplots of Numeric columns"
    )

    ax.set_ylabel("values")

    plt.tight_layout()

    return fig


def create_barcharts(df: pd.DataFrame):
    """
    Create bar charts for categorical columns.
    """

    categorical_df = df.select_dtypes(
        include=["object", "category"]
    )

    if categorical_df.empty:
        return None
    
    num_cols = len(categorical_df.columns)

    fig, axes = plt.subplots(
        num_cols,
        1,
        figsize=(8, 4*num_cols),
    )

    if num_cols == 1:
        axes = [axes]

    for ax, column in zip(
        axes,
        categorical_df.columns,
    ):
        
        counts = (
            categorical_df[column].value_counts()
        )

        ax.bar(
            counts.index.astype(str),
            counts.values,
        )

        ax.set_title(
            f"{column} counts"
        )

        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")

        plt.setp(
            ax.get_xticklabels(),
            rotation=45,
            ha="right",
        )

    plt.tight_layout()

    return fig


def generate_visualizations(df: pd.DataFrame) -> dict:
    """
    Generate all visualizations for the given Dataframe.
    
    Returns
    -------
    dict
        Dictionary mapping chart names to
        matplotlib figure Objects (or None).
    """

    figures = {}

    figures["Missing values"] = create_missing_values_chart(df)
    
    figures["correlation heatmap"] = create_correlation_heatmap(df)
    
    figures["Histograms"] = create_histograms(df)

    figures["Boxplots"] = create_boxplots(df)

    figures["Categorical charts"] = create_barcharts(df)

    return figures



