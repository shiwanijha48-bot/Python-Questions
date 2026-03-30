#   Find GCD and LCM of two numbers

def gcd(x, y):  # HCF 
    ans = 1
    for i in range(1, min(x,y) + 1):
        if x % i == 0 and y % i == 0:
            ans = i
    return ans

def lcm(x , y):
    for i in range(max(x,y), x*y + 1):
        if i % x== 0 and i % y == 0:
            return i


print(gcd(12, 15))
print(lcm(12, 15))