# Day 22: Pong Arcade Game

## Project Overview
A fully functional recreation of the classic arcade game Pong, built entirely with Python and the `turtle` GUI module. This project expands on Object-Oriented Programming principles by managing multiple independent objects (paddles, ball, scoreboard) and introducing autonomous movement logic for the computer-controlled opponent.

## Skills Demonstrated
*   **Vector-Based Movement:** Simulating physics by updating X and Y coordinates dynamically within the game loop, and creating bounce mechanics by reversing coordinate vectors upon impact.
*   **Collision Detection (Hitboxes):** Tuning distance algorithms and coordinate constraints to accurately detect when the ball strikes a paddle or hits the top/bottom boundaries of the screen.
*   **Basic AI Implementation:** Writing autonomous control flow logic that allows the computer paddle to continuously track up and down the screen without user input.
*   **State Management:** Continuously tracking and updating a live scoreboard while managing the active state of the game loop based on win conditions.

## Disclaimer & Credits
This project was inspired by the **"100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu**. 

My focus was on decoupling the class modules, implementing the vector physics for the ball, tuning the hitboxes for the paddles, and writing the logic for the automated computer opponent.

## How to Run
Ensure all files (`main.py`, `paddle.py`, `ball.py`, `scoreboard.py`) are in the same directory and execute:

    python main.py
