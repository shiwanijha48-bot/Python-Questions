#  Remove duplicate characters from a string

def removeDuplicate(s):
    r = ""
    for i in s:
        if i not in r:
            r = r + i
    return r

print(removeDuplicate("Hellooooo"))