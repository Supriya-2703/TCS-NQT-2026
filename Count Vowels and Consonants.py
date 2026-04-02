# Count Vowels and Consonants

s = "tcsnqt"
vowels = "aeiou"

v = c = 0

for ch in s:
    if ch in vowels:
        v += 1
    else: 
        c += 1

print("Vowels:",v)
print("Consonats:",c)