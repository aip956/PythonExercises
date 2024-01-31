'''
	my_count_on_it.py
    Count the size of each elements in an array.

Create a function my_count_on_it that receives a string array 
as a parameter and returns an array with the length of each string.
:type  param_1: {String[]}
:rtype: integer[]
"""
def my_count_on_it(param_1):
length (string).split()
    '''

def my_count_on_it(string):
    return [sum(c.isalnum() or c.isspace() for c in string)]


result = [length for sublist in map(my_count_on_it, ["This", "is", "the", "way"]) for length in sublist]
result2 = [length for sublist in map(my_count_on_it, ["aBc", "AbcE Fgef1"]) for length in sublist]
result3 = [length for sublist in map(my_count_on_it, ["aBc"])for length in sublist]
print(result)
print(result2)
print(result3)


# print(list(map(my_count_on_it,["This", "is", "the", "way"])))
# print(my_count_on_it(["This", "is", "the", "way"]))
# print(my_count_on_it(["aBc", "AbcE Fgef1"]))