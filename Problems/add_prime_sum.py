# Write a function that takes a positive integer as argument and returns the sum
# of all prime numbers inferior or equal to it followed by a newline.

# If the number of arguments is not 1, or the argument is not a positive number,
# just display 0 followed by a newline.
"""
5: 
is 2 prime?
    2 / 2 != 0; no
is 3 prime?
    3 /2 != 0; yes
is 4 prime?
    4 / 2 != 0; no
is 5 prime?
    5 / 2 != 0; yes
    5 / 3 != 0; yes
    5 / 4

"""


def add_prime_sum(param_1):
    # For each num, check if it is prime
    # If prime, add to sum
    sum = 0
    upper = param_1//2 + 1
    print("upper: ", upper)
    # 3, 4, 5, 6 
    for i in range(2, upper):
        print("i: ", i) #2
        for j in range(2, i): #2, 3
            if i % j != 0:
                sum += j
                print("j: ", j)
                print("sum: ", sum)
    return sum
        
# Test cases
print("input: 5")
print(add_prime_sum(5))  # 17
print("input: 7")
print(add_prime_sum(7))  # 28
