'''
Your function will return an integer

Given 2 strings with the exact number of characters, count how many characters are different at the same position. 
if they don't share the exact number of characters, return -1.

if the two arguments are not the same size, you will return -1

Example 00
Input: "GGACTGA" && "GGACTGA"
Output: 
Return Value: 0

Example 01
Input: "ACCAGGG" && "ACTATGG"
Output: 
Return Value: 2

Example 02
Input: "GGACGGATTCTG" && "AGG"
Output: 
Return Value: -1
'''
def my_hamming_dna(string1, string2):
    diff = 0
    if len(string1) != len(string2):
        return -1
    for i in range(1, len(string1)):
        if string1[i] != string2[i]:
            diff += 1
    return diff

print(my_hamming_dna("GGACTGA", "GGACTGA"))
print(my_hamming_dna("ACCAGGG", "ACTATGG"))
print(my_hamming_dna("GGACGGATTCTG","AGG"))
print(my_hamming_dna("",""))

