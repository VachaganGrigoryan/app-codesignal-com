def arrayPacking(a):
    k = 0
    for i,v in enumerate(a):
        k |= (v<<(i<<3))
    return k

def arrayPacking(a):
    return sum(map(lambda i,v : v<<(i<<3), range(len(a)), a))

a = [24, 85, 0]

print(arrayPacking(a))