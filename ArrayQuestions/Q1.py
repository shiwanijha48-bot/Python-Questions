# Find the maximum and minimum element in an array 

def MaxMin(arr):
    maxi = float('-inf')
    mini = float('inf')
    for i in arr:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    return mini, maxi

print(MaxMin([2,5,8,4]))
print(MaxMin([364,99,223,55,7074847,383]))