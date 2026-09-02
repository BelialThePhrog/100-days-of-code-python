# Day 53: Zillow Data Entry Automation

## Project Overview

An automated data entry bot combining web scraping and browser automation. It parses rental property listings from Zillow based on user-defined parameters (location, price thresholds) and autonomously populates a Google Form with the extracted addresses, prices, and property URLs.

## Skills Demonstrated

* **Anti-Bot Evasion:** Injecting custom `User-Agent` strings and language headers into the Chrome WebDriver to bypass basic automated traffic blocks.
* **Dynamic DOM Scraping:** Utilizing a combination of CSS Selectors and XPath traversing (`./ancestor::div`) to reliably extract data from heavily nested, JavaScript-rendered UI cards.
* **Automated Data Entry:** Iterating through scraped datasets to systematically fill and submit external Google Forms using explicit `WebDriverWait` conditions.
* **Driver Management:** Implementing `webdriver_manager` to automatically handle binary dependencies for the Chrome browser

## Disclaimer & AI Acknowledgement

I utilized AI as a collaborative thought partner to help engineer the complex XPath selectors and manage the dual-navigation logic required to switch between Zillow and Google Forms. 

**Critical Note on Zillow Scraping:** Real estate platforms like Zillow constantly update their DOM structures, obfuscate CSS classes, and aggressively deploy anti-bot CAPTCHA mechanisms. While this script currently bypasses protections using custom headers, there is absolutely no guarantee it will work in the long run without continuous structural maintenance. 

## How to Run

Ensure the file (`zillow_scraper.py`) is in your directory and you have installed the required packages (`selenium`, `webdriver_manager`). 

```bash
python zillow_scraper.py
