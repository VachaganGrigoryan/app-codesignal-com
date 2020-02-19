def spiralNumbers(n):
    arr = [[0]*n for i in range(n)]
    sumA = 1
    for i in range(0, n // 2 + 1):
        for r in range(i, n - i):
            arr[i][r] = sumA
            sumA += 1
        for d in range(i + 1, n - i):
            arr[d][r] = sumA
            sumA += 1
        for l in range(n - i - 2, i - 1, -1):
            arr[d][l] = sumA
            sumA += 1
        for u in range(n - i - 2, i, -1):
            arr[u][l] = sumA
            sumA += 1

    return arr