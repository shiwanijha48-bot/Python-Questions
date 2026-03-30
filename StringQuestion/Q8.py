# Count frequency of each character

def freq(s):
    count = {}
    for i in s:
        if i not in count :
            count[i] = 1
        else:
            count[i] += 1
    return count

print(freq("Hello"))
print(freq("String"))