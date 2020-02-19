def phoneCall(min1, min2_10, min11, s):
    count = 0
    if s - min1 >= 0:
        count += 1
        s -= min1
    if s - 9 * min2_10 >= 0:
        s -= 9 * min2_10
        count += 9
    else:
        count += s // min2_10
        s -= s // min2_10 * min2_10
        return count
    if s // min11 >= 0:
        count += s // min11

    return count


def phoneCall(min1, min2_10, min11, s):
    if s<min1:
        return 0
    elif s>=min1 and s<=min1+9*min2_10:
        return 1+(s-min1)//min2_10
    return 10+(s-min1-9*min2_10)//min11
