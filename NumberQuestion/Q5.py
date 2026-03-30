# Print all divisors of a number 

n = 12
divisors = set()
for i in range(1, n + 1):
    if n % i == 0:
        divisors.add(i)
print("divisors of number = ", divisors)
