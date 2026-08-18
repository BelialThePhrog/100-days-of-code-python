# Day 36: Stock Trading Alert Application

## Project Overview

An automated financial monitoring script that tracks daily stock price fluctuations for a given ticker (e.g., MSFT) using the Alpha Vantage API. If the stock experiences a significant price movement, the application automatically triggers an SMTP email alert detailing the percentage change. 

## Skills Demonstrated

* **Environment Variables for Security:** Implemented `os.environ.get()` to securely load sensitive credentials (App Passwords) from the local operating system, preventing accidental exposure in version control.
* **Financial API Integration:** Connected to the Alpha Vantage REST API to fetch daily time-series data for stock market analysis[cite: 18].
* **Complex Data Extraction:** Programmatically accessed dynamically changing JSON keys (dates) by casting dictionary keys into a list (`list(time_series.keys())`) to consistently retrieve the most recent trading days[cite: 18].
* **Context Management:** Used the `with smtplib.SMTP(...) as connection:` context manager to ensure network connections are safely and automatically closed after execution, preventing resource leaks[cite: 18].

## Disclaimer & Credits

This project architecture was guided by the "100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu.

## How to Run

Ensure the file (`stock_alert.py`) is in the directory. You must configure your local environment variables (`GMAIL_APP_PASSWORD`) and supply a valid Alpha Vantage API key.

```bash
python stock_alert.py
