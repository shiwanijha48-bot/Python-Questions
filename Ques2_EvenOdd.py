#------ first ------
if (n//2)*2 == n:
    print("even")
else:
    print("odd")


#--------- second ------
if n & 1:
    print("odd")
else:
    print("even")


#-------- third --------
if n%2 == 0:
    print("even")
else:
    print("odd")

#-------- fourth --------
last_digit = n % 10
if last_digit in [0, 2, 4, 6, 8]:
    print("Even")
else:
    print("Odd")
