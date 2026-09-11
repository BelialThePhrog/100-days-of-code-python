# Day 62: Interactive Plotting with Plotly and Cufflinks

## Project Overview
This module transitions from static data visualization to dynamic, interactive charts. By shifting the Pandas plotting backend to `plotly` and utilizing `cufflinks`, these scripts demonstrate how to create zoomable, hover-enabled visualizations. Interactive charting is a critical skill for modern data analytics, allowing users to drill down into specific data points without writing complex visualization code from scratch.

## Skills Demonstrated
*   **Environment Configuration:** Setting up offline mode for `cufflinks` and overriding the default Pandas plotting engine (`pd.options.plotting.backend = "plotly"`).
*   **Interactive Line Plots:** Generating dynamic charts where individual data points can be inspected via hover tooltips, and axes can be zoomed or panned.
*   **Data Generation & Mapping:** Using `numpy` to generate test DataFrames and mapping discrete color sequences (e.g., `color_discrete_sequence=['gold']`) to specific data series.
*   **Package Management:** Handling dependencies including `chart-studio`, `cufflinks`, and `plotly` to enable seamless interactive rendering in local environments.

## How to Run
Ensure the required libraries are installed before running the script:
```bash
pip install plotly cufflinks chart-studio
python interactive_plotly_cufflinks.py
