#  Check whether two strings are anagrams

def Anagram(s, r):
    s = s.lower()
    r = r.lower()
    count1 = {}
    count2 = {}
    if len(s) != len(r):
        return False
    for i in s:
        if i not in count1 :
            count1[i] = 1
        else:
            count1[i] += 1
    for i in r:
        if i not in count2 :
            count2[i] = 1
        else:
            count1[i] += 1
    
    print( count2, count2)

    if count1 == count2:
        print("True")
    else:
        print("False")
    
Anagram("rat", "Car")
Anagram("RaT", "rat")