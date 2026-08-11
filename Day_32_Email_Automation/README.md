# Day 32: SMTP Email Automation & Datetime Module

## Project Overview

This module explores the fundamentals of backend automation by programmatically sending emails using Python. The objective is to understand how to connect to email servers via the Simple Mail Transfer Protocol (SMTP), secure the connection using TLS encryption, and schedule tasks based on the current day of the week using the `datetime` module.

> 🔒 **Security Notice:** The core project (Automated Birthday/Motivational Wisher) has been intentionally omitted from this public repository due to security protocols. Establishing a live SMTP connection requires embedding authentication credentials (such as Google App Passwords). To prevent sensitive data leaks, only the generalized practice script is provided to demonstrate the technical architecture.

## Skills Demonstrated

* **Protocol Communication (SMTP):** Utilizing Python's built-in `smtplib` to instantiate a connection object (`smtplib.SMTP("smtp.gmail.com")`) and route data through the correct port.
* **Network Security (TLS):** Implementing `starttls()` to upgrade an insecure connection to a secure one, encrypting the authentication payload (email and password) before it is transmitted over the network.
* **Temporal Logic (Datetime):** Leveraging the `datetime` module (`dt.datetime.now()`) to extract specific temporal attributes (like `weekday()`) to trigger conditional logic—e.g., executing a routine strictly on Tuesdays (index `1`).

## How to Run

Ensure the file (`smtp_practice.py`) is in the directory. You will need to replace the placeholder strings with a valid email and an *App Password* generated from your email provider's security settings.

```bash
python smtp_practice.py
