# Day 54: Flask Web Server & Python Decorators

## Project Overview

This module marks the official entry into backend web development using the Flask framework. The exercises focus on establishing a local web server, defining route handlers, and mastering advanced Python concepts—specifically, creating custom decorators to modify function behavior at runtime.

## Skills Demonstrated

* **Backend Web Development:** Initializing a Flask application instance and utilizing route decorators (`@app.route`) to bind specific URL endpoints to Python functions.
* **Advanced Python Functions:** Utilizing first-class functions to create the `@speed_calc_decorator`, a wrapper that intercepts function calls to measure their execution time using the `time` module.
* **Performance Profiling:** Measuring execution differentials between computationally light and heavy loops (1,000 vs. 10,000 iterations) to understand runtime scaling.

## Disclaimer & Credits

The foundational concepts for backend development with Flask and the decorator exercises were sourced from the **"100 Days of Code™: The Complete Python Pro Bootcamp"** by Dr. Angela Yu. 

## How to Run

Ensure `Flask` is installed in your environment (`pip install Flask`). You will need two separate terminal instances or to run these scripts sequentially.

To run the Flask server:
```bash
python server.py
