# Day 27: Graphical User Interfaces (GUI) with Tkinter

## Project Overview

A practical desktop application that converts distances from miles to kilometers. Built using Python's built-in `tkinter` library, the script efficiently captures user input and dynamically updates the UI with mathematical conversions, making it a perfect exercise in event-driven programming and widget management.

## Skills Demonstrated

* **Tkinter Basics & UI Setup:** Creating windows, configuring dimensions (padding, sizing), and setting up the main event loop (`mainloop()`) to keep the application active and responsive.
* **Widget Placement (Grid Layout):** Utilizing the `grid()` geometry manager to precisely align `Label`, `Entry`, and `Button` widgets in a structured, matrix-like layout, avoiding the less predictable `pack()` method.
* **Event-Driven Programming:** Binding a button click to a custom Python function (`command=button_clicked`) to execute data extraction (`get()`) and dynamically update UI text elements based on real-time user input.
* **Exception Handling & Data Validation:** Implementing `try/except` blocks to catch `ValueError` exceptions when a user inputs non-numeric characters, ensuring the application handles edge cases gracefully without crashing.

## Disclaimer & Credits

This project architecture was guided by the "100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu.

My core focus was on mastering the `grid` placement system over standard packing, implementing robust exception handling for user inputs, and separating raw learning snippets into a standalone practice module.

## How to Run

Ensure all files (`mile_to_km_converter.py`, `tkinter_practice.py`) are in the same directory and execute:

```bash
python mile_to_km_converter.py
