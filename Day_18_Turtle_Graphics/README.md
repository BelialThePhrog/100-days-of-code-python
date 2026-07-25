# Day 18: Turtle Graphics & Hirst Painting Generator

## Project Overview
This project focuses on manipulating the Graphical User Interface (GUI) using Python's built-in `turtle` module. The final script generates a piece of modern art (inspired by Damien Hirst's spot paintings) by extracting a color palette from an existing image and randomly drawing a grid of colored dots based on the window's spatial coordinates.

## Skills Demonstrated
*   **GUI Manipulation:** Setting up the screen, adjusting coordinates, and controlling the Turtle's state (speed, pen states, direction).
*   **External Packages:** Installing and utilizing the `colorgram.py` library to parse through image pixels and extract dominant RGB values.
*   **Data Structures (Tuples):** Extracting and storing RGB colors as immutable tuples to pass directly into the `turtle.color()` function.
*   **Logic & Loops:** Utilizing mathematical logic and modulo operators within loops to create an automated, perfectly spaced grid layout that adapts to screen dimensions.

## Disclaimer & Credits
The specific concepts for the challenges (drawing dashed lines, spirographs, and the Hirst Painting project) were provided by the **"100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu**. 

My implementation involved writing the automated drawing logic, handling the color extraction, and ensuring the grid correctly scales with the screen coordinates.

## How to Run
Ensure you have the `colorgram.py` package installed and an image named `sweet_pic.png` in the same directory:

    pip install colorgram.py
    python main.py
