import re

def isMAC48Address(inputString):
    MAC48 = inputString.split('-')
    if len(MAC48) != 6:
        return False
    MAC48 = "".join(MAC48)
    if len(MAC48) != 12:
        return False
    try:
        k = int(MAC48,16)
    except ValueError:
        return False
    return True

print(isMAC48Address("00-1B-63-84-45-E6"))
print(isMAC48Address("02-03-04-05-06-07-"))

def isMAC48Address(inputString):
    return bool(re.match('^([\dA-F]{2}-){5}([\dA-F]{2})$', inputString))

