import math
import matplotlib.pyplot as plt
import numpy as np

class ShotPut:
    def __init__(self, launchAngle):
        self.currentVel = 13.72
        self.currentVelY = self.currentVel * math.sin(math.radians(launchAngle))
        self.currentVelX = self.currentVel * math.cos(math.radians(launchAngle))
        #print(self.currentVelX, self.currentVelY)
        self.gravityAccel = -9.81
        self.launchAngle = launchAngle
        self.y = 2.1
        self.x = 0
        self.xCoordinates = []
        self.yCoordinates = []

    def calcTrajectory(self):
        t = 0

        while self.y > 0:
            self.yDisplacement = self.currentVelY * t + (self.gravityAccel * t**2)/2
            self.xDisplacement = self.currentVelX * t
            #print(self.yDisplacement, self.xDisplacement)

            self.y = 2.1 + self.yDisplacement
            self.x = 0 + self.xDisplacement

            #print(self.y, self.x)

            self.yCoordinates.append(self.y)
            self.xCoordinates.append(self.x)

            t += 0.001

def main():
    angleList = []
    for angle in range(5, 89, 5):
        shot = ShotPut(angle)
        shot.calcTrajectory()
        angleList.append(str(angle) + "°")
        plt.plot(shot.xCoordinates, shot.yCoordinates)
        #print(shot.xCoordinates, "\n", shot.yCoordinates)

    #plot the ground
    plt.plot([0, 22], [0, 0])

    #Add the ground to the legend
    angleList.append("Ground")

    #plot start point
    plt.plot([0, 0], [0, 8])

    #Add the ground to the legend
    angleList.append("Start")

    #Create the legend for the graphs
    plt.legend(angleList, loc="upper right")
    plt.subplots_adjust(left=0.038, bottom=0.05, right=0.99, top=0.99, wspace=None, hspace=None)

    plt.xlabel("horizontal distance travelled by projectile")
    plt.ylabel("height of projectile")

    plt.show()

main()
