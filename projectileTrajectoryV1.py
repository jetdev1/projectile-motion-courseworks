#this approach will focus most of the calculations on vector quantities
import math
import matplotlib.pyplot as plt

#create the object shotPut to hold all the constants
#as well as the current state of the projectile

class shotPut:

    #the init function will run when the object is first created
    #variables and constants of the shot put will be defined here
    def __init__(self, launchAngle):
        #launch velocity = 13.72m/s
        #value taken from Ryan Crouser's best throw in 2017 IAAF championshups
        self.u = 13.72

        #take gravitational acceleration constant as -9.81m/s^2
        self.gravityAccel = -9.81

        #take radius of men's shot put as 0.065m
        self.radius = 0.065

        #take drag coefficient of shot as 0.5
        self.dragCoeff = 0.5

        #take the density of air at sea level at 15 degrees Celsius as 1.225kg/m^3
        self.airDensity = 1.225

        #create a variable to hold the current velocity value of the shot put
        #at the point where this object is created, set the velocity to its launch velocity
        self.currentVel = 13.72

        #calulate the verticle velocity of the shot at launch put using trigonometric ratios
        #math.sin accepts values only in radians
        self.yVel = self.currentVel * math.sin(math.radians(self.releaseAngle))

        #calulate the horizontal velocity of the shot put at launch using trigonometric ratios
        #math.cos accepts values only in radians
        self.xVel = self.currentVel * math.cos(math.radians(self.releaseAngle))

        #set the mass(kg) of the shot put
        self.mass = 7.26

        #set the launch angle of this instance of the shot shotPut
        self.launchAngle = launchAngle

        #initialise the coordinates of the shot put to t=0
        #coordinates are in meters
        self.y = 2.1
        self.x = 0

        #create blank lists for coordinates to plot trajectory
        self.xCoordinates = []
        self.yCoordinates = []



    #this function calculates the drag of the shot put based on
    #current velocity of the shot put
    def calcDragDecel(self, currentVel):
        #using Newton's drag and taking pi = 3.14159
        self.drag = 0.5 * 0.5 * airDensity * 3.14159 * currentVel ** 2

        #calculate the acceleration caused by drag based on F = ma
        self.dragAccel = - (self.drag / self.mass)

        #return the acceleration value caused by drag
        return self.dragAccel


    #decompose the diagonal motion of the shot put into its horizontal and verticle motion
    #These work in the context of each time interval

    #calculate displacement of shot put along y-axis
    def calcYDisplacement(self, elapsedTime, currentDragAccel):
        #calculate the verticle displacement of the shot put
        self.yDisplacement = self.yVel * elapsedTime + ((self.gravityAccel + currentDragAccel) * t**2)/2

        return self.yDisplacement


    #calculate displacement of shot put along y-axis
    def calcXDisplacement(self, elapsedTime, currentDragAccel):
        #calculate the verticle displacement of the shot put
        self.xDisplacement = self.xVel * elapsedTime + ((currentDragAccel) * t**2)/2

        return self.xDisplacement

    #update the y coordinates of the shotPut
    def updateYCoordinates(self, displacement):
        self.y += displacement
        self.yCoordinates.append(self.y)

    #update the x coordinates of the shotPut
    def updateXCoordinates(self, displacement):
        self.x += displacement
        self.xCoordinates.append(self.x)

    def updateYvel(self, currentDragAccel, elapsedTime):
        self.yVel += (currentDragAccel + self.gravityAccel) * elapsedTime

    def updateXvel(self, currentDragAccel, elapsedTime):
        self.xVel += currentDragAccel * elapsedTime




#the coordinates of the shot put can be fed into this function to plot out the graph
def plotGraph(xCoordinates, yCoordinates):
    #plot the graph using all the coordinates calculated previously
    plt.plot(xCoordinates, yCoordinates)

    #label the coordinates of the graph
    plt.xlabel("horizontal distance travelled by projectile")
    plt.ylabel("height of projectile")

    #displays all graphs that have been plotted
    plt.show()


#main() houses core logic of the calculations
def main():

    #create instances of shotPut of launch angles ranging from 1 to 89
    for angle in range(1, 90):
        shotput = shotPut(angle)

        ##INSERT LOGIC HERE

        #plot graph for this instance of shotPut
        plotGraph(shotput.xCoordinates, shotput.yCoordinates)

    #displays all graphs that have been plotted
    plt.show()

main()
