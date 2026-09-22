# Day 67: K Nearest Neighbors (KNN) Project

## Project Overview

A machine learning workflow focusing on the K Nearest Neighbors (KNN) algorithm. This project involves predicting a target class based on anonymized features by standardizing the data, applying the KNN algorithm, and optimizing the `n_neighbors` parameter using the Elbow Method to minimize the error rate.

## Skills Demonstrated

* **Data Preprocessing:** Utilizing `sklearn.preprocessing.StandardScaler` to standardize feature scales, which is a critical requirement for distance-based algorithms like KNN.
* **Model Evaluation:** Interpreting `confusion_matrix` and `classification_report` to assess model accuracy, precision, recall, and f1-score.
* **Parameter Tuning (Elbow Method):** Iterating through various K values (from 1 to 60) and plotting error rates with `matplotlib` to visually identify the optimal number of neighbors.

## Disclaimer & Credits

The foundation for the machine learning and data analysis concepts was inspired by the "Python for Data Science and Machine Learning Bootcamp" by Jose Portilla.

**Independent Engineering & Custom Upgrades:** I heavily customized this module to transition from experimental Jupyter Notebooks into a professional, production-ready modular script format. I independently architected the clean functional structure and generated robust documentation that highlights my independent approach to Machine Learning.
