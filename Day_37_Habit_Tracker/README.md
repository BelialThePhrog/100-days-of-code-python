# Day 37: Pixela Habit Tracker (API POST, PUT, DELETE)

## Project Overview

A console-based habit tracking application that integrates with the Pixela API. This project goes beyond simple data retrieval by implementing advanced HTTP methods to create, update, and delete daily habit data (e.g., hours spent coding) on a live, interactive graph.

> 🔒 **Security Notice:** The Pixela API Token and Username have been replaced with environment variables/placeholders in this repository to prevent unauthorized access to the graph.

## Skills Demonstrated

* **Advanced HTTP Methods:** Utilizing `requests.post()`, `requests.put()`, and `requests.delete()` to push new data, modify existing entries, and remove records from the external database.
* **API Header Authentication:** Securely authenticating API calls by passing the token via HTTP Headers (`"X-USER-TOKEN"`) rather than exposing it in the URL parameters.
* **Datetime Formatting:** Leveraging the `datetime` module and `.strftime("%Y%m%d")` to format user-inputted dates into the exact string structure required by the Pixela API.
* **Interactive CLI Flow:** Building a dynamic console menu that routes the user's choice to the appropriate API endpoint and operational logic.

## Disclaimer & Credits

This project architecture was guided by the "100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu.

## How to Run

Ensure the file (`habit_tracker.py`) is in the directory. You must supply your own Pixela Username, Token, and Graph ID.

```bash
python habit_tracker.py
