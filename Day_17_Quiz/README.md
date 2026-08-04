# Day 17: OOP Quiz Game

## Project Overview
This project is a text-based True/False Quiz Game built entirely using Object-Oriented Programming (OOP) principles. It demonstrates how to create custom classes, initialize objects, and manage the internal state of an application across multiple modular files.

## Disclaimer & Credits
The trivia questions and answers stored in `data.py` were provided by the **"100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu**. 

My core objective for this project was to build the OOP architecture from scratch, specifically designing the `Question` model and the `QuizBrain` logic to dynamically process whichever data list is passed into it.

## Repository Structure
*   **`main.py`**: The execution script that initializes the question bank and runs the main game loop.
*   **`quiz_brain.py`**: Contains the `QuizBrain` class, which handles the core game mechanics (tracking the score, asking questions, and validating answers).
*   **`question_model.py`**: Contains the `Question` class, serving as a blueprint for creating individual question objects.
*   **`data.py`**: Contains the raw list of trivia dictionaries (Provided by course).

## Disclaimer & Credits

This project architecture was guided by the "100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu.

## How to Run
To start the quiz, execute the following command in your terminal:

    python main.py
