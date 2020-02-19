# def electionsWinners(votes, k):
#     count = 0
#     mCount = 0
#     vMax = max(votes)
#     for val in votes:
#         if val+k > vMax:
#             count += 1
#         if val == vMax:
#             mCount += 1
#     if k > 0:
#         return count
#     elif mCount == 1:
#         return 1
#     else:
#         return 0

def electionsWinners(votes, k):
    vMax = max(votes)
    count = 0
    if k == 0:
        return 1 if votes.count(vMax) == 1 else 0
    for v in votes:
        if v + k > vMax:
            count += 1
    return count