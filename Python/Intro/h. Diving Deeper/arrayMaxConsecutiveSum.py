def arrayMaxConsecutiveSum(inputArray, k):
    # return max([sum(inputArray[i:i+k]) for i in range(len(inputArray)-k+1)]) # if len(inputArray) else 0
    maxSum = sum(inputArray[:k])
    newSum = maxSum
    for i in range(1,len(inputArray) - k + 1):
        newSum = newSum - inputArray[i-1] + inputArray[i+k-1]
        if newSum > maxSum: maxSum = newSum
    return maxSum