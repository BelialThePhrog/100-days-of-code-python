# Day XX: Linear Regression Practice Projects

## Project Overview

Two supervised machine learning projects built while practicing linear regression with scikit-learn. The first predicts house prices from area-level housing and demographic statistics (`USA_Housing.csv`). The second predicts a customer's yearly spending for an e-commerce clothing retailer based on how they engage with the company's mobile app versus its website (`Ecommerce Customers`).

## Skills Demonstrated

- **Exploratory Data Analysis:** Using `seaborn` (`pairplot`, `jointplot`, `heatmap`, `lmplot`) to visualize feature distributions and correlations before committing to a model.
- **Feature/Target Selection:** Isolating relevant numerical predictor columns and separating them from the target variable ahead of training.
- **Model Training:** Splitting data with `train_test_split` and fitting `sklearn.linear_model.LinearRegression`, then inspecting the resulting coefficients to interpret feature impact.
- **Model Evaluation:** Scoring predictions with Mean Absolute Error, Mean Squared Error, and Root Mean Squared Error (`sklearn.metrics`), then validating fit quality with residual distribution plots.

## Disclaimer & Credits

The project structure and the `Ecommerce Customers` dataset/exercise were provided as part of a Python for Data Science and Machine Learning course (Pierian Data). I completed the linear regression modeling and evaluation logic myself, and independently applied the same end-to-end pipeline (EDA → train/test split → fit → evaluate → interpret coefficients) to a second dataset, `USA_Housing.csv`, as additional practice.

## How to Run

Ensure the relevant script (`usa_housing_regression.py` or `ecommerce_regression.py`) and its matching CSV file are in the same directory, then install dependencies:

```
pip install pandas numpy matplotlib seaborn scikit-learn
```

```
python usa_housing_regression.py
```

```
python ecommerce_regression.py
```
