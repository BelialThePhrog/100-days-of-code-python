# Capstone Project: Warframe Market Alert Club

## Project Overview

A custom-built, fully independent Object-Oriented application designed to track in-game item prices within the Warframe player-driven economy. This system orchestrates multiple APIs to monitor specific market thresholds and dispatch formatted HTML emails with ready-to-use in-game whisper commands when a deal is found. 

## 🤖 AI Collaboration & The Learning Journey

This project marks a significant departure from guided coursework into independent software architecture. I actively collaborated with AI to bridge knowledge gaps, heavily researching and iterating on the code to make the system robust. Key learning milestones included:
*   Understanding how to design a modular, multi-file OOP architecture (`main.py`, `data_manager.py`, `market_checker.py`, `notification_manager.py`).
*   Mastering the integration of multiple external systems (Sheety API for user/item databases, Warframe Market API for live trading data, and SMTP for alerts).

## System Architecture & Features

*   **Market Intelligence Engine:** Connects to the `api.warframe.market` endpoint to scrape live sell orders, dynamically filtering for sellers whose status is strictly "ingame" to ensure actionable alerts.
*   **Database Management (Sheety):** Utilizes Google Sheets as a backend via the Sheety API, handling user registration and tracking individual item price limits natively.
*   **Advanced HTML Email Generation:** Uses `email.mime.multipart` to construct responsive, styled HTML emails that present users with the exact `/w` chat command needed to copy-paste into the game client.
*   **Enterprise-Grade Security:** Employs the `dotenv` library to securely inject all SMTP credentials, Bearer tokens, and Sheety endpoints from the local environment, ensuring zero leakage in version control.

## How to Run

Ensure all modules are in the same directory and you have configured your `.env` file with your specific `SMTP_EMAIL`, `SMTP_PASSWORD`, and Sheety credentials.

```bash
python main.py
