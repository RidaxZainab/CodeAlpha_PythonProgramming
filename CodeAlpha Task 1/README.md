# CodeAlpha Internship - Task 1: Hangman Game

This repository contains **Task 1: Hangman Game**, developed as a part of my Python Programming Internship at CodeAlpha

## 📌 Project Overview
The objective of this project is to create a classic, text-based Hangman game where the user attempts to guess a randomly selected secret word one letter at a time

To comply with the project parameters, the game avoids complex graphics or external audio streams, focusing purely on clean console input/output operations and core algorithmic logic

## 🛠️ Project Constraints & Features
* **Predefined Vocabulary:** The program utilizes a localized, predefined array of exactly 5 words, eliminating the dependencies for external file handling or API connections
* **Attempt Counter:** The user is restricted to a maximum of 6 incorrect guesses before the game concludes
* **Input Validation:** The script includes robust checks to filter out numeric values, special characters, multi-letter inputs, or duplicate guesses.
* **Dynamic Score Tracking:** Converts user inputs to uppercase dynamically to avoid case-sensitivity bugs and outputs the hidden word status clearly after each attempt.

## 💻 Key Python Concepts Covered
* **Random Module:** Utilizing `random.choice()` for secure word selection
* **Control Flow Loops:** Managing game states with interactive `while` loops
* **Conditional Logic:** Processing system input variations via nested `if-elif-else` structures
* **Data Collections:** Handling mutating state profiles using Python strings and lists

