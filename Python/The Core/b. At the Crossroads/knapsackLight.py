def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    if value2 <= value1 and weight1 <= maxW:
        return value1
    elif weight2 <= maxW:
        return value2
    if weight1 <= maxW:
        return value1
    return 0
