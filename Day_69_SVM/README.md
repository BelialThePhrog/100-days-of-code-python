# Day 69: Support Vector Machines & Grid Search

## Project Overview

This module focuses on Support Vector Machines (SVM) for classification tasks. The project utilizes the Breast Cancer Wisconsin dataset from `sklearn.datasets` to predict tumor malignancy. It establishes a baseline Support Vector Classifier (SVC) and then applies hyperparameter tuning using `GridSearchCV` to optimize the model's `C` and `gamma` parameters for improved recall and precision

## Skills Demonstrated

* **Support Vector Classification:** Implementing `sklearn.svm.SVC` to construct a baseline classifier for predicting target classes.
* **Hyperparameter Optimization:** Utilizing `sklearn.model_selection.GridSearchCV` to systematically test combinations of `C` and `gamma` parameters (across 25 candidates and 125 fits) to overcome baseline model limitations.
* **Model Evaluation:** Using `confusion_matrix` and `classification_report` to track improvements in accuracy and target class recall after parameter tuning.

## Disclaimer & Credits

The foundation for the machine learning and data analysis concepts was inspired by the "Python for Data Science and Machine Learning Bootcamp" by Jose Portilla.

**Independent Engineering & Custom Upgrades:** I heavily customized this module to transition from experimental Jupyter Notebooks into professional, production-ready modular Python scripts. I independently architected the clean functional structure and generated robust documentation.
