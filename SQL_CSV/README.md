# Welcome to my ds babel

## Task
What is the problem, and where is the challenge?
The task is to bridge the gap between different data formats by converting data between SQL and CSV. This involves:
- SQL to CSV: Extracting data from an SQLite database and transforming it into a well-formatted CSV file
- CSV to SQL: Taking data from a CSV file and importing it into an SQLite database, dynamically creating the table if necessary
- Challenge: Ensuring compatibility with varying column names and handling data integrity between formats.
This project demonstrates the importance of data interoperability and showcases how to efficiently handle format conversions in Python.

## Description
To solve the problem, I created two core functions:
1. sql_to_csv: Connects to an SQLite database, retrieves data from a specified table, and converst it to a CSV format. The output is saved to a file for portability.
2. csv_to_sql: Reads an CSV file, extracts headers to define the table schema, and inserts the data into an SQLite database. If the table does not exist, it is created dynamically.

## Installation
How to install my project? ie. venv, npm install?

## Usage
How does it work? How do I run it?

