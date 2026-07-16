"""
pdf_generator.py

Generate professional PDF reports for ResearchViz.
"""

from io import BytesIO
import tempfile

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    PageBreak,
)

import matplotlib.pyplot as plt


def create_styles():
    """
    Create all PDF styles.
    """

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading1"]

    subheading_style = styles["Heading2"]

    normal_style = styles["BodyText"]

    return {
        "title": title_style,
        "heading": heading_style,
        "subheading": subheading_style,
        "normal": normal_style,
    }


def create_table(data):
    """
    Create a professional ReportLab table.
    """

    table = Table(data)

    table.setStyle(
        TableStyle(

            [

                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563EB")),

                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

                ("FONTSIZE", (0, 0), (-1, 0), 11),

                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),

                ("ALIGN", (0, 0), (-1, -1), "CENTER"),

            ]
        )
    )

    return table


def figure_to_image(fig):
    """
    Convert a matplotlib figure into
    a ReportLab Image.
    """

    temp = tempfile.NamedTemporaryFile(
        suffix=".png",
        delete=False,
    )

    fig.savefig(
        temp.name,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close(fig)
    temp.close()

    return Image(
        temp.name,
        width=7.2 * inch,
        height=5.4 * inch,
    )


def add_footer(story, styles):

    story.append(
        Spacer(1, 0.4 * inch)
    )

    story.append(
        Paragraph(
            "Generated automatically by ResearchViz",
            styles["normal"],
        )
    )

    story.append(
        Paragraph(
            "© ResearchViz",
            styles["normal"],
        )
    )


def add_dataset_analysis(
    story,
    report,
    styles,
):
    """
    Add dataset analysis section.
    """

    analysis = report["Dataset Analysis"]

    story.append(
        Paragraph(
            "Dataset Analysis",
            styles["heading"],
        )
    )

    story.append(
        Spacer(1, 0.20 * inch)
    )

    table_data = [
        ["Metric", "Value"],
        ["Rows", str(analysis["Shape"]["rows"])],
        ["Columns", str(analysis["Shape"]["columns"])],
        ["Memory Usage (MB)", str(analysis["Memory usage (MB)"])],
        ["Duplicate Rows", str(analysis["Duplicate Rows"])],
    ]

    story.append(
        create_table(table_data)
    )

    story.append(
        Spacer(1, 0.30 * inch)
    )

def add_column_names(
    story,
    report,
    styles,
):
    """
    Add column names.
    """

    analysis = report["Dataset Analysis"]

    story.append(
        Paragraph(
            "Column Names",
            styles["heading"],
        )
    )

    story.append(
        Spacer(1, 0.15 * inch)
    )

    columns = ", ".join(
        analysis["Column Names"]
    )

    story.append(
        Paragraph(
            columns,
            styles["normal"],
        )
    )

    story.append(
        Spacer(1, 0.30 * inch)
    )


def add_missing_values(
    story,
    report,
    styles,
):
    """
    Add missing values table.
    """

    analysis = report["Dataset Analysis"]

    story.append(
        Paragraph(
            "Missing Values",
            styles["heading"],
        )
    )

    story.append(
        Spacer(1, 0.15 * inch)
    )

    table = [
        ["Column", "Missing Values"],
    ]

    for column, value in analysis["Missing Values"].items():

        table.append(
            [
                column,
                str(value),
            ]
        )

    story.append(
        create_table(table)
    )

    story.append(
        Spacer(1, 0.30 * inch)
    )


def add_data_types(
    story,
    report,
    styles,
):
    """
    Add data types table.
    """

    analysis = report["Dataset Analysis"]

    story.append(
        Paragraph(
            "Data Types",
            styles["heading"],
        )
    )

    story.append(
        Spacer(1, 0.15 * inch)
    )

    table = [
        ["Column", "Data Type"],
    ]

    for column, dtype in analysis["Data Types"].items():

        table.append(
            [
                column,
                dtype,
            ]
        )

    story.append(
        create_table(table)
    )

    story.append(
        Spacer(1, 0.30 * inch)
    )


def add_numeric_summary(
    story,
    report,
    styles,
):
    """
    Add numeric summary table.
    """

    analysis = report["Dataset Analysis"]

    numeric = analysis["Numeric Summary"]

    if not numeric:
        return

    story.append(
        Paragraph(
            "Numeric Summary",
            styles["heading"],
        )
    )

    story.append(
        Spacer(1, 0.20 * inch)
    )

    headers = ["Statistic"] + list(numeric.keys())

    table = [headers]

    statistics = list(next(iter(numeric.values())).keys())

    for stat in statistics:

        row = [stat]

        for column in numeric:

            value = numeric[column].get(stat, "")

            if isinstance(value, float):
                value = round(value, 2)

            row.append(str(value))

        table.append(row)

    story.append(
        create_table(table)
    )

    story.append(
        Spacer(1, 0.30 * inch)
    )


def add_categorical_summary(
    story,
    report,
    styles,
):
    """
    Add categorical summary table.
    """

    analysis = report["Dataset Analysis"]

    categorical = analysis["Categorical summary"]

    if not categorical:
        return

    story.append(
        Paragraph(
            "Categorical Summary",
            styles["heading"],
        )
    )

    story.append(
        Spacer(1, 0.20 * inch)
    )

    headers = ["Statistic"] + list(categorical.keys())

    table = [headers]

    statistics = list(next(iter(categorical.values())).keys())

    for stat in statistics:

        row = [stat]

        for column in categorical:

            value = categorical[column].get(stat, "")

            row.append(str(value))

        table.append(row)

    story.append(
        create_table(table)
    )

    story.append(
        Spacer(1, 0.30 * inch)
    )


def add_correlation_matrix(
    story,
    report,
    styles,
):
    """
    Add correlation matrix table.
    """

    analysis = report["Dataset Analysis"]

    corr = analysis["Correlation Matrix"]

    if corr is None:
        return

    story.append(
        Paragraph(
            "Correlation Matrix",
            styles["heading"],
        )
    )

    story.append(
        Spacer(1, 0.20 * inch)
    )

    headers = [""] + list(corr.keys())

    table = [headers]

    for row_name in corr:

        row = [row_name]

        for col_name in corr:

            value = corr[row_name][col_name]

            if isinstance(value, float):
                value = round(value, 2)

            row.append(str(value))

        table.append(row)

    story.append(
        create_table(table)
    )

    story.append(
        Spacer(1, 0.40 * inch)
    )


def add_visualizations(
    story,
    figures,
    styles,
):
    """
    Add all generated visualizations
    to the PDF.
    """

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "Visualizations",
            styles["heading"],
        )
    )

    story.append(
        Spacer(1, 0.25 * inch)
    )

    for name, figure in figures.items():

        if figure is None:
            continue

        story.append(
            Paragraph(
                name,
                styles["subheading"],
            )
        )

        story.append(
            Spacer(1,0.10*inch)
        )

        if isinstance(figure, list):

            for fig in figure:

                story.append(
                    figure_to_image(fig)
                )

                story.append(
                    Spacer(1,0.25*inch)
                )

        else:

            story.append(
                figure_to_image(figure)
            )

            story.append(
                Spacer(1,0.25*inch)
            )



