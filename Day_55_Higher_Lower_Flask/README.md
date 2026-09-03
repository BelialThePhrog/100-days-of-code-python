# Day 55: HTML Parsing & Flask URL Routes

## Project Overview

This module expands on backend routing by parsing dynamic variables directly from the URL and rendering inline HTML elements from the server. The exercises culminate in a web-based "Higher or Lower" guessing game, where the user inputs their guess via the URL path.

## Skills Demonstrated

* **Dynamic URL Routing:** Utilizing Flask's variable rules (`<name>` and `<int:number_1>`) to capture user input directly from the web address.
* **Advanced Decorators:** Creating a custom `@make_bold` wrapper function that dynamically injects HTML formatting (`<b>`) around the returned strings of route functions.
* **HTML Rendering in Python:** Returning concatenated HTML strings, including paragraphs (`<p>`) and external media (`<img>` with a Giphy source), directly from backend endpoints.
* **Stateful Logic:** Generating a randomized target number upon server initialization (`random.randint(0,9)`) and evaluating conditional logic against user-provided URL parameters.

## Disclaimer & Credits

The foundational concepts for these Flask routing exercises and the "Higher or Lower" URL game were sourced from the **"100 Days of Code™: The Complete Python Pro Bootcamp"** by Dr. Angela Yu.

## How to Run

Ensure `Flask` is installed in your environment. You will need to run these scripts sequentially to avoid port conflicts on `localhost:5000`.

To run the HTML rendering and decorator practice:
```bash
python flask_practice.py
```
To run the Higher or Lower game:
```bash
python higher_lower.py
