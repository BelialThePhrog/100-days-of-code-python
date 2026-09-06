# Day 57: Pandas Data Analysis Exercises

## Project Overview

Continuing the pivot into the Data Science and Machine Learning curriculum, this module focuses on practical data manipulation and exploratory data analysis (EDA). The project is split into two real-world inspired exercises: parsing a dataset of mocked E-commerce purchases and analyzing a public dataset of San Francisco city employee salaries.

## Skills Demonstrated

* **Data Aggregation & Grouping:** Utilizing the `groupby()` function to isolate metrics by year and calculating specific means (e.g., Average BasePay across different years).
* **Advanced String Manipulation:** Applying Python's `lambda` functions to split email domains and extract specific substring indices (like credit card expiration years).
* **Regular Expressions in Pandas:** Leveraging `str.contains(r'\bchief\b')` with word boundary indicators to accurately filter job titles while ignoring substrings like "mischief".
* **Correlation Analysis:** Creating derived columns (e.g., length of a job title) and using the `.corr()` method to determine statistical relationships against total compensation.
* **Complex Boolean Masking:** Combining multiple conditional statements to filter DataFrames, such as matching specific credit card providers with transaction thresholds.

## Disclaimer & Credits

**Custom Curriculum Path:** These exercises belong to the **"Python for Data Science and Machine Learning Bootcamp"**, reflecting a direct pivot toward Data Analytics. 

## How to Run

Ensure `pandas` is installed. You will need the raw data files (`Ecommerce Purchases.csv` and `Salaries.csv`) in your working directory to execute the scripts. 

To run the Ecommerce analysis:
```bash
python ecommerce_analysis.py
```
To run the Ecommerce analysis:
```bash
python sf_salaries_analysis.py
```
