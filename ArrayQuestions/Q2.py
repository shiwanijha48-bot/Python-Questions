# Calculate the sum of elements in an array

def SumElements(arr):
    sumArray = 0
    for i in arr:
        sumArray += i
    return sumArray

print(SumElements([6,8,3,2,1]))