# Day 56: Introduction to Pandas & Data Analysis

## Project Overview

A strategic pivot towards Data Science and Machine Learning. This module establishes the foundational knowledge required for data manipulation and analysis using the `pandas` and `numpy` libraries, shifting focus from frontend web development to backend data engineering.

## Skills Demonstrated

* **Data Structures:** Creating and manipulating multi-dimensional DataFrames and 1D Series using custom indices and NumPy arrays.
* **Data Selection & Indexing:** Filtering datasets using boolean masking, conditional logic (`df[df["W"] > 0]`), and extracting specific rows/columns.
* **Missing Data Handling:** Cleaning datasets by dropping null values (`dropna`) or filling them with specific threshold parameters (`fillna`).
* **Data Merging & Operations:** Combining DataFrames using `concat`, `merge`, and `join`. Applying custom lambda/Python functions across data series (`apply`), and generating pivot tables.
* **File I/O:** Reading and exporting datasets to external formats, including CSV and Excel files.

## Disclaimer & Credits

**Custom Curriculum Path:** To better align with my career trajectory as a Data Analyst, this specific module temporarily diverges from Dr. Angela Yu's "100 Days of Code™" web-focused curriculum. The concepts and exercises documented here were sourced from the **"Python for Data Science and Machine Learning Bootcamp"**.

## How to Run

Ensure `pandas` and `numpy` are installed in your environment. You will also need a sample CSV (`example`) and Excel file (`Excel_Sample.xlsx`) in the directory to test the File I/O functions.

```bash
python pandas_crash_course.py
