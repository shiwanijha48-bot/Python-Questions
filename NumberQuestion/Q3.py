# Check whether a number is a palindrome
n = 1210
temp = n
rev = 0
while n > 0:
    ld = n % 10
    rev = rev * 10 + ld
    n = n// 10
if temp == rev :
    print("It is Palindrome Number")
else:
    print("Not a Palindrome Number")
