# Written by Ty Kirchmann
from random import random
from math import cos, sin, atan, floor

class Engine:
    def __init__(self, iterations, numberOfTests, distribution):
        self.iterations = iterations #Number of randomized centers generated
        self.distribution = distribution #The underlying distribution/pattern that the darts are thrown in
        self.numberOfTests = numberOfTests #number of times each randomized center will  be tested
        self.testLength = 0
        self.testAngle = 0
    
    def run(self):
        #Init list of centers
        lengths = []
        angles = []
        avgPoints = []
        avgThrows = []

        #Loop over the range of iterations - aka how many randomized centers there are
        for i in range(self.iterations + 1):
            self.testLength = 0
            self.testAngle = 0
            if i != 0:
                self.testLength = random() * 100
                self.testAngle = random() * 360
                print("Center Length: " + str(self.testLength) + " -- Center Angle: "+str(self.testAngle))
            
            lengths.append(self.testLength)
            angles.append(self.testAngle)
            
            listOfPoints = []
            listOfThrows = []

            #Loop over the number of tests per center
            for j in range(self.numberOfTests):
                points = 301
                throwCount = 0

                #Loop to throw darts until below 1
                while points >= 1:
                    throwValue = self.throwDart(self.testLength, self.testAngle)
                    listOfPoints.append(throwValue)
                    print(points)
                    print(throwValue)
                    points = points - throwValue
                    throwCount += 1
                
                listOfThrows.append(throwCount)
            
            #print(listOfPoints)
            #print(listOfThrows)
            avgPoints.append(sum(listOfPoints)/len(listOfPoints))
            avgThrows.append(sum(listOfThrows)/len(listOfThrows))
        
        return lengths, angles, avgPoints, avgThrows
                

    def throwDart(self, centerLength, centerAngle):
        length, angle = self.distribution.getThrowCoords()
        throwLength = ((centerLength**2) + (2 * centerLength * length * cos(angle - centerAngle)) + (length**2))**.5
        throwAngle = centerAngle + atan((length * sin(centerAngle - angle))/(centerLength + (length*cos(angle - centerAngle))))        
        return valueThrow(throwLength, throwAngle)

# separate function to value the individual throw   
def valueThrow(length, angle):
    print(angle)
    if length < 32:
        if length < 12.7:
            return 50
        else:
            return 25
    pointCategories = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]

    points = pointCategories[floor((angle + 9)/18) - 1]
    #print(points)

    if length < 107 and length > 99:
        return points*3
        
    
    if length <= 170 and length > 162:
        return points*2
    
    if length > 170:
        return 0
    
    return points
        