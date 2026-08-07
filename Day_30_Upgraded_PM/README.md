# Day 30: Password Manager Pro (JSON & Exceptions)

## Project Overview

An advanced iteration of the Local Password Manager. This version upgrades the flat-file storage system to a structured JSON database, enabling fast, dictionary-based credential searches. Additionally, it introduces robust error handling to prevent application crashes during file I/O operations.

## Skills Demonstrated

* **JSON Data Handling:** Transitioning from plain text to JSON (`json.dump`, `json.load`) for structured, hierarchical data storage and seamless Python dictionary integration.
* **Advanced Exception Handling:** Implementing full `try / except / else / finally` blocks to elegantly handle edge cases, such as a missing database file (`FileNotFoundError`), ensuring uninterrupted UX.
* **Search Algorithms:** Engineering a search feature that parses the JSON dictionary to instantly retrieve and display stored emails and passwords for a requested website via UI pop-ups (`messagebox`).
* **UI Resilience:** Clearing entry fields dynamically and verifying user inputs (e.g., catching empty strings) before allowing database updates.

## Disclaimer & Credits

This project architecture was guided by the "100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu. 

My core focus for this module was independently integrating the JSON architecture with the existing Tkinter UI and engineering the search functionality to provide a complete, crash-resistant desktop application.

## How to Run

Ensure all files (`password_manager_pro.py`, `logo.png`) are in the same directory and execute:

```bash
python password_manager_pro.py
