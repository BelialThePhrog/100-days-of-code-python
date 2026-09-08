# Day 58: Matplotlib Crash Course & Object-Oriented Plotting

## Project Overview

This module dives into data visualization using `matplotlib`. While `seaborn` and `pandas` will be primary tools moving forward, understanding the foundational `matplotlib` syntax—specifically its Object-Oriented (OO) API—is critical for fine-tuning charts, managing multiple axes, and controlling exact figure dimensions.

## Skills Demonstrated

* **Functional vs. OO Plotting:** Transitioning from simple `plt.plot()` functional calls to the more robust Object-Oriented approach using `plt.figure()` and `fig.add_axes()`.
* **Axes Positioning & Multiple Plots:** Manually defining plot dimensions and locations using list coordinates `[left, bottom, width, height]` to embed smaller charts within larger ones or place them side-by-side.
* **Figure Resizing:** Utilizing `plt.subplots(nrows, ncols, figsize)` to generate multi-plot grids and explicitly control the output resolution/size.
* **Styling & Aesthetics:** Customizing chart visuals including line colors (HEX codes), line styles (`ls="--"`), transparency (`alpha`), and marker properties (`marker="o"`, `markerfacecolor`).
* **Exporting Visuals:** Saving generated plots to the local directory using `fig.savefig()`.

## Disclaimer & Credits

**Custom Curriculum Path:** These exercises belong to the **"Python for Data Science and Machine Learning Bootcamp"**, continuing the pivot toward Data Analytics. 

## How to Run

Ensure `matplotlib` and `numpy` are installed in your environment (`pip install matplotlib numpy`).

```bash
python matplotlib_exercises.py
