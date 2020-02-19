def rangeBitCount(a, b):
    return sum([bin(v).count("1") for v in range(a,b+1)])