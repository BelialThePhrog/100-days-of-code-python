# Day 24: Local File I/O & Persistent Data

## Project Overview
This day focuses on one of the most critical aspects of software development: persistent data storage. The exercises are split into two parts:
1. **Snake Game Improvements:** Upgrading the classic Snake game to store and retrieve an all-time High Score locally, ensuring the record persists even after the game is closed.
2. **Mail Merge Automation:** A practical script that reads a list of names from a `.txt` file and automatically generates personalized invitation text files for each person.

## Skills Demonstrated
*   **File I/O Operations:** Utilizing Python's built-in `open()`, `read()`, `write()`, and `readlines()` methods to manipulate text files.
*   **Context Managers:** Using the `with open(...) as file:` syntax to ensure memory-safe file handling and automatic resource cleanup.
*   **State Persistence:** Decoupling the game's temporary state (current score) from its persistent state (high score stored in `data.txt`), and writing logic to compare and overwrite these values dynamically.
*   **String Manipulation & Automation:** Iterating through file data (`splitlines()`), dynamically formatting strings, and generating multiple discrete output files algorithmically.

## How to Run
*   **Snake Game:** Run `python main.py` (Ensure `data.txt` contains a single integer, e.g., `0`, before the first run).
*   **Mail Merge:** Run `python mail_merge.py` (Ensure `names.txt` exists in the directory).
