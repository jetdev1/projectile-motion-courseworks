#this is practicing the equations for kinematics
import math
import matplotlib.pyplot as plt
from projectileTrajectoryV1 import *

#set the launch velocity and the gravity constant
u = 13.72
gravityAccel = -9.81
#create blank lists for coordinates to plot trajectory
xCoordinates = []
yCoordinates = []

def calcTrajectory(releaseAngle):
    #set the initial t value
    t = 0
    #Set the starting coordinates of the projectile in meters
    y = 2.1
    x = 0

    while y > 0:
        #calculate the displacement of the object in flight
        uy = u * math.sin(math.radians(releaseAngle))
        #vy =
        sy = uy * t + (gravityAccel * t**2)/2
        y = 2.1 + sy
        if not y < 0:
            #print(y)
            yCoordinates.append(y)

            ux = u * math.cos(math.radians(releaseAngle))
            sx = ux * t
            x = 0 + sx
            #print(x)
            xCoordinates.append(x)

        #increase t value by 0.001s increments
        t += 0.0001


angleList = []
for angle in range(5, 89, 5):
    calcTrajectory(angle)
    print(angle)
    angleList.append(str(angle) + "°")

plotGraph(xCoordinates, yCoordinates)

#plot the ground
plotGraph([0, 22], [0, 0])

#Add the ground to the legend
angleList.append("Ground")

#plot start point
plotGraph([0, 0], [0, 8])

#Add the ground to the legend
angleList.append("Start")
print(angleList)
#Create the legend for the graphs
plt.legend(angleList, loc="upper right")
plt.subplots_adjust(left=0.025, bottom=0.05, right=0.99, top=0.99, wspace=None, hspace=None)

plt.show()
