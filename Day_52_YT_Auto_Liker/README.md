# Day 52: YouTube History Auto-Liker

## Project Overview

A custom-built, daily utility script designed to automate interactions on YouTube. The application utilizes Selenium WebDriver to parse a logged-in user's watch history and programmatically "likes" all videos watched that day, acting as an automated support mechanism for content creators.

## Skills Demonstrated

* **Advanced DOM Traversal:** Locating dynamically loaded web components (`ytd-item-section-renderer`) within a complex, modern single-page application.
* **JavaScript DOM Injection:** Executing custom JavaScript (`execute_script`) directly within the browser session to bypass standard viewport occlusion and "element intercepted" exceptions.
* **State Verification:** Extracting and evaluating ARIA attributes (`aria-pressed`) to verify the current state of UI elements, preventing the script from toggling off existing likes.
* **Custom Automation Tooling:** Architecting a practical, daily-use automation tool to solve a real-world workflow inefficiency.

## Disclaimer & Credits

This project diverges from the standard curriculum of the "100 Days of Code™: The Complete Python Pro Bootcamp". 

**Custom R&D & AI Collaboration:**  I actively collaborated with AI to conceptualize the tool and troubleshoot advanced DOM manipulation techniques, particularly the JavaScript injection required to interact with complex, nested UI elements.

## How to Run

Ensure the file (`youtube_liker.py`) is in your directory. To run this successfully, your Selenium WebDriver must be configured to use a specific Chrome user profile that is already authenticated with your Google account.

```bash
python youtube_liker.py
