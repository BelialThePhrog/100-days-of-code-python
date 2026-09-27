# Day 72: Recommender Systems Project

## Project Overview

This module focuses on building a foundational Item-Based Collaborative Filtering Recommender System. Utilizing a subset of the MovieLens dataset (`u.data` and `Movie_Id_Titles`). the system recommends movies to users based on similarities in user rating patterns.

## Skills Demonstrated

* **Data Wrangling:** Merging relational datasets, utilizing `groupby` to aggregate metrics (mean ratings and review counts), and reshaping data using `pd.pivot_table` to construct a user-item rating matrix.
* **Exploratory Data Analysis (EDA):** Visualizing the relationship between average movie ratings and the volume of ratings using `seaborn.jointplot` and histograms.
* **Correlation Analysis:** Calculating the Pearson correlation coefficient between specific movie vectors (e.g., *Star Wars (1977)* and *Liar Liar (1997)*) and the rest of the matrix using `corrwith()`.
* **Recommendation Filtering:** Implementing review-count thresholds (e.g., >70 or >60 ratings) to filter out spurious correlations from movies with too few reviews, ensuring reliable recommendations.

## Disclaimer & Credits

The foundation for the machine learning and data analysis concepts was inspired by the "Python for Data Science and Machine Learning Bootcamp" by Jose Portilla.

**Independent Engineering & Custom Upgrades:** I heavily customized this module to transition from experimental Jupyter Notebooks into professional, production-ready modular Python scripts. I independently architected the clean functional structure, wrapped the logic into reusable functions, and generated robust documentation.
