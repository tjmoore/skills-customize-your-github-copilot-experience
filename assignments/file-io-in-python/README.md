# 📘 Assignment: File I/O in Python

## 🎯 Objective

Learn how to read from and write to files in Python. By the end of this assignment, you will be able to open files safely, process their contents, and save results to a new file.

## 📝 Tasks

### 🛠️	Read and Display a File

#### Description
Write a Python program that opens a text file and prints its contents to the console, one line at a time.

#### Requirements
Completed program should:

- Open `data.txt` for reading using Python's built-in `open()` function.
- Read and print each line of the file to the console.
- Use a `with` statement to ensure the file is closed automatically after reading.

### 🛠️	Analyse the File Contents

#### Description
Extend your program to count and display useful statistics about the file's contents.

#### Requirements
Completed program should:

- Count and display the total number of lines in the file.
- Count and display the total number of words across all lines.
- Count and display the total number of characters in the file.

### 🛠️	Write Results to an Output File

#### Description
Save the statistics from Task 2 into a new file called `results.txt`, and handle any file errors gracefully.

#### Requirements
Completed program should:

- Write the line count, word count, and character count to `results.txt`.
- Use a `try`/`except` block to catch and display a helpful error message if the input file cannot be opened.
- Confirm to the user (via a printed message) when `results.txt` has been written successfully.
