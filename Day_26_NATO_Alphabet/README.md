# Day 26: NATO Phonetic Alphabet & Comprehensions

## Project Overview

A practical console application that translates any given word or name into the NATO Phonetic Alphabet. Built using Python's `pandas` library, the script efficiently parses a CSV dataset and maps user input to standardized phonetic codes, making it a perfect exercise in data iteration and error handling.

## Skills Demonstrated

* **Dictionary Comprehensions & Pandas Iteration:** Optimizing data lookups by iterating over a DataFrame with `iterrows()` to generate a hash map (Python dictionary), drastically improving lookup speed to O(1) time complexity.
* **List Comprehensions:** Dynamically generating lists from user string inputs to create the final phonetic translation array in a single, readable line of code.
* **Exception Handling & Data Validation:** Implementing `try/except` blocks to catch `KeyError` exceptions when a user inputs non-alphabet characters (like numbers or spaces), and `FileNotFoundError` to gracefully handle missing dataset files.

## Disclaimer & Credits

This project architecture was guided by the "100 Days of Code™: The Complete Python Pro Bootcamp" by Angela Yu.

My core focus was on optimizing the DataFrame iteration process using dictionary comprehensions instead of slow row-by-row filtering, implementing robust exception handling for edge cases, and separating learning snippets into a standalone practice module.

## How to Run

Ensure all files (`main.py`, `comprehensions_practice.py`, `nato_phonetic_alphabet.csv`) are in the same directory and execute:

```bash
python main.py
