# CodeAlpha Internship - Task 3: Task Automation with Python Scripts

This repository contains **Task 2 / Task 3: Task Automation**, developed as part of my Python Programming Internship at CodeAlpha

## 📌 Project Overview
The objective of this project is to optimize and automate a common, repetitive real-life daily task using a clean Python script

For this specific task, I selected the directory organization workflow option. [cite_start]The script scans a designated source directory, identifies all image files containing the target extension (`.jpg`), and moves them automatically into a new organized destination folder.

## 🛠️ Project Features[cite: 44]
* **Automated Directory Generation:** Uses system checks (`os.path.exists`) to detect missing directories. If the source or destination folder does not exist, the script builds them natively on runtime.
* **Targeted Extension Filtering:** Utilizes explicit string filtering operations (`.endswith(".jpg")`) to isolate and filter specific file types without disturbing other data types in the directory.
* **High-Level File Operations:** Leverages active stream tools to safely lift, transfer, and rewrite files cleanly between operating system partitions.
* **Console Automation Summary:** Provides dynamic console feedback tracking every single moved asset and outputs a finalized tally of total actions completed.

## 💻 Key Python Concepts Covered
* **System Operations (`os`):** Navigating paths, creating directories, and indexing directory listings
* **High-level File Utilities (`shutil`):** Executing clean file migrations and system transfers safely
* **Control Loops & String Matching:** Scanning multi-file data streams using `for` loops combined with case-insensitive validation strings.

