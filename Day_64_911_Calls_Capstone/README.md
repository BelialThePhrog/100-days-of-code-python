# Day 64: 911 Calls Data Capstone Project

## Project Overview
This module consolidates an exploratory data analysis (EDA) of emergency 911 calls. The project focuses on data wrangling, feature engineering, and time-series visualization using Pandas, Matplotlib, and Seaborn[. 

## Skills Demonstrated
*   **Feature Engineering:** Extracting specific categorical variables (e.g., call reasons) from text strings using `apply()` and lambda functions.
*   **Datetime Manipulation:** Converting string timestamps into Pandas Datetime objects to extract `Hour`, `Month`, `Day of Week`, and `Date`.
*   **Data Mapping:** Transforming integer representations into readable string categories using `.map()`.
*   **Data Aggregation & Grouping:** Using `.groupby()` alongside `.count()` and `.reset_index()` to prepare datasets for regression and time-series plotting.
*   **Advanced Visualization:** Generating categorical countplots, linear regression models (`sns.lmplot()`), and multi-plot time-series distributions for distinct emergency categories (Traffic, Fire, EMS).

## How to Run
Ensure `911.csv` is located in the same directory as the script.
```bash
pip install pandas matplotlib seaborn
python 911_calls_analysis.py
