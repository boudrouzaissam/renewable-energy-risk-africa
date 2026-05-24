import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Renewable Energy Derisking Risk Matrix in Africa",
    layout="wide"
)

BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / "images"
DATA_DIR = BASE_DIR / "data"

st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go to:",
    [
        "Project Overview",
        "Methodology",
        "Main Heatmap",
        "Income Group Heatmaps",
        "Regional Heatmaps",
        "Summary Tables",
        "Interpretation",
        "Limitations"
    ]
)

st.title("Renewable Energy Derisking Risk Matrix in Africa")


def show_image(path, caption=None):
    if path.exists():
        st.image(str(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Image not found: {path}")


if section == "Project Overview":
    st.header("Project Overview")
    st.write(
        """
        This dashboard presents a comparative risk matrix for renewable energy investment across African countries.
        The objective is to identify structural and operational constraints that may increase the need for derisking
        mechanisms in renewable energy projects.
        """
    )

elif section == "Methodology":
    st.header("Methodology")
    st.write(
        """
        The matrix is based on six risk dimensions:

        - Fossil fuel subsidies
        - Transmission and distribution losses
        - Climate vulnerability
        - Electricity access constraints
        - Renewable energy policy readiness
        - Logistics performance

        Each variable is transformed so that higher values represent higher risk.
        Risk scores are calculated using quartiles from 1 to 4:

        - 1 = Low risk
        - 2 = Moderate-low risk
        - 3 = Moderate-high risk
        - 4 = High risk

        The composite risk score is calculated as the average of available risk scores.
        """
    )

elif section == "Main Heatmap":
    st.header("Main Risk Heatmap")
    show_image(
        IMAGES_DIR / "Matrix2_Heatmap.png",
        "Matrix 2 - Renewable Energy Derisking Risk Heatmap"
    )

elif section == "Income Group Heatmaps":
    st.header("Heatmaps by Income Group")

    income_options = {
        "Low income": "Matrix2_Heatmap_Low_income.png",
        "Lower middle income": "Matrix2_Heatmap_Lower_middle_income.png",
        "Upper middle income": "Matrix2_Heatmap_Upper_middle_income.png",
        "High income": "Matrix2_Heatmap_High_income.png"
    }

    selected_income = st.selectbox("Select income group:", list(income_options.keys()))
    show_image(IMAGES_DIR / income_options[selected_income], selected_income)

elif section == "Regional Heatmaps":
    st.header("Heatmaps by African Region")

    region_options = {
        "North Africa": "Matrix2_Heatmap_North_Africa.png",
        "West Africa": "Matrix2_Heatmap_West_Africa.png",
        "Central Africa": "Matrix2_Heatmap_Central_Africa.png",
        "East Africa": "Matrix2_Heatmap_East_Africa.png",
        "Southern Africa": "Matrix2_Heatmap_Southern_Africa.png"
    }

    selected_region = st.selectbox("Select region:", list(region_options.keys()))
    show_image(IMAGES_DIR / region_options[selected_region], selected_region)

elif section == "Summary Tables":
    st.header("Summary Tables")

    excel_file = DATA_DIR / "Matrix2_Risk_Heatmap.xlsx"

    if excel_file.exists():
        st.success("Excel matrix file is available.")
        with open(excel_file, "rb") as f:
            st.download_button(
                label="Download Excel Risk Matrix",
                data=f,
                file_name="Matrix2_Risk_Heatmap.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.warning(f"Excel file not found: {excel_file}")

elif section == "Interpretation":
    st.header("Interpretation")
    st.write(
        """
        Green cells indicate low relative risk, yellow cells indicate intermediate risk,
        and red cells indicate high relative risk. Countries with higher composite scores
        face stronger structural constraints for renewable energy investment and may require
        stronger derisking mechanisms.
        """
    )

elif section == "Limitations":
    st.header("Limitations")
    st.write(
        """
        This matrix is descriptive and comparative. It depends on data availability and the latest
        available historical observations. Some countries may have missing values for certain variables.
        Future improvements may include alternative weighting methods, regional classifications,
        income group analysis, and comparison with investment attractiveness indices such as Climatescope.
        """
    )
