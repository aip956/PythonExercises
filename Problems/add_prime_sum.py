# Write a function that takes a positive integer as argument and returns the sum
# of all prime numbers inferior or equal to it followed by a newline.

# If the number of arguments is not 1, or the argument is not a positive number,
# just display 0 followed by a newline.

# 5: 
# is 2 prime?
#     2 / 2 != 0; no => add
# is 3 prime?
#     3 /2 != 0; yes => add
# is 4 prime?
#     4 / 2 != 0; no
# is 5 prime?
#     5 / 2 != 0; yes
#     5 / 3 != 0; yes
#     5 / 4

def is_prime(param_1): # 10
    # print("line 20: ", param_1)
    if param_1 <= 1:
        return False
    # print("line 23: ", param_1//2 + 1)
    for j in range(2, param_1//2 + 1):
        # print("line24: ", j)
        if param_1 % j == 0:
            # print (param_1, " is not prime")
            return False
    # print(param_1, " is prime")
    return True
        
    
def add_prime_sum(param_1):
#     i = param_1
#     # For each num, check if it is prime
#     # If prime, add to sum

    sum = 0
    for i in range(2, param_1+1):
        print("i: ", i) #2
        print("is_prime(i): ", is_prime(i))
        if (is_prime(i)):
            sum += i
    return sum
        
# Test cases
print("input: 5")
print(add_prime_sum(5))  # 2+3+5
print("input: 8")
print(add_prime_sum(8))  # 2+3+5+7=17
