'''
Problem

Check if two strings contain the same characters in any order.

Example
listen and silent → True

'''

s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")