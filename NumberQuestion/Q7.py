# Print all prime numbers in a given range
prime_nos = set()
def prime_no(n):
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_nos.add(i)
    print("Prime Numbers= ", prime_nos)
prime_no(9)