from Essential_module import *
import numpy
# height와 width 값 이상하면 순서 바꾸기

class Student:
    firstMatrix=[[0]*height]*width
    secondMatrix=[[0]*height]*width
    Firstimage = None
    def __init__(self,studentNumber):
        self.studentNumber = studentNumber
    def saveFirstMatrix(self,firstMatrix):
        for x in range(width):
            for y in range(height):
                self.firstMatrix[x][y] = firstMatrix[x][y]
    def saveSecondMatrix(self,secondMatrix):
        for x in range(width):
            for y in range(height):
                self.secondMatrix[x][y] = secondMatrix[x][y]
    
    def calculateFirstVolume(self):
        Volume=0
        for x in range(width):
            for y in range(height):
                Volume+=(Plate_matrix[x][y]-self.firstMatrix[x][y])*pixelSize
        return Volume
    
    def calculateSecondVolume(self):
        Volume=0
        for x in range(width):
            for y in range(height):
                Volume+=(self.secondMatrix[x][y]-self.firstMatrix[x][y])*pixelSize
        return Volume