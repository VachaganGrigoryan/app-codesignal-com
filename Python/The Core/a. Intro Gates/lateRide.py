def lateRide(n):
    return sum(int(v) for v in ''.join(str(n//60)+str(n%60)))

