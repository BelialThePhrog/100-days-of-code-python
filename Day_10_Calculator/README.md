# Day 10: Functions with Outputs & Practical Debugging

## Project Overview
Day 10 of the "100 Days of Code" challenge focuses on mastering functions with return values. This directory contains the raw development process, documenting both successful implementations and the active debugging of errors encountered during practice.

## Learning Journey & Code Progression
The workflow is captured directly in the Jupyter Notebook (`Day_10_Calc.ipynb`), showcasing incremental progress:

1. **Basic Return Values:** Initial experimentation with returning simple expressions from functions.
2. **String Formatting & Syntax Debugging:** 
   * *The Challenge:* Encountered a `SyntaxError` while testing conditional checks on user input (`if name or surname ==`).
   * *The Fix:* Refactored the control flow to properly validate empty inputs using standard logical operators.
3. **Leap Year Logic:** Implemented nested conditions to evaluate leap years based on calendar rules.
4. **The Capstone: CLI Calculator:** Built a fully interactive command-line calculator capable of chaining operations on a continuously updating result.

## Key Concepts Practiced
* **Functions with Outputs:** Utilizing the `return` keyword to pass data back to the global scope.
* **Error Analysis:** Actively interpreting Python stack traces (like `SyntaxError`) to fix broken logic during live practice.
* **While Loops & Flag Variables:** Managing execution states for continuous user interaction.

## How to Run the Notebook
To see the step-by-step execution, including the standard output and error flags from the practice environment:
```bash
pip install notebook
jupyter notebook Day_10_Calc.ipynb
