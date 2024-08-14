# Write a function that determines if a given number is a power of 2.
# This function returns 1 if the given number is a power of 2, otherwise it returns 0.

def power_of_2(n):
    if n <= 0:
        return 0
    else:
        return 1 if (n & (n - 1)) == 0 else 0

    

# Test cases
print(power_of_2(1))  # 1
print(power_of_2(4))  # 1
print(power_of_2(4294967295))  # 1