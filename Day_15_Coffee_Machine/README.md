# Day 15: Virtual Coffee Machine

## Project Overview
This project simulates the internal software of a digital coffee machine. It is a comprehensive exercise in procedural programming, requiring continuous execution, resource management, and complex mathematical logic for handling monetary transactions.

## Repository Structure
*   **`project.py`**: The complete application script, handling user inputs, resource deduction, and calculating exact coin change.

## Key Concepts Covered
* **State Management:** Tracking and updating global variables (water, milk, coffee, money) as different drinks are ordered.
* **Algorithmic Thinking:** Implementing a greedy algorithm within the `payment` function to calculate the exact number of quarters, dimes, nickels, and pennies to return as change, while keeping track of the machine's coin inventory.
* **Data Structures:** Using lists of dictionaries to store the recipe requirements and costs for each type of coffee.
* **Continuous Execution:** Utilizing `while` loops to keep the machine running until a hidden maintenance command (`off`) is issued.

## How to Run
To boot up the coffee machine, run the following command in your terminal:

    python project.py

*(Hint: Type `report` to check current resources, or `off` to shut the machine down).*
