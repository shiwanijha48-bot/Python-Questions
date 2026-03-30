# Count vowels and consonants in a string

def countVowels(s):
    count = 0
    s = s.lower()
    for v in s:        
        if v == 'a' or v == 'e' or v == 'o' or v == 'i' or v == 'u':
            count += 1
    return count

print(countVowels("HellO"))
print(countVowels("AeiOu"))