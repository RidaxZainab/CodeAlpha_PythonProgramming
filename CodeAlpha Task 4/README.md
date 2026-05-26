# CodeAlpha Internship - Task 4: Basic Chatbot

This repository contains **Task 4: Basic Chatbot**, developed as a part of my Python Programming Internship at CodeAlpha.

## 📌 Project Overview
The objective of this project is to build a simple, rule-based conversational assistant in Python. The chatbot interacts with users through the command-line interface, matching specific textual patterns to instantly deliver pre-defined replies.

This task demonstrates how control flow logic can be structured to handle interactive, conversational streams without the need for complex machine learning models or natural language processing (NLP) libraries.

## 🛠️ Project Features
* **Encapsulated Design:** The entire execution engine is wrapped cleanly within a standalone main function (`basic_chatbot()`) for modularity and professional code organization.
* **Continuous Chat Loop:** Implements an infinite processing loop (`while True`) that keeps the chat window active until the user explicitly signals to terminate the session.
* **Input Normalization:** Strips leading/trailing white spaces and automatically shifts user input to lowercase characters (`.lower().strip()`) to guarantee robust, case-insensitive keyword evaluation.
* **Multi-Keyword Lists:** Groups alternate user phrasings together in structured lookup lists (e.g., catching "hello", "hi", or "hey" under one condition) to broaden response capabilities cleanly.
* **Graceful Exit Option:** Provides an explicit keyword pattern ("bye") that prints a warm departure message and safely terminates execution using a clean `break` sequence.

## 💻 Key Python Concepts Covered
* **Functions:** Wrapping execution sequences neatly into reusable structural blocks.
* **Control Loops:** Sustaining application states using continuous conditional loops.
* **If-Elif-Else Conditioning:** Layering precise operational logic to select proper response streams.
* **String Processing Methods:** Transforming user data dynamically for robust pattern-matching.

