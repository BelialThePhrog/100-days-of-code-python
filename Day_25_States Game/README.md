# Day 25: Data Analysis with Pandas & U.S. States Game

## roject Overview
This directory contains two projects focusing on data manipulation, extraction, and graphical user interfaces:
1. **Central Park Squirrel Census Analysis:** A data analysis script leveraging the `pandas` library to parse a large dataset of squirrel sightings and aggregate them by primary fur color.
2. **U.S. States Game:** An interactive educational game built with `turtle` and `pandas`. The user must guess the names of all 50 US states within a 10-minute time limit. Correct guesses are dynamically mapped to their corresponding X/Y coordinates on a blank map.

##  Skills Demonstrated
*   **Vectorized Data Operations:** Replaced manual `for` loops with optimized `pandas` methods like `.value_counts()` for efficient data aggregation.
*   **Data I/O:** Reading from and writing to `.csv` files seamlessly using Pandas DataFrames.
*   **GUI Integration:** Combining graphical coordinate mapping (`turtle`) with tabular data lookups to place text dynamically on an image background.
*   **Event-Driven Programming:** Implementing asynchronous timers within the `turtle` main loop using `ontimer()`.

##  How to Run
*   **Squirrel Census:** Run `python squirrel_census.py`. It will read `Squirrel.csv` and generate a `squirrel_count.csv` summary file.
*   **U.S. States Game:** Run `python us_states_game.py`. Ensure `50_states.csv` and `blank_states_img.gif` are in the same directory.
