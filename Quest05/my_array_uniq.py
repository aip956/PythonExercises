'''
Create an array without any duplicates.

Create a function my_array_uniq that receives an integer 
array as a parameter and returns an array with those integers 
but without any duplicates.

create an empty output array
for each element, if not in output
add to output
'''

def my_array_uniq(input):
    output = []
    for element in input:
        if element not in output:
            output.append(element)
    return output

# print(my_array_uniq([1, 1, 2]))
# print(my_array_uniq([]))
# print(my_array_uniq([1, 1, 1, 2, 3, 4, 1]))