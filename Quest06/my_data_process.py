'''
my_data_process.py
Our function will group the data and it will become a Hash of hash. (Wow.)
Example:
"{'Gender': {'Male': 22, 'Female': 21}, 'Email': {'yahoo.com': 3, 'hotmail.com': 2}, ...}"

We will discard the column FirstName, LastName, UserName and Coffee Quantity from our output.


'''

import json
def my_data_process(data):
    lines = data.split("\n")
    header = lines[0].split(",")
    result = {}

    for col in header:
        result[col] = {}

    for line in lines[1:]:
        if not line:
            continue
        row = line.split(",")
        print("row: ", row)

        if len(row) < len(header):
            continue

        for col, value in zip(header, row):
            