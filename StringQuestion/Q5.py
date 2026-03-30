# Find the length of string without using len()

def LenString(s):
    count = 0
    for i in s:
        count += 1
    return count

print(LenString("HELLO"))
print(LenString("AbhHFnnTRDHV"))
print(LenString("hElP"))