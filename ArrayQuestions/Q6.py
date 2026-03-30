#   Find all pairs with given sum (Two Sum problem)

def twoSum(arr, target):
    pairs = []
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

print(twoSum([2,3,5,8,1], 10))
print(twoSum([2,3,5,8,1], 11))