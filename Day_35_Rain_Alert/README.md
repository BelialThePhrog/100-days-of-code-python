# Day 35: Rain Alert App & API Authentication

## Project Overview

A weather monitoring script designed to fetch meteorological data from the OpenWeatherMap API and trigger an automated email alert if rain is forecasted. This project introduces API authentication mechanisms, passing parameters securely, and parsing complex JSON forecast data to drive conditional automation.

> 🔒 **Security Notice:** API Keys and SMTP credentials have been deliberately removed from this repository. Storing authentication keys in version control is a critical security vulnerability. 

## Skills Demonstrated

* **API Authentication:** Utilizing unique API keys to authenticate requests and access secured endpoints on third-party servers.
* **HTTP Request Parameters:** Structuring API queries using the `params` dictionary in the `requests` module to pass geographical coordinates (Latitude/Longitude) and authorization tokens cleanly.
* **JSON Traversal:** Navigating multi-level JSON structures (lists within dictionaries) to extract specific nested data points (e.g., condition codes).
* **Conditional Automation:** Combining real-time data evaluation (checking if weather condition codes indicate rain) with backend SMTP actions to create an event-driven alert system.

## Disclaimer & Credits

This project architecture was guided by the "100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu.

My core focus was setting up the API authentication and integrating the JSON parsing logic with my existing SMTP notification structure.

## How to Run

Ensure the file (`rain_alert.py`) is in the directory. You must supply your own OpenWeatherMap API key and configure the SMTP credentials locally.

```bash
python rain_alert.py
