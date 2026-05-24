Skip to content
boudrouzaissam
renewable-energy-risk-africa
Repository navigation
Code
Issues
Pull requests
Actions
Projects
Wiki
Security and quality
Insights
Settings
Owner avatar
renewable-energy-risk-africa
Public
boudrouzaissam/renewable-energy-risk-africa
Go to file
t
T
Name		
boudrouzaissam
boudrouzaissam
Added Dev Container Folder
fde318a
 · 
2 minutes ago
.devcontainer
Added Dev Container Folder
2 minutes ago
data
Add files via upload
2 weeks ago
images
Add files via upload
2 weeks ago
README.md
Add files via upload
2 weeks ago
app.py
Add files via upload
2 weeks ago
requirements.txt
Add files via upload
2 weeks ago
Repository files navigation
README
Renewable Energy Derisking Risk Matrix in Africa
Project Overview
This project builds a comparative risk matrix for renewable energy investment across African countries. The objective is to identify structural and operational constraints that may increase the need for derisking mechanisms in renewable energy projects.

Unlike general investment attractiveness indices, this dashboard focuses on risk exposure and derisking needs.

Risk Dimensions
The matrix is based on six dimensions:

Fossil fuel subsidies
Transmission and distribution losses
Climate vulnerability
Electricity access constraints
Renewable energy policy readiness
Logistics performance
Methodology
The project follows four main steps:

Data cleaning and harmonization from international datasets.
Selection of the latest available historical observation for each country and variable.
Transformation of indicators so that higher values represent higher risk.
Quartile scoring from 1 to 4, where 1 indicates low relative risk and 4 indicates high relative risk.
The composite risk score is calculated as the average of the available quartile scores.

Dashboard Content
The Streamlit dashboard includes:

Project overview
Methodology
Heatmaps by income group
Heatmaps by African region
Summary risk tables
Interpretation of results
Limitations and future improvements
Tools Used
Python
pandas
matplotlib
openpyxl
Streamlit
Excel
Key Output
The dashboard provides visual heatmaps that help compare renewable energy investment risks across African countries by income group and region.

Author
Aissam Boudrouz

About
Streamlit dashboard assessing renewable energy investment risks across African countries using a composite derisking risk matrix.

Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 0 watching
Forks
 0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
1
@boudrouzaissam
boudrouzaissam
Languages
Python
100.0%
Suggested workflows
Based on your tech stack
Publish Python Package logo
Publish Python Package
Publish a Python Package to PyPI on release.
Python application logo
Python application
Create and test a Python application.
Python Package using Anaconda logo
Python Package using Anaconda
Create and test a Python package on multiple Python versions using Anaconda for package management.
More workflows
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
