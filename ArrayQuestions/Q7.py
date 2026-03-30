#  Move all zeros to end of array

def moveZero(arr):
    j = 0    # position where non zero should go
    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

print(moveZero([3,0,2,0,0,1,7,8,9]))
        
