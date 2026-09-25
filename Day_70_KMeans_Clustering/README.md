# Day 70: K Means Clustering Project

## Project Overview

This module utilizes the unsupervised K-Means algorithm to partition universities into two groups (Private and Public) based on their features. Since this is an exercise in unsupervised learning, the actual labels from the `College_Data` dataset are excluded during training and only used at the end to evaluate the clustering performance.

## Skills Demonstrated

* **Exploratory Data Analysis (EDA):** Generating scatterplots (`sns.lmplot`) for room and board versus graduation rate, and full-time undergraduates versus out-of-state tuition. Visualizing distributions with overlapping histograms using `sns.FacetGrid`.
* **Data Cleaning:** Identifying and correcting outliers, such as a graduation rate exceeding 100% for Cazenovia College (capped at 100%).
* **Unsupervised Machine Learning:** Implementing the `KMeans` algorithm with `n_clusters=2` on the full dataset, deliberately dropping the target column.
* **Clustering Evaluation:** Constructing a custom function to convert 'Yes'/'No' labels into a binary format for direct comparison against model-generated labels (using `confusion_matrix` and `classification_report`).

## Disclaimer & Credits

The foundation for the machine learning and data analysis concepts was inspired by the "Python for Data Science and Machine Learning Bootcamp" by Jose Portilla.

**Independent Engineering & Custom Upgrades:** I heavily customized this module to transition from experimental Jupyter Notebooks into professional, production-ready modular Python scripts. I independently architected the clean functional structure and generated robust documentation.
