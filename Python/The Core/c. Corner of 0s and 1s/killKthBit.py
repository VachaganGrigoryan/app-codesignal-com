def killKthBit(n, k):
    return n&(n^(1<<k-1))

def killKthBit(n, k):
    return n ^ n & 1 << k - 1