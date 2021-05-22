#this is practicing the equations for kinematics
import math
import matplotlib.pyplot as plt
from labellines import *

#set the launch velocity and the gravity constant
u = 13.72
gravityAccel = -9.81
#releaseAngle = 45


def calcTrajectory(releaseAngle):
    #set the initial t value
    t = 0

    #create blank lists for coordinates to plot trajectory
    #this can be replaced with a numpy array later on
    xCoordinates = []
    yCoordinates = []

    #Set the starting coordinates of the projectile in meters
    y = 2.1
    x = 0

    while not y < 0:
        #calculate the displacement of the object in flight
        uy = u * math.sin(math.radians(releaseAngle))
        #vy = 
        sy = uy * t + (gravityAccel * t**2)/2
        y = 2.1 + sy
        if not y < 0:
            print(y)
            yCoordinates.append(y)

            ux = u * math.cos(math.radians(releaseAngle))
            sx = ux * t
            x = 0 + sx
            print(x)
            xCoordinates.append(x)


        #increase t value by 0.001s increments
        t += 0.0001

    plotGraph(xCoordinates, yCoordinates)


def plotGraph(xCoordinates, yCoordinates):
    plt.plot(xCoordinates, yCoordinates)
    plt.xlabel("horizontal distance travelled by projectile")
    plt.ylabel("height of projectile")
    labelLines(plt.gca().get_lines(),align=False,fontsize=14)
    #plt.show()

def calcDrag():
    #take radius of shot put as 0.065m
    radius = 0.065

    #take the density of air at sea level at 15 degrees Celsius as 1.225kg/m^3
    airDensity = 1.225

    #take the drag coefficient of the shotput as 0.5
    dragCoeff = 0.5



for angle in range(1, 51, 5):
    calcTrajectory(angle)
plt.show()
