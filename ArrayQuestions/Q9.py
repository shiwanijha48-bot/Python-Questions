#   Merge two sorted arrays

def merge(num1, num2):
    m = len(num1)
    n = len(num2)
    num1 = num1 + [0]*n  # adding space fpr arr num2
    i = m-1  # last ele of num1
    j = n-1  # last ele of num2
    k = m + n -1   # last index of final array

    while j >= 0: # loop until 2nd arr finishes
        if i >= 0 and num1[i] > num2[j]:  #  num1[i=3]= 4 and num2[j=3] = 8, 8 is bigger num1 still has elements, val is bigger
            num1[k] = num1[i]  # place 8 at num1[k=7]= last eleemnt. put larger val at end
            i-=1  # move ptr i
        else:
            num1[k] = num2[j]  # put val from num2
            j -= 1  # move ptr j
        k -= 1  # move backward in res arr
    return num1
    
print(merge([1,2,3,4], [3,4,7,8]))
