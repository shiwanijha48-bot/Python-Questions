# Check whether a string is a palindrome

def palindrome_String(s):
    temp = s
    r = ""
    for i in s:
        r = i + r
    if temp == r:
        print("Palindrome String")
    else:
        print("Not a Palindrome string")

palindrome_String("HELLO")
palindrome_String("AAABBB")
palindrome_String("ABBA")