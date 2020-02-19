import re

def longestWord(text):
    arr = ''.join([c if c.isalpha() else ' ' for c in text]).split(' ')
    newArr = [len(val) for val in arr]
    maxLen = max(newArr)
    return ''.join([c for c in arr if len(c) == maxLen])

def longestWord(text):
    return max(re.split('[^a-zA-Z]', text), key = len)

