from random import gauss, random

class Gaussian:
    def __init__(self, stddev):
        self.stddev = stddev

    def getThrowCoords(self):
        length = gauss(0, self.stddev)
        angle = random() * 360
        return length, angle
