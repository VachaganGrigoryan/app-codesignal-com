def tennisSet(score1, score2):
    mins, maxs = (min(score1, score2), max(score1, score2))
    return (maxs == 6 and mins < 5) or (maxs == 7 and mins in (5,6))



def tennisSet(score1, score2):
    if score1 >= 7 and score2 >= 7 or score1 < 5 and score2 >= 7 or score2 < 5 and score1 >= 7:
        return False
    if score1 >= 5 and score2 >= 5:
        if score1 == 7:
            return True
        if score2 == 7:
            return True
        return False
    if score1 >= 5:
        return True
    if score2 >= 5:
        return True
    return False
