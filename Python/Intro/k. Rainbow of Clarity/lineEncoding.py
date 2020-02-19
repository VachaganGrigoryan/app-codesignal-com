def lineEncoding(s):
    newS = ''
    word = s[0]
    for v in range(1,len(s)):
        if word[0] == s[v]:
            word += s[v]
            continue
        newS += str(len(word)) + word[0] if len(word) > 1 else word[0]
        word = s[v]
    newS += str(len(word)) + word[0] if len(word) > 1 else word[0]
    return newS
