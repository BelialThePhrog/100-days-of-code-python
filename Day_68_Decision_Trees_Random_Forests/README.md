# Day 68: Decision Trees & Random Forests Project

## Project Overview

This module explores tree-based machine learning algorithms for classification tasks. It features two distinct datasets:
1. **Kyphosis Practice:** Predicting the presence of the spinal condition post-surgery based on patient age and affected vertebrae.
2. **Lending Club Project:** Classifying historical loan data from 2007-2010 to predict whether a borrower will pay back their loan in full (`not.fully.paid`).

## Skills Demonstrated

* **Categorical Data Engineering:** Converting categorical text features (e.g., loan `purpose`) into numerical formats using `pd.get_dummies(drop_first=True)`.
* **Exploratory Data Analysis (EDA):** Visualizing distributions using `seaborn.pairplot` and overlapping histograms based on target variables (e.g., FICO scores by credit policy).
* **Decision Tree Classification:** Implementing `DecisionTreeClassifier` to create highly interpretable baseline models.
* **Ensemble Learning:** Applying `RandomForestClassifier` to aggregate multiple decision trees, effectively reducing variance and preventing overfitting.
* **Model Evaluation:** Interpreting `confusion_matrix` and `classification_report` to compare the accuracy and f1-scores between single trees and forest ensembles.

## Disclaimer & Credits

The foundation for the machine learning and data analysis concepts was inspired by the "Python for Data Science and Machine Learning Bootcamp" by Jose Portilla.

**Independent Engineering & Custom Upgrades:** I heavily customized this module to transition from experimental Jupyter Notebooks into professional, production-ready modular Python scripts. I independently architected the clean functional structure and generated robust documentation.
