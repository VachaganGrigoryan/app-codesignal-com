import string

def isBeautifulString(inputString):
    arr = [inputString.count(ch) for ch in string.ascii_lowercase]
    print(arr)
    return arr[::-1] == sorted(arr)

# def isBeautifulString(inputString):
#     abc = [0]*26;
#     for c in inputString:
#         abc[ord(c) - 97] += 1
#     t = len(inputString) + 1
#     for i in abc:
#         if t < i:
#             print(abc,t)
#             return False
#         else:
#             t = i
#     return True