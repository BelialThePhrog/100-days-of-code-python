# Day 49: Pracuj.pl Job Search Automator

## Project Overview

An automated web scraping script designed to navigate the Polish job portal Pracuj.pl[cite: 19]. It dynamically constructs search URLs based on user input (job title and location) and utilizes advanced browser automation to bypass cookie banners and wait for asynchronous job listings to load.

## Skills Demonstrated

* **URL Encoding:** Using the `urllib.parse` library to safely encode user inputs directly into the URL structure, bypassing the need to interact with fragile frontend search forms.
* **Explicit Waits (UI Module):** Implementing `WebDriverWait` and `expected_conditions` from `selenium.webdriver.support.ui` to pause execution until specific DOM elements (like the cookie banner or results container) become interactive or present.
* **Robust Error Handling:** Wrapping element locators in `try/except` blocks with a fallback candidate list (XPath and ID combinations) to handle dynamically changing cookie consent modals.

## Disclaimer & Credits

The foundation for web scraping and browser automation was inspired by the **"100 Days of Code™: The Complete Python Pro Bootcamp"** by Dr. Angela Yu. 

**Custom Upgrades & AI Collaboration:** I heavily customized this module to target a local job board. I explicitly acknowledge utilizing AI as an engineering partner to architect the robust web scraping logic-specifically mastering the `selenium.webdriver.support.ui` module to handle asynchronous page rendering and dynamic cookie popups without causing script-breaking timeouts.

## How to Run

Ensure the file (`job_scraper.py`) is in the directory and you have the `undetected_chromedriver` package installed.

```bash
python job_scraper.py
