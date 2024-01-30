''' my_string_index.py
Create a my_string_index function which takes 2 parameters (haystack and needle) and locates the first occurrence of the character needle in the string haystack and returns the position.

You can think of this function as: is there an L (character) in my string "helLo"?

The objective is to build a loop that has an if statement which returns the characters position when it matches the right character.

for i in range(1, len(sys.argv)):
'''

def my_string_index(string, character):
    for i in range(1, len(string)):
        if character == string[i]:
            return i
    return -1

print(my_string_index("hello", "l"))
print(my_string_index("aaaa", "b"))