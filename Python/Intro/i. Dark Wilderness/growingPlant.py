# import math
def growingPlant(upSpeed, downSpeed, desiredHeight):
    # return math.ceil((desiredHeight-downSpeed)/(upSpeed-downSpeed)) if desiredHeight > upSpeed else 1
    return (desiredHeight - upSpeed - 1) // (upSpeed - downSpeed) + 2 if desiredHeight > upSpeed else 1