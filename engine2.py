# Written by Ty Kirchmann
from random import random
import pandas as pd
from math import cos, sin, atan, floor
from statistics import stdev
from distributions.circle import Circle

#Version 2.0
class Engine:
    def __init__(self, games, distribution):
        self.length = 0
        self.angle = 0
        self.gameData = pd.DataFrame(columns=['length','angle','avgPoints','std'])
        self.pointData = pd.DataFrame(columns=['length','angle','avgPoints','std'])
        self.games = games
        self.distribution = distribution
    
    def loadWriteGames(self):
        points = pd.read_csv('points.csv')
        for idx, row in points.iterrows():
            self.length = row['length']
            self.angle = row['angle']
            for i in range(self.games):
                self.gameData = self.gameData.append(runGame(self.length, self.angle, self.distribution))
        
        self.gameData.to_csv('raw_data.csv')
        aggData = self.gameData.groupby(['length','angle']).agg({'score':['mean','std']})
        aggData = aggData.xs('score', axis=1, drop_level=True).reset_index(['length','angle'])
        aggData.rename(columns={'mean','avgPoints'}, inplace=True)
        aggData.to_csv('aggData.csv')



def buildPoints():
    points = pd.DataFrame(columns=['length','angle'])
    lengths = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]
    angles = list(range(0, 360))
    for length in lengths:
        newPoints = pd.DataFrame({'length':[length]*360, 'angle':angles}, columns=['length','angle'])
        points = points.append(newPoints)
    print(len(points) + " points were created")
    points.to_csv('points.csv', index=False)

def throwDart(centerLength, centerAngle, distribution):
    print(centerLength)
    print(centerAngle)
    length, angle = distribution.getThrowCoords()
    x1, y1 = cartesian(centerLength, centerAngle)
    x2, y2 = cartesian(length, angle)
    x3 = x1 + x2
    y3 = y1 + y2
    newLength, newAngle = polar(x3, y3)
    #print("\nDistriubtion Coords")
    print(x1)
    print(y1)
    # print("\nCenter Coords")
    # print(x2)
    # print(y2)
    # print("\nCart after")
    # print(x3)
    # print(y3)
    #throwLength = ((centerLength**2) + (2 * centerLength * length * cos(angle - centerAngle)) + (length**2))**.5
    #throwAngle = centerAngle + atan((length * sin(angle - centerAngle))/(centerLength + (length*cos(angle - centerAngle))))
    # print("\nAfter translation")
    # print(newLength)
    # print(newAngle)        
    return valueThrow(newLength, newAngle)

def runGame(centerLength, centerAngle, distribution):
    points = 301
    listOfPoints = []

    #Loop to throw darts until below 1
    while points >= 1:
        throwValue = throwDart(centerLength, centerAngle, distribution)
        listOfPoints.append(throwValue)
        #print(throwValue)
        points = points - throwValue
        print(throwValue)
    return print(pd.DataFrame({'length':[centerLength], 'angle':[centerAngle], 'avgPoints':[(sum(listOfPoints)/len(listOfPoints))], 'std':stdev(listOfPoints)}))

def cartesian(length, angle):
    return length*cos(angle/57.2958), length*(sin(angle))

def polar(x, y):
    return (x**2 + y**2)**.5, atan(y/x)*57.2958

def valueThrow(length, angle):
    if length < 32:
        if length < 12.7:
            return 50
        else:
            return 25
    #pointCategories = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]
    pointCategories = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]

    points = pointCategories[floor((angle - 9)/18)]
    #print(points)

    if length < 107 and length > 99:
        return points*3
        
    
    if length <= 170 and length > 162:
        return points*2
    
    if length > 170:
        return 0
    return points

