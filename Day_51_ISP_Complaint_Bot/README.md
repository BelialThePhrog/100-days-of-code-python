# Day 51: Internet Speed Complaint Automator

## Project Overview

An automated diagnostic script that uses Selenium WebDriver to autonomously run an internet speed test on Speedtest.net. If the scraped download or upload speeds fall below the ISP's promised thresholds, the script automatically composes and dispatches a formal complaint email to the provider via SMTP.

## Skills Demonstrated

* **Advanced Browser Automation:** Using Selenium to navigate dynamic web pages, locate specific interactive elements (`By.CSS_SELECTOR`), and execute clicks on non-standard UI components.
* **Execution Delays & Synchronization:** Implementing strategic `time.sleep()` pauses to allow the browser to fully load external widgets and wait for the minute-long speed test to conclude before attempting data extraction.
* **Data Extraction & Type Casting:** Scraping live dynamic text elements from the DOM and casting them into Python `float` variables for mathematical comparison against threshold values.
* **Secure SMTP Communication:** Accessing environment variables (`os.environ.get`) to securely pass App Passwords for TLS-encrypted email dispatch via the `smtplib` library.

## Disclaimer & Credits

The core concept of automating the Speedtest.net website was inspired by the **"100 Days of Code™: The Complete Python Pro Bootcamp"** by Dr. Angela Yu. 

**Custom Upgrades:** The original course curriculum directs students to build a Twitter/X bot to publicly complain to ISPs. I engineered this project to trigger direct, professional email communications via Gmail's SMTP server instead, making it a more practical tool for actual customer service interactions.

## How to Run

Ensure the file (`speed_complaint_bot.py`) is in your directory. You must set your `GMAIL_APP_PASSWORD` as an environment variable before running the script to avoid `535 Authentication` errors.

```bash
python speed_complaint_bot.py
