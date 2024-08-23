# Write a function that takes one string and, capitalize the last character
# of each word in uppercase and the rest in lowercase.

# A word is a section of string delimited by spaces/tabs or the start/end of the
# string. If a word has a single letter, it must be capitalized.

# A letter is a character in the set [a-zA-Z]
# For word in string, for word[-1]

def rcapitalize(param):
    words = param.split()
    for word in words:
        print("Word: ", word)
        print("word[-1]: ", word[-1])

rcapitalize("a FiRSt LiTTlE TESt")