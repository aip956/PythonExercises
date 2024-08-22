# Write a program that takes a string, and print the first 'z'
# character it encounters in it, followed by a newline. If there are no
# 'z' characters in the string, the program writes 'z' followed
# by a newline. If the number of parameters is not 1, the program prints
# 'z' followed by a newline.

# for each character in param, 
# if length is not 1, print z
# if = z, print z, \n
def aff_z(param):
    if len(param) != 1:
        print("z")
    elif param == 'z':
        print("z")
    else: 
        print("z")


# Test
aff_z("abc")
aff_z("RaInB0w d4Sh!")
aff_z("")
    
    
