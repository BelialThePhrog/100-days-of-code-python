# Day 73: Natural Language Processing (NLP) Project

## Project Overview

This module explores Natural Language Processing (NLP) by classifying text data. The primary objective is to categorize Yelp reviews into 1-star or 5-star ratings based purely on their text content]. The project also draws on text processing techniques commonly used in spam detection systems.

## Skills Demonstrated

* **Text Feature Engineering:** Creating new features, such as `text length`, to analyze word counts across different rating categories.
* **Exploratory Data Analysis (EDA):** Using `seaborn.FacetGrid` to visualize text length distributions and generating correlation heatmaps to identify relationships between review metrics (cool, useful, funny.
* **Text Vectorization:** Converting raw text into a matrix of token counts using `CountVectorizer`.
* **TF-IDF Transformation:** Applying Term Frequency-Inverse Document Frequency (`TfidfTransformer`) to normalize word counts and evaluate term importance.
* **Machine Learning Pipelines:** Constructing a `sklearn.pipeline.Pipeline` to streamline the workflow from text vectorization to model training with a `MultinomialNB` (Naive Bayes) classifier.

## Disclaimer & Credits

The foundation for the machine learning and data analysis concepts was inspired by the "Python for Data Science and Machine Learning Bootcamp" by Jose Portilla.

**Independent Engineering & Custom Upgrades:** I heavily customized this module to transition from experimental Jupyter Notebooks into professional, production-ready modular Python scripts. I independently architected the clean functional structure, integrated advanced pipeline management, and generated robust documentation.
