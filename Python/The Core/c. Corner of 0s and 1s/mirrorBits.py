def mirrorBits(a):
    return int('{:b}'.format(a)[::-1], 2)

def mirrorBits(a):
    return int(bin(a)[2:][::-1], 2)

