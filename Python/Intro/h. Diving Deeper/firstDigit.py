# def firstDigit(inputString):
#     for val in inputString:
#         if val.isdigit():
#             return val
#     return False

import re
def firstDigit(inputString):
    return re.findall("\d",inputString)[0]
