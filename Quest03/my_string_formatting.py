''' 	my_string_formatting.py
Create a my_string_formatting function which takes 3 parameters (firstname, lastname and age) and prints a string composed value.
Formatting should be: "Hello, my name is FIRSTNAME LASTNAME, I'm AGE."
Make sure you are printing a newline.
'''

def my_string_formatting(firstname, lastname, age):
    print("Hello, my name is",firstname,lastname,", I'm",age,".")
    print(f"Hello, my name is {firstname} {lastname}, I'm {age}.")

print(my_string_formatting("John", "Doe", 37))
print(my_string_formatting("Baby", "Yoda", 50))
print(my_string_formatting("Marie", "Curie", 26))