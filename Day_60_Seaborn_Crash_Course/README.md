# Day 60: Seaborn Statistical Data Visualization

## Project Overview

Continuing the Data Science and Machine Learning track, this module focuses on statistical data visualization using the `seaborn` library. The exercises cover analyzing built-in datasets (`tips`, `flights`, `iris`) to uncover patterns, distributions, and correlations through advanced matrix, categorical plotting, grid mappings, and linear regression models.

## Skills Demonstrated

* **Distribution & Categorical Plots:** Visualizing data distributions and category comparisons using `histplot`, `jointplot`, `barplot`, `violinplot`, and `swarmplot`.
* **Matrix Plots:** Reshaping data with Pandas `pivot_table` to create multi-variable visualizations like `heatmap` and `clustermap`.
* **Grid Graphics:** Generating multi-plot grids using `PairGrid` and `FacetGrid` to instantly map dataset variables (like the `iris` dataset) to multiple axes based on categorical conditions.
* **Regression Plotting:** Fitting linear regression models using `lmplot` and customizing underlying matplotlib properties via dictionary arguments like `scatter_kws`.
* **Style & Context Tuning:** Globally controlling chart aesthetics and scaling elements for different presentation formats (e.g., presentations vs. papers) using `set_style`, `set_context`, and `despine`.

## How to Run

Ensure `seaborn`, `matplotlib`, `pandas`, and `numpy` are installed in your environment.

```bash
python seaborn_crash_course.py
