# Day 11: Blackjack Capstone Project

## Project Overview
For this milestone, I built a fully functional, text-based Blackjack game. Instead of settling for the basic requirements, I challenged myself to implement three distinct deck management systems, making the game logic significantly more complex and realistic.

## Repository Structure
*   **`project.py`**: The main executable script containing the game logic, card drawing mechanics, and computer opponent AI.

## Key Features & Concepts
* **Dynamic Deck Modes:** The game allows the player to choose between an infinite deck, one deck per person, or a single shared deck, affecting how probability works as cards are removed.
* **Computer AI:** The dealer's decisions are not hardcoded but rely on a probability matrix using the `random` module to simulate realistic gambling risks.
* **List Manipulation:** Extensive use of list operations (`.append()`, `.remove()`) to track hands and active decks.

## How to Run
To start the Blackjack game, run the following command in your terminal:

    python project.py
