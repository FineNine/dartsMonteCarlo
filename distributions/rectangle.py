from random import random
from .toPolar import convertToPolar

class Rectangle:
    def __init__(self, height, width, tilt):
        self.height = height
        self.width = width
        self.tilt = tilt
    
    def getThrowCoords(self):
        x = random() * self.width
        y = random() * self.height
        length, angle = convertToPolar(x, y)
        return length, angle + self.tilt
