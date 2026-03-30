#  Find the longest word in a sentence

def longestWord(s):
    i = s.split()  # ["python", "is", "high", "level", "language"]
    longest = ""
    for k in i:
        if len(k) > len(longest):
            longest = k
    return longest

print(longestWord("Python is high level language"))