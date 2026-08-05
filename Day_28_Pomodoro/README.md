# Day 28: Dynamic Pomodoro Timer

## Project Overview

A robust desktop productivity application based on the Pomodoro Technique, built with Python's `tkinter` library. Unlike standard timers, this application features a custom dialog interface that dynamically calculates optimal work, short break, and long break intervals based on the user's total available time and desired cycle loops.

## Skills Demonstrated

* **Advanced Tkinter & Window Management:** Utilizing `Toplevel()` to create secondary pop-up dialogs for user configuration before initializing the main application loop, as well as manipulating window attributes (`window.lift()`, `-topmost`) to force the app to the foreground when a timer ends.
* **Dynamic Time Allocation Algorithm:** Implementing mathematical logic (`math.floor`, `round`) to proportionally divide total inputted time across 27-unit cycles to automatically generate balanced work and rest intervals.
* **Event-Driven Countdowns:** Leveraging Tkinter's `.after()` method to create a non-blocking, recursive countdown mechanism that updates the UI in real-time without freezing the main window.
* **User Validation & Alerts:** Using the `messagebox` module to implement robust input validation, catching invalid zero-time inputs and proactively warning the user if their settings would result in inefficiently short work sessions.

## Disclaimer & Credits

This project architecture was guided by the "100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu.

My core focus for this module was building the dynamic time allocation engine. I would like to acknowledge the use of AI as a collaborative tool to help me better understand and structure the mathematical logic required for dividing the total time and accurately matching the intervals to the Pomodoro cycle.

## How to Run

Ensure all files (`main.py`, `tomato.png`) are in the same directory and execute:

```bash
python main.py
