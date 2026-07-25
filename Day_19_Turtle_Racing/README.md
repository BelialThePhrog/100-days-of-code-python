# Day 19: Instances, State, and Higher-Order Functions

## Project Overview
This module explores advanced Graphical User Interface (GUI) concepts in Python using the `turtle` package. The main project is a **Turtle Racing Game** where the user places a bet on a colored turtle, and multiple independent turtle objects race across the screen using randomized movement logic. 

A secondary practice script includes an Etch-A-Sketch application built to demonstrate keyboard event binding.

## Skills Demonstrated
*   **Event Listeners:** Binding keystrokes to specific functions using `screen.listen()` and `screen.onkey()` to create interactive desktop applications.
*   **Higher-Order Functions:** Passing functions as arguments to other functions.
*   **Object State & Instantiation:** Generating multiple unique object instances from the same class, managing their individual states (color, position), and storing them dynamically in lists for iteration.
*   **GUI User Input:** Utilizing pop-up dialogs (`textinput`, `numinput`) to safely capture user constraints before executing the main application loop.

## Disclaimer & Credits
The core concepts for these projects (Etch-A-Sketch controls and the Turtle Racing premise) were introduced in the **"100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu**. 

My focus was on writing the logic that dynamically aligns the objects on the starting line based on user input, tracks their independent coordinates (`x > 150`), and triggers the endgame sequence.

## Repository Structure
*   **`main.py`**: The Turtle Racing Game. Run this to place your bet and watch the instances race.
*   **`practice.py`**: The Etch-A-Sketch app. Use W, A, S, D to draw, and 'R' to clear the screen.
