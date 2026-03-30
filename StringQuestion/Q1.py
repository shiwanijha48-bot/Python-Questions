# Reverse a string

def reverseString(s):
    r = ""
    for i in s:
        r = i + r
    return r

print(reverseString("abcd"))
print(reverseString("HELLO"))