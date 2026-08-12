# Day 33: API Endpoints, JSON Parsing & Task Scheduling

## Project Overview

This module focuses on backend data fetching and background task automation. It integrates multiple live Application Programming Interfaces (APIs) to dynamically retrieve data—such as the real-time coordinates of the International Space Station (ISS) and localized sunrise/sunset hours. 

> 🔒 **Security Notice:** The core automated email notification feature has been omitted from this repository. Connecting to an SMTP server requires authentication payloads (e.g., App Passwords) which should never be exposed in public version control. The provided code includes a safe, templated structure for handling SMTP connections.

## Skills Demonstrated

* **REST API Integration:** Utilizing the `requests` module to execute HTTP GET requests against live endpoints (Open-Notify, Sunrise-Sunset, Kanye Rest).
* **JSON Data Processing:** Parsing complex, nested JSON responses to extract specific floats and integers (e.g., geographical coordinates, temporal data).
* **Advanced Automation:** Implementing the `apscheduler` library (`BlockingScheduler`) to run background polling routines at fixed intervals.
* **Error Handling & Status Codes:** Validating network responses dynamically using `response.raise_for_status()` to gracefully catch and handle HTTP anomalies.

## Disclaimer & Credits

This project architecture was guided by the "100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu.

My core focus was safely handling API responses, scheduling routines, and ensuring secure SMTP configuration structures. 

## How to Run

Ensure all files are in the same directory. The Kanye Quotes app requires the accompanying graphical assets (`background.png`, `kanye.png`).

To run the GUI app:
```bash
python kanye_quotes_app.py
