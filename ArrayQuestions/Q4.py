#  Find the second largest element in an array

def SecondLargest(arr):
    f = float('-inf')
    s = float('-inf')
    for i in arr:
        if i > f:
            s = f
            f = i
        elif i > s and i != f:
            s = i
    return s

print(SecondLargest([6,7,2,99,32,56]))