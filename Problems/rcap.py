# Write a function that takes one string and, capitalize the last character
# of each word in uppercase and the rest in lowercase.

# A word is a section of string delimited by spaces/tabs or the start/end of the
# string. If a word has a single letter, it must be capitalized.

# A letter is a character in the set [a-zA-Z]
# For word in string, for word[-1]
import re
def rcapitalize(param):
    words = re.split(r'(\s+)', param)
    new_str = []
    for word in words:
        # if len(word) > 1:
            # print("Word: ", word)
            # print("word[-1]: ", word[-1]
        if word.strip(): # Check if the word is not just white space
            if len(word) > 1:
                new_word = word[:-1].lower() + word[-1].upper()
            else:
                new_word = word.upper()
            # print("word[-1] cap: ", new_word)
        else:
            new_word = word # Preserve the spaces as is
        new_str.append(new_word)
    result = ''.join(new_str)
    print(result)

rcapitalize("a FiRSt LiTTlE TESt")