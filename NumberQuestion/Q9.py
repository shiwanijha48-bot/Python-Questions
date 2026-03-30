#   Convert decimal to binary (without built-in functions)

def decimalToBinary(n):
    if n == 0:
        return "0"
    bin = ""
    while n > 0:
        r = n% 2
        bin = str(r) + bin
        n = n//2
    return bin

print(decimalToBinary(10))

#  builtin function-> print(bin(n)[2:]), 
# [2:] as bin(n) gives #0b-1010. so need to remove first 2 "0b".