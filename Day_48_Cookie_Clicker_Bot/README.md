# Day 48: Selenium Webdriver & Cookie Clicker Automation

## Project Overview

An automated browser bot designed to play the web-based game "Cookie Clicker" using Selenium WebDriver. The script programmatically interacts with the DOM to click the main cookie element and automatically purchase the most expensive available upgrades within a defined time limit. 

## Skills Demonstrated

* **Browser Automation:** Instantiating and controlling a live Chrome browser session using Python.
* **Bot Detection Evasion:** Utilizing the `undetected_chromedriver` package to bypass standard browser fingerprinting and anti-bot protections.
* **DOM Element Interaction:** Locating HTML elements using `By.ID` for the main cookie and `By.CSS_SELECTOR` (`.product.enabled`) to identify dynamically changing upgrade buttons.
* **Time Management & Loop Control:** Implementing a `time.time()` check to enforce a strict 600-second (10-minute) execution limit while batching 100 clicks per upgrade check cycle.

## Disclaimer & Credits

The core concepts of Selenium browser automation and the objective to automate Cookie Clicker were inspired by the **"100 Days of Code™: The Complete Python Pro Bootcamp"** by Dr. Angela Yu. 

My specific implementation incorporates the external `undetected_chromedriver` library to ensure the browser does not get flagged or blocked by modern web protections during execution.

## How to Run

Ensure the file (`cookie_bot.py`) is in your directory and you have installed the required packages (`selenium`, `undetected_chromedriver`). 

```bash
python cookie_bot.py
