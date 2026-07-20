# Day 13: Debugging 

## Project Overview
Day 13 is entirely focused on one of the most crucial skills in programming: debugging. Instead of building a new project from scratch, the objective was to read existing, broken code, understand the error messages (such as `SyntaxError`), identify logical flaws, and implement fixes.

## Repository Structure
*   **`practice.py`**: A collection of debugging exercises. The file contains the original broken code (commented out for reference) alongside the corrected, working versions.

## Key Concepts Covered
* **Error Handling:** Using `try` / `except ValueError` blocks to catch invalid user inputs and prevent the program from crashing.
* **Syntax Errors:** Catching common typos, such as using an assignment operator (`=`) when an equality operator (`==`) is required.
* **Logical Errors:** Fixing incorrect mathematical constants (e.g., using `4000` instead of `400` in leap year logic) and control flow (using `elif` instead of consecutive `if` statements to prevent multiple unintended outputs).
* **Code Tracing:** Mentally running through code line-by-line to find unexpected behavior, like in the classic FizzBuzz algorithm.

## How to Run
To review the debugging exercises:

    python practice.py
