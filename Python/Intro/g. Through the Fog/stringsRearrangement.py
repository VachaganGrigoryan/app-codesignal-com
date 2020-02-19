def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l

def stringsRearrangement(inputArray):
    for line in permutation(inputArray):
        flag = True
        for i in range(len(line) - 1):
            c = 0
            for j in range(len(line[i])):
                if line[i][j] != line[i + 1][j]:
                    c += 1
            if c != 1:
                flag = False
        if flag:
            return True
    return False
