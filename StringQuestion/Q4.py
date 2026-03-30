#  Convert string to uppercase without using built-in functions
 
def upperCase(s):
    r = ""
    for i in s:
        if i >= 'A' and i <= 'Z':
            r = r + i
        else:
            r = r + chr(ord(i) - 32)
    return r

print(upperCase("HeLLoOoO"))

#  ord(i) = converts char into ASCII numbers. a= 97
#  ord(i)-32 = gives uppercase of the same char
#  a= 97, A 65  ->  a-A = 32
#  chr(65) = gives char from ASCII number of A