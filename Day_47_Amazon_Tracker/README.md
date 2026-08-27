# Day 47: Amazon Price Tracker

## Project Overview

An automated web scraping application designed to monitor Amazon product prices. The script fetches the live HTML of a specific product page, parses the DOM to extract the current price, cleans the string data into a float, and triggers an SMTP email alert if the price drops below a user-defined threshold.

> 🔒 **Security Notice:** Email credentials and passwords have been removed from this script and replaced with placeholders to prevent accidental exposure.

## Skills Demonstrated

* **Advanced Web Scraping:** Using `requests` with custom HTTP headers (`User-Agent`, `Accept-Language`) to bypass basic bot-detection mechanisms on Amazon.
* **DOM Traversal & Data Cleaning:** Utilizing `BeautifulSoup` to target specific HTML IDs (`apex-pricetopay-accessibility-label`), and leveraging Python's `string` and `maketrans` methods to strip currency symbols and extract clean numerical values.
* **SMTP Email Automation:** Connecting to Gmail's SMTP server with TLS encryption to send automated, conditional alerts based on real-time scraped data.

## Disclaimer & Credits

The foundational concepts and core logic for this web scraping automation were inspired by the **"100 Days of Code™: The Complete Python Pro Bootcamp"** by Dr. Angela Yu.

My independent focus for this module was ensuring the script effectively bypasses basic scraper blocking via custom HTTP headers, cleanly parsing the strings into usable floats, and securely formatting the SMTP connection for real-time alerting.

## How to Run

Ensure the file (`amazon_tracker.py`) is in the directory. You will need to update the `my_email` and `password` variables with your actual credentials (use an App Password).

```bash
python amazon_tracker.py
