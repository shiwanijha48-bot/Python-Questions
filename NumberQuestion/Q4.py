#  Find the sum of digits of a number

n = 12345
sum_of_digits = 0
while n > 0:
    ld = n % 10
    sum_of_digits += ld
    n = n // 10
print("Sum of digits = ", sum_of_digits)
