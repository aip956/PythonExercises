# An anagram is a sequence of characters formed by rearranging the letters of
# another sequence, such as 'cinema', formed from 'iceman'.

# Given two strings as parameters, create a function able to tell whether or
# not the first string is an anagram of the second.

from collections import Counter
def is_anagram(string1, string2):
    print((Counter(string1) == Counter(string2)))
    return (Counter(string1) == Counter(string2))


is_anagram("abcdef", "fabcde")