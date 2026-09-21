# Day 66: Logistic Regression Practice & Project

## Project Overview

A complete machine learning workflow focusing on binary classification using Logistic Regression. This module is divided into two parts: a practice session tackling the famous Titanic survival dataset (data cleaning, missing value imputation, categorical dummy variables) and a core project analyzing a digital advertising dataset to predict whether a user will click on an ad based on demographic and behavioral metrics.

## Skills Demonstrated

* **Data Cleaning & Imputation:** Building custom Python functions applied via `pandas.apply()` to intelligently fill missing age values based on passenger class.
* **Categorical Feature Engineering:** Utilizing `pd.get_dummies(drop_first=True)` to convert text-based categorical variables (Sex, Embarked) into machine-readable boolean/integer formats while avoiding the dummy variable trap.
* **Logistic Regression Modeling:** Implementing the `sklearn.linear_model.LogisticRegression` algorithm to perform binary classification.
* **Performance Evaluation:** Utilizing `sklearn.metrics.classification_report` to critically assess model performance across Precision, Recall, and F1-Score metrics instead of relying solely on baseline accuracy.

## Disclaimer & Credits

The foundation for the machine learning and data analysis concepts was inspired by the "100 Days of Code™: The Complete Python Pro Bootcamp" by Dr. Angela Yu.

**Custom Upgrades & AI Collaboration:** I heavily customized this module to transition from experimental Jupyter Notebooks into a professional, production-ready modular script format. I explicitly acknowledge utilizing AI as an engineering partner to architect this clean functional structure, handle library convergence warnings (`max_iter`), resolve pandas deprecation warnings, and generate robust documentation that highlights my independent approach to Machine Learning.

## How to Run

Ensure the dataset files (`titanic_train.csv` and `advertising.csv`) are in the same directory as the scripts and you have the `scikit-learn`, `pandas`, `seaborn`, and `matplotlib` packages installed.

```bash
python titanic_practice.py
python advertising_project.py
