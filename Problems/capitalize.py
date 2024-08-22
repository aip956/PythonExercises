def my_capitalize(param):
    if not param:
        return param
    # Convert string to list to edit
    result = list(param)
    first_letter_found = False

    for i in range(len(result)):
        if result[i].isalpha():
            if not first_letter_found:
                result[i]=result[i].upper()
                first_letter_found = True
            else:
                result[i]=result[i].lower()
        elif first_letter_found:
            result[i]=result[i].lower()
    return ''.join(result)

# Test cases
print(my_capitalize("aBc"))
print(my_capitalize(""))
print(my_capitalize("AbcE Fgef1"))
