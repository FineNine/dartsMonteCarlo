from math import atan, cos

def convertToPolar(x, y):
    angle = atan(y/x)
    length = x / cos(angle)
    return abs(length), angle