"""
Write a function that takes an array of strings and returns
the longest string that appears in every parameter's strings. If more that one
string qualifies, it will return the one that appears first in the first
parameter. Note that the empty string technically appears in any string.

Example 00
Input: ["ab", "bac", "abacabccabcb"] && 3
Output: 
Return Value: "a"

Example 01
Input: ["bonjour", "salut", "bonjour", "bonjour"] && 4
Output: 
Return Value: "u"

Example 02
Input: ["xoxAoxo", "xoxAox", "oxAox"] && 3
Output: 
Return Value: "oxAox"

"""

def str_maxlenoc(param_1, param_2):
    # Find the shortest string
    shortest_str = min(param_1, key=len)
    # Find the longest string
    longest_str = max(param_1, key=len)
    # Find the common string
    common_str = ""
    for i in range(len(shortest_str)):
        if shortest_str[i] == longest_str[i]:
            common_str += shortest_str[i]
        else:
            break
    return common_str