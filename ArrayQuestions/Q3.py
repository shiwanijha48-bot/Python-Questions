# Reverse an array

def reverseArray(arr):
    res = []
    for i in arr:
        res = [i] + res
    return res

print(reverseArray([1,3,5,7,9]))