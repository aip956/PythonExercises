

def alpha_mirror(param_1):
    output = ""
    for letter in param_1:
        if letter.isupper():
            new_letter = letter.lower()
            output += new_letter
            print("9output: ", output)
        elif letter.islower():
            new_letter = letter.upper()
            output += new_letter
            print("13output: ", output)
    return output

input1 = "abc"
        
