# Day 61: Pandas Data Visualization - Exercises

## Project Overview

This module serves as a practical assessment of built-in Pandas data visualization capabilities. As part of the broader Data Analytics and Machine Learning progression, the exercises demonstrate how to generate rapid, insightful plots directly from DataFrames without writing extensive `matplotlib` boilerplate.

## Skills Demonstrated

* **Scatter Plots:** Adjusting figure size (`figsize`), point color, and size mapping (`df.plot.scatter`).
* **Histograms & Styling:** Modifying bin counts, transparency (`alpha`), and applying the `ggplot` style sheet for presentation-ready aesthetics.
* **Boxplots:** Comparing distributions of multiple columns simultaneously (`df[['a', 'b']].plot.box()`).
* **Kernel Density Estimation (KDE):** Visualizing continuous probability density and customizing line weights and styles (`style="--"`).
* **Area Plots & Layout Management:** Slicing DataFrames (`iloc`), generating stacked area charts, and relocating the legend outside the plot boundaries using `bbox_to_anchor`.

## How to Run

The script generates dummy data reflecting the structure of the original exercise dataset (`df3`). 

```bash
python pandas_viz_exercises.py
