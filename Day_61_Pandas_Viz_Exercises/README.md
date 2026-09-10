# Day 61: Pandas Data Visualization (Practice & Exercises)

## Project Overview

This module focuses on the built-in data visualization capabilities of the `pandas` library. The workflow is split into two sections: a practice script to explore fundamental plotting methods using `df1` and `df2`, and a challenge script that reconstructs target visualizations based on a specific set of parameters using `df3`

## Skills Demonstrated

* **Data Importing:** Handling time-series indices (`index_col=0`) and standard CSV imports.
* **Core Plot Types:** Generating scatter plots with custom colormaps, histograms with explicit bin counts, and boxplots for distribution comparisons.
* **Aesthetic Tuning:** Modifying global styles via `plt.style.use('ggplot')`, adjusting alpha for transparency, and mapping colors.
* **Advanced Charting:** Creating Kernel Density Estimation (KDE) plots with custom line weights/styles, and building stacked area charts.
* **Layout Management:** Relocating plot legends outside the main figure boundaries using `bbox_to_anchor.

## How to Run

Ensure the `df1`, `df2`, and `df3` CSV files are in the same directory as the script.

```bash
python pandas_viz_combined.py
