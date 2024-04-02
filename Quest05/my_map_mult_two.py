'''
my_map_mult_two.py
Multiply each element of an array by 2.

Create a function my_map_mult_two that receives an integer array as a parameter and iterates over the array. 
Perform a multiplication by 2 on each value and return the new array collected.
:type  param_1: {Integer[]}
:rtype: integer[]
"""
def my_map_mult_two(param_1):
'''
#  Mult by 2 in place
def my_map_mult_two(array):
    for i in range (len(array)):
        array[i] *= 2
    return array

# def my_map_mult_two(param):
#     return param * 2

# array = [1, 2, 3, 4, 5]
# result = map(my_map_mult_two, array)
# print(list(result))
# array2 = []
# result2 = map(my_map_mult_two, array2)
# print(list(result2))