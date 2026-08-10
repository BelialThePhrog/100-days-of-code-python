# Day 31: Flashcard Language Learning App

## Project Overview

A desktop flashcard application designed to help users learn French vocabulary. Built with Python's `tkinter` for the graphical interface and `pandas` for data management, the app features automated card flipping, progress tracking, and a streak system. Words that are mastered are dynamically moved out of the learning queue and saved to a separate database.

## Skills Demonstrated

* **Data Management with Pandas:** Reading from and writing to CSV files (`french_words.csv`, `known_words.csv`) and converting DataFrames to dictionaries (`to_dict(orient="records")`) for rapid iteration.
* **Canvas & Image Manipulation:** Using `tkinter.Canvas` to layer text over background images (`card_front.png`, `card_back.png`) and dynamically configuring canvas items to simulate a flashcard flip.
* **Event-Driven Timing:** Implementing the `window.after()` and `window.after_cancel()` methods to create non-blocking timers that automatically reveal the English translation after a set delay.
* **State Management & File I/O Logic:** Tracking user streaks using a custom Python dictionary. Once a word reaches a streak of 5, the app prompts the user and safely migrates the data between active and mastered CSV datasets.

## Disclaimer & Credits

This project architecture was guided by the "100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu. 

My core focus for this module was building the streak tracking system and handling data persistence. I would like to acknowledge the use of AI as a collaborative tool to help me better understand and implement the `should_move` logic within the Pass/Fail and file movement mechanics.

## How to Run

Ensure all graphical assets (`card_front.png`, `card_back.png`, `right.png`, `wrong.png`) and the dataset (`french_words.csv`) are in the same directory, then execute:

```bash
python flashcard_app.py
