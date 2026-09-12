# Day 63: Geographical Plotting with Plotly Choropleth Maps

## Project Overview
This module explores geographic data visualization using Plotly's offline engine and `graph_objs.Figure`. It covers the creation of choropleth maps across both national and global scales, mapping quantitative indicators such as GDP, agricultural export values, and energy consumption to geopolitical boundaries.

## Implemented Workflows

### 1. Practice (`choropleth_maps_practice.py`)
* **US State-Level Prototyping:** Constructs a baseline map using state postal abbreviations (`USA-states`) with predefined palettes (e.g., `'Greens'`).
* **Agricultural Exports Analysis:** Maps US agricultural commodities by state using `2011_US_AGRI_Exports`, adding custom borders (`marker.line`), lake fills (`lakecolor`), and the `'portland'` color scale.
* **Global GDP Mapping:** Uses `2014_World_GDP` with 3-letter ISO country codes (`CODE`) and the `'bonne'` geographic projection to plot worldwide economic output.

### 2. Exercises (`choropleth_maps_exercise.py`)
* **Global Power Consumption:** Visualizes worldwide electricity consumption (`Power Consumption KWH`) from `2014_World_Power_Consumption` using standard country names (`locationmode='country names'`).
* **2012 US Election Analysis:** Analyzes state-level voting demographics (`Voting-Age Population (VAP)`) from `2012_Election_Data` with customized color bars and white boundary lines.

## Requirements & Execution
Ensure all dependencies and local data files are available in the working directory:

```bash
pip install plotly chart-studio pandas
python choropleth_maps_practice.py
python choropleth_maps_exercise.py
