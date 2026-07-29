# Day 23: Turtle Crossing (Frogger Clone)

## Project Overview
A custom take on the classic Frogger / Crossy Road arcade game built with Python's `turtle` module. The player controls a turtle that must navigate across a busy multi-lane highway. With each successful crossing, the game speed increases, requiring faster reflexes.

## Skills Demonstrated
*   **Object-Oriented Game Entities:** Managing multiple moving objects simultaneously by appending newly instantiated `CarManager` objects to a list and iterating through them within the main game loop.
*   **Bidirectional Spawning:** Implementing random choice logic to spawn cars from both the left and right sides of the screen, dynamically assigning their movement vectors based on their spawn coordinates.
*   **Dynamic RGB Colors:** Utilizing `turtle.colormode(255)` and the `random` module to generate completely random RGB values for every spawned car, rather than relying on a hardcoded list of strings.
*   **Difficulty Scaling:** Manipulating the `time.sleep()` parameter upon leveling up to increase the frame rate, thereby speeding up all obstacles and increasing the difficulty.

## Disclaimer & Credits
This project architecture was guided by the **"100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu**. 

My core focus was on implementing the randomized bidirectional car spawning, adjusting the collision hitboxes, and writing the dynamic difficulty scaling logic.

## How to Run
Ensure all files (`main.py`, `player.py`, `car_manager.py`, `scoreboard.py`) are in the same directory and execute:

    python main.py
