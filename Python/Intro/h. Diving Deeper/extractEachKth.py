def extractEachKth(inputArray, k):
    return [i for (n,i) in enumerate(inputArray) if (n+1) % k != 0]
