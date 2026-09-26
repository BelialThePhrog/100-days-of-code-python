# Day 71: Principal Component Analysis (PCA)

## Project Overview

This module focuses on dimensionality reduction using Principal Component Analysis (PCA). By utilizing the Breast Cancer Wisconsin dataset, the project demonstrates how to condense a 30-feature dataset into 3 principal components while preserving the core variance for visualization and analysis[cite: 13].

## Skills Demonstrated

* **Feature Scaling:** Implementing `StandardScaler` to normalize the data distributions, a mandatory prerequisite for effective PCA.
* **Dimensionality Reduction:** Utilizing `sklearn.decomposition.PCA` to reduce the dataset's dimensionality from 30 to 3 components.
* **Data Visualization:** Mapping the principal components into a 2D space using `matplotlib.pyplot.scatter` to visualize class separation based on the target variable.
* **Component Interpretation:** Generating a correlation heatmap with `seaborn.heatmap` to analyze the relationship between the original features and the newly created principal components.

## Disclaimer & Credits

The foundation for the machine learning and data analysis concepts was inspired by the "Python for Data Science and Machine Learning Bootcamp" by Jose Portilla.

**Independent Engineering & Custom Upgrades:** I heavily customized this module to transition from experimental Jupyter Notebooks into professional, production-ready modular Python scripts. I independently architected the clean functional structure and generated robust documentation.
