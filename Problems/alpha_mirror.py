'''
Write a function called alpha_mirror that takes a string and return a new string built
from this string after replacing each alphabetical character by the opposite alphabetical
character.

'a' becomes 'z', 'Z' becomes 'A'
'd' becomes 'w', 'M' becomes 'N'

and so on.

Case is not changed.

ascii a = 97; z = 122; sum of the mirrors is always 219 for lower case
ascii A = 65; Z = 90; sum of the mirrors is always 155 for upper case

'''

def alpha_mirror(param_1):
    output = ""
    for letter in param_1:
        if letter.isupper():
            new_letter = chr(155 - ord(letter))
            output += new_letter
            print("9output: ", output)
        elif letter.islower():
            new_letter = chr(219 - ord(letter))
            output += new_letter
            print("13output: ", output)
        else:
            output += letter
            print("16output: ", output)
    return output

input1 = "abc"
print(alpha_mirror(input1))
        
