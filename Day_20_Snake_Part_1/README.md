# Day 20: Snake Game (Part 1) - Animation & Coordinates

## Project Overview
This project is the first half of a fully functional, classic Snake arcade game built entirely with Python's `turtle` graphics library. Part 1 focuses on the foundational Object-Oriented Programming (OOP) architecture: generating the snake body, creating smooth animations, and mapping directional inputs to specific coordinate headings.

## Skills Demonstrated
*   **Object-Oriented Design:** Decoupling the game logic by separating the overarching screen setup (`main.py`) from the specific mechanics and state of the snake object (`snake.py`).
*   **Screen Animation:** Utilizing the `tracer()` and `update()` methods combined with `time.sleep()` to control the screen refresh rate, achieving seamless animation instead of watching individual graphic elements draw sequentially.
*   **Coordinate Manipulation:** Programming the snake's tail segments to dynamically follow the exact coordinates of the segment immediately preceding them, allowing for complex turning logic.
*   **Control Flow & Constraints:** Implementing conditional logic to prevent the snake from reversing directly into itself (e.g., ignoring a "Down" command if the current heading is "Up").

## Disclaimer & Credits
This project was built following the structure of the **"100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu**. 

My focus was on writing the class structures, implementing the directional constraint logic, and managing the refresh-rate animation loop.

## How to Run
Ensure both files are in the same directory and execute:

    python main.py
