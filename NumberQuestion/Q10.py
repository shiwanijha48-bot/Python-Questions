#   Check whether a number is a perfect number

def perfect(n):
    sumDiv = 0
    for i in range(1, n):
        if n % i == 0:
            sumDiv += i
    if sumDiv == n:
        print("Perfect Number")
    else:
        print("Not a Prefect Number")

perfect(6)  # 6= 1+2+3 = 6 perfect
perfect(25) # 25 = 1+5 = 6 not perfect
perfect(28)
perfect(496)
perfect(8128)