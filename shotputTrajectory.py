#Projecting trajectory of a shot put
import math
import matplotlib as plt

class shotPut:
    def __init__(releaseAngle):
        #angle of release in degrees
        self.releaseAngle = releaseAngle
        self.elapsedTime = 0
        #Release force in newtons
        self.releaseForce = 51.9
        #Velocity in m/s
        self.currentVelocity = 13.72
        #XY coordinates in meters
        self.currentX = 2.10
        self.currentY = 0.0

    def updateTime(interval):
        self.elapsedTime += interval

    def updateState(vel, X, Y):
        self.currentVelocity = vel
        self.currentX = X
        self.currentY = Y


def calcDrag(shotPut):
    drag = 6 * math.pi * 0.065 * 0.0000186 * shotPut.currentVelocity
    return drag

def generateCoordinates(shotPut):


def plotGraph(xList, yList):
    plt.plot(xList, yList)
    plt.ylabel("Height of shot put (m)")
    plt.xlabel("Distance travelled by shot put (m)")
