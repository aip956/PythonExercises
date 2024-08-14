# Create an iterated function that returns the value of a power applied to a number. An power lower than 0 returns 0. Overflows don't have to be handled.
# First parameter is the number, second parameter is the power

def recursive_pow(n, power):
    if power < 0:
        return 0
    elif power == 0:
        return 1
    else:
        return n * recursive_pow(n, power - 1)
    
# Test cases
print(recursive_pow(2, 3))  # 8