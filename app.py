import streamlit as st
import pandas as pd
from PIL import Image
import os

# =========================
# Page configuration
# =========================
st.set_page_config(
    page_title="Renewable Energy Risk Matrix in Africa",
    page_icon="🌍",
    layout="wide"
)

# =========================
# Load data
# =========================
@st.cache_data
def load_data():
    df = pd.read_excel("data/Matrix2_Risk_Heatmap_By_Region_Income.xlsx")
    return df

df = load_data()

# =========================
# Sidebar
# =========================
st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go to:",
    [
        "Project Overview",
        "Methodology",
        "Income Group Heatmaps",
        "Regional Heatmaps",
        "Summary Tables",
        "Interpretation",
        "Limitations"
    ]
)

# =========================
# Title
# =========================
st.title("🌍 Renewable Energy Derisking Risk Matrix in Africa")

st.markdown("""
This dashboard presents a comparative risk matrix for renewable energy investment across African countries. 
The objective is to identify structural and operational constraints that may increase the need for derisking mechanisms in renewable energy projects.
""")

# =========================
# Project Overview
# =========================
if section == "Project Overview":
    st.header("Project Overview")

    st.markdown("""
    This project builds a **renewable energy investment risk matrix** for African countries. 
    Unlike general attractiveness indices, this matrix focuses on **risk exposure** and **derisking needs**.

    The analysis uses six dimensions:

    - **Fossil fuel subsidies**
    - **Transmission and distribution losses**
    - **Climate vulnerability**
    - **Electricity access constraints**
    - **Renewable energy policy readiness**
    - **Logistics performance**

    The final output is a composite risk score and a set of heatmaps by income group and African region.
    """)

    st.subheader("Dataset Preview")
    st.dataframe(df, use_container_width=True)

# =========================
# Methodology
# =========================
elif section == "Methodology":
    st.header("Methodology")

    st.markdown("""
    The risk matrix was constructed in four main steps.

    **Step 1 — Data cleaning and harmonization**  
    Six datasets were cleaned and harmonized by country and year.

    **Step 2 — Latest available historical observation**  
    For each country and each variable, the latest available historical observation was retained. 
    Future projections were excluded.

    **Step 3 — Risk orientation**  
    All variables were transformed so that a higher value represents a higher level of risk. 
    Variables such as electricity access, RISE score and LPI score were inverted because lower values indicate weaker enabling conditions.

    **Step 4 — Quartile scoring**  
    Each variable was converted into quartiles:

    - **1 = low risk**
    - **2 = moderate-low risk**
    - **3 = moderate-high risk**
    - **4 = high risk**

    The composite risk score is calculated as the average of the available quartile scores for each country.
    """)

    st.subheader("Risk Dimensions")

    risk_table = pd.DataFrame({
        "Dimension": [
            "Fossil fuel subsidies",
            "Transmission and distribution losses",
            "Climate vulnerability",
            "Electricity access constraints",
            "Renewable energy policy readiness",
            "Logistics performance"
        ],
        "Interpretation": [
            "Higher subsidies indicate stronger dependence on fossil-based energy systems.",
            "Higher losses reflect grid inefficiency and potential offtaker risk.",
            "Higher vulnerability increases exposure to climate-related shocks.",
            "Lower electricity access indicates weaker energy infrastructure.",
            "Lower RISE scores indicate weaker renewable energy policy and regulatory frameworks.",
            "Lower LPI scores indicate higher operational and supply-chain constraints."
        ]
    })

    st.dataframe(risk_table, use_container_width=True)

# =========================
# Income Group Heatmaps
# =========================
elif section == "Income Group Heatmaps":
    st.header("Heatmaps by Income Group")

    st.markdown("""
    The heatmaps show relative risk levels by country and by risk dimension.

    - **Dark purple / blue** = lower relative risk  
    - **Green** = intermediate risk  
    - **Yellow** = higher relative risk  
    - **White** = missing data  

    The values range from **1 to 4**, where 1 indicates low risk and 4 indicates high risk.
    """)

    image_files = {
        "Low income": "images/Matrix2_Heatmap_Low_income.png",
        "Lower-middle income": "images/Matrix2_Heatmap_Lower_middle_income.png",
        "Upper-middle income": "images/Matrix2_Heatmap_Upper_middle_income.png"
    }

    selected_group = st.selectbox("Select income group:", list(image_files.keys()))

    image_path = image_files[selected_group]

    if os.path.exists(image_path):
        img = Image.open(image_path)
        st.image(img, caption=f"Renewable Energy Risk Heatmap — {selected_group}", use_container_width=True)
    else:
        st.warning(f"Image not found: {image_path}")

