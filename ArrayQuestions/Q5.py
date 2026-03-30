#  Count even and odd numbers in an array

def countEvenOdd(arr):
    even_count = 0
    odd_count = 0
    for i in arr:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

print(countEvenOdd([4,9,8,5,6,2]))
