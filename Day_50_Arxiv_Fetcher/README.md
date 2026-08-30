# Day 50: arXiv Academic Paper Fetcher

## Project Overview

A command-line interface (CLI) application designed to fetch and read the latest academic papers from the arXiv public API. The script provides an interactive menu to navigate through specific scientific disciplines (Computer Science, Physics, Mathematics) and automatically opens the selected research paper's PDF directly in the default web browser.

## Skills Demonstrated

* **XML API Parsing:** Transitioning from standard HTML scraping to parsing structured XML data from an open academic API using `BeautifulSoup` with the `xml` feature.
* **CLI Menu Engineering:** Building a dynamic, robust command-line menu system with input validation to prevent crashes from invalid user choices.
* **Standard Library Integration:** Utilizing the built-in `webbrowser` module to bridge the gap between terminal execution and the operating system's graphical interface.
* **Data Structuring:** Using nested Python dictionaries to map human-readable academic categories to specific arXiv taxonomy codes (e.g., `math.ST` for Statistics Theory).

## Disclaimer & Credits

The core concepts of API integration and data parsing were inspired by the **"100 Days of Code™: The Complete Python Pro Bootcamp"** by Dr. Angela Yu. 

**Custom Upgrades:** This project diverges entirely from the standard course curriculum. It was independently engineered to interface specifically with the arXiv API, utilizing custom XML parsing logic and dynamic CLI menus tailored for academic research.

## How to Run

Ensure the file (`arxiv_fetcher.py`) is in your directory and you have installed the required packages (`requests`, `beautifulsoup4`, `lxml`). 

```bash
python arxiv_fetcher.py
