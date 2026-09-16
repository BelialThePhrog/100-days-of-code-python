# Day 64: Exploratory Data Analysis - Real Estate & Ecommerce

## Project Overview
This module covers Day 64 of the 100 Days of Code challenge, focusing on Exploratory Data Analysis (EDA) across two distinct datasets: USA Housing and Ecommerce Customers. The goal is to perform initial data profiling, understand dataset structures, and visualize relationships between variables to prepare for predictive modeling.

## Implemented Workflows

### 1. USA Housing Analysis (`usa_housing_eda.py`)
*   **Data Ingestion:** Loading real estate data and verifying its integrity using Pandas `.info()` and `.describe()`.
*   **Structural Overview:** Inspecting columns and basic statistical distributions of features like average area income, house age, and number of rooms.

### 2. Ecommerce Customers Analysis (`ecommerce_eda.py`)
*   **Bivariate Analysis:** Utilizing Seaborn's `jointplot` to visualize correlations between continuous variables (e.g., `Time on Website` vs. `Yearly Amount Spent`).
*   **Data Density Visualization:** Applying hexbin plots (`kind="hex"`) to effectively display dense data clusters representing app usage time against membership length.
*   **Pairwise Relationships:** Leveraging `sns.pairplot()` to instantly visualize relationships and distributions across the entire numerical dataset.

## Requirements & Execution
Ensure the `USA_Housing.csv` and `Ecommerce Customers.csv` files are present in your directory.
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python usa_housing_eda.py
python ecommerce_eda.py
