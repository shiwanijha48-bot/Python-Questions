#  Find missing number in an array (1 to n) 
def missingnum(arr):
    n = len(arr) + 1 # one for missing num
    total = n * (n+1) // 2   # sum of n numbers= formula
    sumArr = 0
    for i in arr:
        sumArr += i
    return total - sumArr

print(missingnum([1,2,3,5,6,7,8,9,10]))




