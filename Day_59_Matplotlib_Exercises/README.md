# Day 59: Matplotlib OO API Exercises

## Project Overview

This module applies the Object-Oriented Matplotlib API concepts to a formal set of visualization exercises. The goal is to accurately recreate target plots by managing figure objects, defining custom axes locations, and adjusting figure sizes.

## Skills Demonstrated

* **Axes Instantiation:** Creating figure objects and explicitly adding axes at specific `[left, bottom, width, height]` coordinates to build inset plots (e.g., placing an inner axis at `[0.2, 0.5, 0.2, 0.2]`).
* **Data Mapping:** Plotting multiple mathematical relationships (linear `y = x*2` and quadratic `z = x**2`) across different axes within the same figure.
* **Subplot Grids:** Utilizing `plt.subplots(nrows=1, ncols=2)` to generate side-by-side axes arrays
* **Aesthetic Tuning:** Adjusting line colors (`color="blue"`, `color="red"`) and styles (`ls="--"`) to distinguish data series across multiple subplots.
* **Figure Dimensions:** Modifying the aspect ratio of subplots using the `figsize=(12, 2)` argument.

## How to Run

Ensure `matplotlib` and `numpy` are installed. Run the script to generate and display the exercise plots sequentially.

```bash
python matplotlib_assignments.py
