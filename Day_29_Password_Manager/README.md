# Day 29: Local Password Manager & Generator

## Project Overview

A fully functional, locally hosted Password Manager built with Python's `tkinter` GUI framework. While the initial architecture was inspired by the "100 Days of Code™" bootcamp, the core logic, UI integration, and file handling mechanisms were independently engineered. The application allows users to generate cryptographically strong passwords, bind them to specific websites and emails, and persistently store them in a local text database[cite: 6, 7].

## Skills Demonstrated

* **Advanced GUI Management:** Utilizing `tkinter.Canvas` to embed custom branding (`logo.png`) and leveraging advanced `grid()` parameters like `columnspan` and `sticky="EW"` to create a responsive, cleanly aligned interface.
* **Algorithmic Password Generation:** Engineering a custom randomization function using the `random` module to generate a 30-character string (combining 20 letters, 5 numbers, and 5 special symbols), followed by a programmatic `shuffle` for maximum entropy[cite: 6].
* **Clipboard Automation:** Integrating `window.clipboard_clear()` and `window.clipboard_append()` to seamlessly copy newly generated passwords to the user's system clipboard for immediate use[cite: 6].
* **Persistent File I/O:** Implementing standard context managers (`with open()`) in append mode (`mode="a"`) to securely dump user credentials into a flat `data.txt` file, structured with pipe (`|`) delimiters[cite: 6, 7].

## How to Run

Ensure all files (`password_manager.py`, `logo.png`) are in the same directory and execute:

```bash
python password_manager.py
