# Day 34: Quizzler - API Trivia App

## Project Overview

An Object-Oriented Graphical User Interface (GUI) quiz application that fetches real-time trivia questions from the Open Trivia Database (OpenTDB) API. The application dynamically parses the JSON payload, unescapes HTML characters, and evaluates user inputs (True/False) providing immediate visual feedback via Tkinter canvas color changes.

## Skills Demonstrated

* **Advanced OOP Architecture:** Structuring the application into highly cohesive, decoupled modules (`ui.py`, `quiz_brain.py`, `data.py`, `question_model.py`) to enforce the Single Responsibility Principle.
* **API Integration & Data Parsing:** Utilizing the `requests` library to connect to the OpenTDB REST API, fetching medium-difficulty boolean questions, and processing the JSON response dynamically.
* **Type Hinting & HTML Unescaping:** Enforcing Python type hints (e.g., `user_answer: str -> bool`) for robust code and utilizing the `html` module to clean up API text containing HTML entities (like `&quot;`).
* **Asynchronous UI Feedback:** Leveraging Tkinter's `window.after()` method to create non-blocking delays for visual PASS/FAIL feedback (green/red canvas flashes) before loading the next question.

## Disclaimer & Credits

This project architecture was guided by the "100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu. 

My core focus for this module was mastering API integration within an OOP framework. I would also like to acknowledge the use of AI as a collaborative tool to help me refine the PASS / FAIL logic evaluation and structure the dynamic feedback mechanics within the application.

## How to Run

Ensure all modules (`main.py`, `ui.py`, `quiz_brain.py`, `data.py`, `question_model.py`) and assets (`true.png`, `false.png`) are in the same directory and execute:

```bash
python main.py
