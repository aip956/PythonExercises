# Write a function that takes two parameters, an integer array and a symbol order, and returns the array sorted. You will take the integer array and order the integers in either descending or ascending order; the symbol order will indicate whether you should sort in ascending or descending order.

# Order can only take two values: asc OR description

# If order is asc, you will order array in ascending order.
# If order is description, you will order array in descending order.

def my_sort(array, order):
    if order == "asc":
        array.sort()
    elif order == "description":
        array.sort(reverse = True)
    return array
    

# Test cases
array1 = [1, 2, 1]
order1 = "asc"
print(my_sort(array1, order1))
