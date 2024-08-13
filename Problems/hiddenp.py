# Write a function named hidenp that takes two strings and returns 1
# if the first string is hidden in the second one,
# otherwise returns 0 followed by a newline.

def hidenp(a, b):
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1
    return 1 if i == len(a) else 0

# Test cases
a1 = "fgex.;"
b1 = "tyf34gdgf;'ektufjhgdgex.;.;rtjynur6"
print(hidenp(a1, b1))  # 1

a2 = "abc"
b2 = "btarc"
print(hidenp(a2, b2))  # 0