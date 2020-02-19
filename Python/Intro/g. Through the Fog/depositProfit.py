# def depositProfit(deposit, rate, threshold):
#     step = 0
#     while deposit < threshold:
#         deposit += deposit / 100 * rate
#         step += 1
#     return step

import math

def depositProfit(deposit, rate, threshold):
    return math.ceil(math.log(threshold/deposit,1+rate/100))

deposit = 100
rate = 20
threshold = 170
print(depositProfit(deposit, rate, threshold))
