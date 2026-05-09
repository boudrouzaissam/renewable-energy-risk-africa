# Renewable Energy Derisking Risk Matrix in Africa

## Project Overview

This project builds a comparative risk matrix for renewable energy investment across African countries. The objective is to identify structural and operational constraints that may increase the need for derisking mechanisms in renewable energy projects.

Unlike general investment attractiveness indices, this dashboard focuses on risk exposure and derisking needs.

## Risk Dimensions

The matrix is based on six dimensions:

1. Fossil fuel subsidies
2. Transmission and distribution losses
3. Climate vulnerability
4. Electricity access constraints
5. Renewable energy policy readiness
6. Logistics performance

## Methodology

The project follows four main steps:

1. Data cleaning and harmonization from international datasets.
2. Selection of the latest available historical observation for each country and variable.
3. Transformation of indicators so that higher values represent higher risk.
4. Quartile scoring from 1 to 4, where 1 indicates low relative risk and 4 indicates high relative risk.

The composite risk score is calculated as the average of the available quartile scores.

## Dashboard Content

The Streamlit dashboard includes:

- Project overview
- Methodology
- Heatmaps by income group
- Heatmaps by African region
- Summary risk tables
- Interpretation of results
- Limitations and future improvements

## Tools Used

- Python
- pandas
- matplotlib
- openpyxl
- Streamlit
- Excel

## Key Output

The dashboard provides visual heatmaps that help compare renewable energy investment risks across African countries by income group and region.

## Author

Aissam Boudrouz
