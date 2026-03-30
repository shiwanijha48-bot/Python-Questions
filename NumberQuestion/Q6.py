#  Check whether a number is an Armstrong number

n = 153
temp = n
x = 0
while n > 0:
    ld = n % 10
    x = x + ld*ld*ld  # ld**3
    n = n//10
if temp == x:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")