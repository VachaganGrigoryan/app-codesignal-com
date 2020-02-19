# import re
def validTime(time):
    return int(time[:2]) < 24 and int(time[3:]) < 60
    # return re.match("(?:[01]\\d|2[0-3]):[0-5]\\d",time)
