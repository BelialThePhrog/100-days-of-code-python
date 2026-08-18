# Day 38: Workout Tracking with NLP & Google Sheets

## Project Overview

An automated workout logging application that leverages Natural Language Processing (NLP) to parse plain English exercise descriptions and calculate caloric burn. The parsed data is then automatically pushed to a Google Sheet database via a REST API, acting as a cloud-based digital workout journal.

> 🔒 **Security Notice:** All API Keys (Nutritionix APP_ID, APP_KEY), Bearer Tokens, and personal Sheety Endpoints have been redacted from this repository and replaced with placeholders to maintain system security.

## Skills Demonstrated

* **Natural Language Processing (NLP) Integration:** Connected to an NLP-powered API to translate conversational inputs (e.g., "jog for 2 hours, swim for 3 hours") into structured numerical data (duration, calories, METs).
* **Bearer Token Authentication:** Implemented advanced HTTP Header authentication using a Bearer Token to securely authorize POST requests to the database API.
* **Third-Party Database Integration (Sheety):** Executed HTTP POST requests to automatically append new rows to a Google Spreadsheet, formatting datetime objects to match the required database schema.
* **Rate Limiting Handling:** Incorporated `time.sleep(3)` to artificially delay sequential API calls within loops, preventing server rejections due to rate-limit quotas[cite: 20].

## How to Run

Ensure the file (`workout_tracker.py`) is in the directory. You must configure your local environment variables or supply valid Nutritionix API credentials and your own Sheety endpoint.

```bash
python workout_tracker.py
