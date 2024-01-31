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
    # split into lines
    lines = array.split("\n")
    print(lines)

    # parse into columns
    result = [line.split(parser) for line in lines]

    # remove last \n
    if result[-1] == ['']:
        result.pop()

    return result


print(my_csv_parser("a,b,c,e\n1,2,3,4\n", ","))
    