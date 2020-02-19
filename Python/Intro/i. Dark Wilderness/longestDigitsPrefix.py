def longestDigitsPrefix(inputString):
    prefix = ''
    for ch in inputString:
        if ch.isdigit(): prefix += ch
        else: break
    return prefix 

print(longestDigitsPrefix("jolkj5456kj"))


