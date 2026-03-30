#  Find duplicate elements in array

def duplicate(arr):
    duplicateElements = set()
    for i in range( 0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                duplicateElements.add(arr[i])
    return duplicateElements

print(duplicate([2,4,5,2,3,6,8,5,2,3,4,6,8,9,1,23,65]))