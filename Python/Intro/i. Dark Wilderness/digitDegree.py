def digitDegree(n):
    count = 0
    while n > 9:
        n = sum(int(v) for v in str(n))
        count += 1
    return count


# Recursion method

def digitDegree(n, count=0):
    if n > 9:
        sumN = sum(int(v) for v in str(n))
        count += 1
        if sumN > 9:
            return digitDegree(sumN, count)
    return count
