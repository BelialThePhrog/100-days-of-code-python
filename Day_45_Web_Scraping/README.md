# Day 45: Web Scraping with Beautiful Soup

## Project Overview

This module focuses on extracting and parsing data from HTML documents using the Beautiful Soup library. The capstone project involves scraping a historically archived webpage (Empire's 100 Greatest Movies) to generate a formatted text file containing a definitive watch list.

## Skills Demonstrated

* **HTML Parsing:** Utilizing `BeautifulSoup` to navigate the Document Object Model (DOM) of both local HTML files and live web responses[.
* **Data Extraction:** Targeting specific HTML elements using CSS selectors (`select_one`), tag names (`find_all`), and class attributes (`class_="title"`) to extract raw text and hyperlink references.
* **List Slicing & Filtering:** Reversing the scraped movie list using Python's slice notation (`[::-1]`) to order the movies from 1 to 100, and implementing conditional logic to filter out unwanted advertisement text ("Buy the film here").
* **File I/O Encoding:** Appending the parsed strings to a local `.txt` file while enforcing `utf-8` encoding to prevent Unicode errors with special characters.

## Disclaimer & Credits

The foundational concepts and initial HTML structures for this web scraping project were inspired by the **"100 Days of Code™: The Complete Python Pro Bootcamp"** by Dr. Angela Yu. 

My engineering focus in this module was to cleanly implement the data extraction logic, handle UTF-8 encoding requirements, and successfully traverse the archived DOM structure.

## How to Run

Ensure all files (`bs4_practice.py`, `empire_movies_scraper.py`, `website.html`) are in the same directory. 

To practice local HTML scraping:
```bash
python bs4_practice.py
```

To run the live web scraper and generate the Movies_to_watch.txt file:
```bash
python empire_movies_scraper.py
```
