# Reproduce the behavior of the function strlen.
# The strlen() function computes the length of the string s.

# The strlen() function returns the number of characters.

def my_strlen(s):
    count = 0
    for i in s:
        count += 1
    return count


input1 = "abc"
print(my_strlen(input1))  # 3
input2 = "RaInB0w d4Sh!"
print(my_strlen(input2))  # 13