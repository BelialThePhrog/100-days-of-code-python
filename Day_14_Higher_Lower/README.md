# Day 14: Higher Lower Game (Beginner Section Final Project)

## Project Overview
This project marks the conclusion of the Beginner Section! It is a terminal-based "Higher Lower" game where the player must guess which of two randomly selected celebrities or brands has a larger Instagram following. 

## Repository Structure
*   **`project.py`**: The complete game logic, including data dictionaries, ASCII art integration, error handling, and a custom high-score leaderboard.

## Key Concepts Covered
* **Complex Data Structures:** Utilizing a list of dictionaries to store and retrieve multiple attributes (name, follower count, description, country) for each entity.
* **Custom Sorting Algorithm:** Instead of relying on Python's built-in `.sort()` method, the leaderboard features a manually implemented Bubble Sort algorithm to rank players by their scores.
* **Input Validation:** Implementing `try/except ValueError` blocks to ensure the user inputs valid menu options ('A' or 'B') without crashing the script.
* **Game State Management:** Using nested `while` loops and boolean flags to handle continuous gameplay and replayability.

*Note: The console clearing feature uses `IPython.display`, which is specifically optimized for running within Jupyter Notebook environments.*

## How to Run
To play the Higher Lower game, run the following command (best experienced in a Jupyter Notebook environment):

    python project.py
