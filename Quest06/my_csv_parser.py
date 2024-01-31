'''
my_csv_parser.py
Rows are separated by "line" (the character "
"). Columns are separated by ",". (Separators can be different, they can also be ";")

Your goal is to transform a string following the CSV format to a 2d array.

Your function will take two arguments, the contents of a CSV as a string and a separator.
Your function will return an array (line) of arrays (columns).

In this assignment, you will have to determine how to transform a string into an array.


'''

def my_csv_parser(array, parser):
    lines = "column1,column2,column3\nvalue1,value2,value3\n".split("\n")
    print(lines)

    var index = 0

    while (index < lines.length) {
    var values = lines[index].split(',');
    }