def generate_pdf(
    report: dict,
    figures: dict,
):
    """
    Main PDF generator.
    """

    pdf_buffer = BytesIO()

    document = SimpleDocTemplate(
        pdf_buffer,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = create_styles()

    story = []

    add_cover_page(
        story,
        report,
        styles,
    )

    add_cleaning_summary(
        story,
        report,
        styles,
    )

    add_dataset_analysis(
    story,
    report,
    styles,
    )

    add_column_names(
        story,
        report,
        styles,
    )

    add_missing_values(
        story,
        report,
        styles,
    )

    add_data_types(
        story,
        report,
        styles,
    )

    add_numeric_summary(
    story,
    report,
    styles,
    )

    add_categorical_summary(
        story,
        report,
        styles,
    )

    add_correlation_matrix(
        story,
        report,
        styles,
    )

    add_visualizations(
    story,
    figures,
    styles,
    )

    add_footer(
        story,
        styles,
    )

    document.build(story)

    pdf_buffer.seek(0)

    return pdf_buffer


def add_cover_page(
    story,
    report,
    styles,
):
    """
    Add the cover page.
    """

    story.append(
        Paragraph(
            "ResearchViz",
            styles["title"],
        )
    )

    story.append(
        Paragraph(
            "AI-Powered Research Dataset Report",
            styles["subheading"],
        )
    )

    story.append(
        Spacer(1, 0.40 * inch)
    )

    story.append(
        Paragraph(
            f"<b>Generated By:</b> {report['Generated By']}",
            styles["normal"],
        )
    )

    story.append(
        Paragraph(
            f"<b>Generated On:</b> {report['Generated On']}",
            styles["normal"],
        )
    )

    story.append(
        Spacer(1, 0.20 * inch)
    )

    story.append(
        Paragraph(
            """
            This report was automatically generated by
            <b>ResearchViz</b>.

            The dataset was cleaned, analyzed and
            visualized automatically before generating
            this report.
            """,
            styles["normal"],
        )
    )

    story.append(
        PageBreak()
    )


def add_cleaning_summary(
    story,
    report,
    styles,
):
    """
    Add the cleaning summary section.
    """

    story.append(
        Paragraph(
            "Cleaning Summary",
            styles["heading"],
        )
    )

    story.append(
        Spacer(1, 0.20 * inch)
    )

    cleaning = report["Cleaning Summary"]

    table_data = [
        ["Metric", "Value"],
    ]

    for key, value in cleaning.items():

        table_data.append(
            [
                key,
                str(value),
            ]
        )

    story.append(
        create_table(table_data)
    )

    story.append(
        Spacer(1, 0.35 * inch)
    )



