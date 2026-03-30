#  Find the first non-repeating character

def FirstNonRepeating(s):
    count = {}
    for i in s:
        if i not in count :
            count[i] = 1
        else:
            count[i] += 1
    for j in range(0, len(s)):
        if count[s[j]] == 1:
            return s[j]
    return -1

print(FirstNonRepeating("hello"))   
print(FirstNonRepeating("hheellooo"))         