# =========================
# Regional Heatmaps
# =========================
elif section == "Regional Heatmaps":
    st.header("Heatmaps by African Region")

    region_image_files = {
        "West Africa": "images/Matrix2_Heatmap_West_Africa.png",
        "East Africa": "images/Matrix2_Heatmap_East_Africa.png",
        "North Africa": "images/Matrix2_Heatmap_North_Africa.png",
        "Central Africa": "images/Matrix2_Heatmap_Central_Africa.png",
        "Southern Africa": "images/Matrix2_Heatmap_Southern_Africa.png"
    }

    selected_region = st.selectbox("Select region:", list(region_image_files.keys()))

    image_path = region_image_files[selected_region]

    if os.path.exists(image_path):
        img = Image.open(image_path)
        st.image(img, caption=f"Renewable Energy Risk Heatmap — {selected_region}", use_container_width=True)
    else:
        st.warning(f"Image not found: {image_path}")

# =========================
# Summary Tables
# =========================
elif section == "Summary Tables":
    st.header("Summary Tables")

    st.subheader("Top 10 Highest-Risk Countries")
    st.dataframe(
        df.sort_values("Composite Risk Score", ascending=False).head(10),
        use_container_width=True
    )

    st.subheader("Top 10 Lowest-Risk Countries")
    st.dataframe(
        df.sort_values("Composite Risk Score", ascending=True).head(10),
        use_container_width=True
    )

    st.subheader("Average Risk by Region")
    region_summary = df.groupby("Region").agg(
        Average_Risk_Score=("Composite Risk Score", "mean"),
        Number_of_Countries=("Country", "count")
    ).reset_index().sort_values("Average_Risk_Score", ascending=False)

    st.dataframe(region_summary, use_container_width=True)

    st.subheader("Average Risk by Income Group")
    income_summary = df.groupby("Income Group").agg(
        Average_Risk_Score=("Composite Risk Score", "mean"),
        Number_of_Countries=("Country", "count")
    ).reset_index().sort_values("Average_Risk_Score", ascending=False)

    st.dataframe(income_summary, use_container_width=True)

# =========================
# Interpretation
# =========================
elif section == "Interpretation":
    st.header("Interpretation")

    st.subheader("Low-Income Countries")
    st.markdown("""
    Low-income countries show the highest concentration of structural risks. 
    Countries such as **Niger, Central African Republic, Sudan and Burundi** appear among the most exposed cases. 
    Their risk profiles are mainly driven by climate vulnerability, limited electricity access, weak renewable energy policy readiness and logistics constraints.
    """)

    st.subheader("Lower-Middle-Income Countries")
    st.markdown("""
    Lower-middle-income countries present a more heterogeneous profile. 
    Some countries show high risk across several dimensions, while others such as **Morocco, Ghana, Côte d'Ivoire, Egypt and Tunisia** appear relatively better positioned.
    This shows that income level alone does not fully explain renewable energy investment risk.
    """)

    st.subheader("Upper-Middle-Income Countries")
    st.markdown("""
    Upper-middle-income countries generally show lower overall risk, especially in electricity access and infrastructure-related dimensions. 
    However, some countries such as **Libya and Algeria** still present transition-related risks linked to fossil fuel dependence and policy or logistics constraints.
    """)

    st.subheader("Overall Finding")
    st.markdown("""
    Renewable energy investment risk in Africa is multidimensional. 
    The highest-risk countries are those where several constraints overlap, including weak electricity access, high climate vulnerability, grid inefficiencies, weak policy readiness, logistics limitations and fossil fuel dependence.

    The matrix can be used as a decision-support tool to identify where renewable energy projects may require stronger derisking mechanisms, including guarantees, concessional finance, public-private partnerships, regulatory reforms, grid investments and targeted technical assistance.
    """)

# =========================
# Limitations
# =========================
elif section == "Limitations":
    st.header("Limitations")

    st.markdown("""
    This dashboard should be interpreted as a comparative risk-screening tool, not as a full investment due diligence model.

    Main limitations include:

    - Missing data for some countries and indicators.
    - Use of latest available observations rather than a full dynamic panel model.
    - Equal weighting of risk dimensions.
    - Quartile scores measure relative risk within the sample, not absolute risk.
    - LPI is partly based on perception-based logistics assessments.

    Future improvements may include adding financial risk indicators, political risk indicators, grid investment data, renewable project pipeline data, and comparison with external benchmarks such as Climatescope.
    """)
