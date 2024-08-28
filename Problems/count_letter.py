'''Write a function called count_letter that takes a string and returns the number
of occurences of its alphabetical characters. Other characters are not counted.
The order is the order of occurence in the string.

The format is in the examples.

Example 00:

Input: "abbcc"
Output: "1a, 2b, 2c"
Example 01:

Input: "My Hyze 47y 7."
Output: "1m, 3y, 1h, 1z, 1e"

make a dictionary, map the char freq
check if char is alphabetical
convert to lower
'''

def count_letter(param):
    # Init dictionary
    counts = {}
    # For each letter
    for letter in param:
        # Check if alpha char
        if letter.isalpha():
            # Convert to lower case
            letter = letter.lower()
            # If the letter is in the dictionary, increment
            if letter in counts:
                counts[letter] += 1
            # Else add it to the dictionary
            else:
                counts[letter] = 1
    print(f"dict of counts: ", counts)
    # Create a list of formatted strings from the dictionary
    result = [f"{count}{letter}" for letter, count in counts.items()]

    # Join the list
    return ", ".join(result)

# Tests
print(count_letter("abbcc")) # "1a, 2b, 2c"
