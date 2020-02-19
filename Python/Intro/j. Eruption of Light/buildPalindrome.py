def checkPalindrome(st):
    return st[::-1] == st


def buildPalindrome(st):
    r = st[::-1]
    if (checkPalindrome(st)):
        return st

    for i in range(len(st)):
        if (checkPalindrome(st + r[len(st) - i::])):
            return st + r[len(st) - i::]
    else:
        return st + r[1::]

##################################################################

def buildPal(line):
    for i in range(0,len(line)):
        if line[i:len(line)] == line[i:len(line)][::-1]:
            return line[0:i] + line[i:len(line)] + line[0:i][::-1]


print(buildPal(input("Enter text : ")))