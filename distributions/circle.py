from random import random

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def getThrowCoords(self):
        return random() * self.radius, random() * 360