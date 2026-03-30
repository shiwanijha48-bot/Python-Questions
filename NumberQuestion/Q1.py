# Check whether a number is prime or not
num = 19
if num <= 1:
    print("Not a Prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Number is not a Prime")
            break
    else:
        print("Number is Prime")