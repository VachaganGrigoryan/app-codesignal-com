def absoluteValuesSumMinimization(a):
    # Sum = [sum([abs(val-elm) for val in a]) for elm in a]
    # min = Sum[0]
    # minSum = a[0]
    # for i,v in zip(a,Sum):
    #     if min > v:
    #         min = v
    #         minSum = i
    # return minSum
    return a[len(a)//2] if len(a)%2 else a[len(a)//2-1]
