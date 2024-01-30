''' my_abs.py
Create a my_abs function.

Reproduce the behavior of an abs() function. It always returns the positive value of a number.
'''

# :type  param_1: {Integer}
# :rtype: integer
# """
def my_abs(x):
    if(x < 0):
        return x * -1
    else:
        return x
    
print(my_abs(-30))
print(my_abs(30))
print(my_abs(0))