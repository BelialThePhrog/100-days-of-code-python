# Day 21: Snake Game (Part 2) - Inheritance & Collision

## Project Overview
This project concludes the development of the classic Snake arcade game. Building upon the movement and animation mechanics established in Part 1, this phase introduces full game logic: spawning interactive food, maintaining a live scoreboard, and implementing strict collision detection for both the screen boundaries and the snake's own tail.

## Skills Demonstrated
*   **Class Inheritance:** Creating `Scoreboard` and `Food` classes that directly inherit from the built-in `Turtle` class using `super().__init__()`, inheriting its properties while adding custom behaviors.
*   **Collision Detection:** Using mathematical distance logic (`distance()`) and coordinate thresholds (`xcor()`, `ycor()`) to trigger events such as eating food or ending the game on boundary impact.
*   **List Slicing:** Utilizing Python's list slicing (`snake.segments[1:]`) to elegantly iterate through the snake's tail elements while intentionally excluding the head to prevent false-positive collision triggers.
*   **State Management:** Dynamic updating of the scoreboard UI and extending the snake's object array continuously as the game progresses.

## Disclaimer & Credits
This project architecture was guided by the **"100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu**. 

My core focus was on implementing the inheritance structures correctly and fine-tuning the mathematical thresholds that dictate when a collision event resolves.

## How to Run
Ensure all modular files (`main.py`, `snake.py`, `food.py`, `scoreboard.py`) are located in the same directory, then execute:

    python main.py
