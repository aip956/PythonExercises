'''
	my_is_sort.py
Let's create a function which will tell us if an array is sorted or not. 
What is sorted? :-)

Write a function that takes an integer array as a parameter (input) and 
returns a boolean (true/false).

Your function should return true if the integer array is sorted in either 
ASC(ascending) or description(descending) order.
Your function should return false if the integer array is not sorted.

Numbers will be from -2_000_000 to 2_000_000

Method:
if sorted list == sorted, flag = 1
if sorted list == sorted, descending, flag = 1

ASC = '''

def my_is_sort(list):
    isSorted = False
    if list == sorted(list):
        isSorted = True
    if list == sorted(list, reverse = True):
        isSorted = True
    return isSorted
    
print(my_is_sort([1, 1, 2]))
print(my_is_sort([2, 1, -1]))
print(my_is_sort([4, 7, 0, 3]))
print(my_is_sort([]))


