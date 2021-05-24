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
        self.dragCoeff = 0.07

        #take the density of air at sea level at 15 degrees Celsius as 1.225kg/m^3
        self.airDensity = 1.225

        #create a variable to hold the current velocity value of the shot put
        #at the point where this object is created, set the velocity to its launch velocity
        self.currentVel = 13.72

        #calulate the verticle velocity of the shot at launch put using trigonometric ratios
        #math.sin accepts values only in radians
        self.yVel = self.currentVel * math.sin(math.radians(launchAngle))

        #calulate the horizontal velocity of the shot put at launch using trigonometric ratios
        #math.cos accepts values only in radians
        self.xVel = self.currentVel * math.cos(math.radians(launchAngle))

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
        self.drag = 0.5 * self.dragCoeff * self.airDensity * 3.14159 * currentVel ** 2

        #calculate the acceleration caused by drag based on F = ma
        self.dragAccel = - (self.drag / self.mass)

        #return the acceleration value caused by drag
        return self.dragAccel


    #decompose the diagonal motion of the shot put into its horizontal and verticle motion
    #These work in the context of each time interval

    #calculate displacement of shot put along y-axis
    def calcYDisplacement(self, elapsedTime, currentDragAccel):
        #calculate the verticle displacement of the shot put
        self.yDisplacement = self.yVel * elapsedTime + ((self.gravityAccel + currentDragAccel) * elapsedTime**2)/2

        return self.yDisplacement


    #calculate displacement of shot put along y-axis
    def calcXDisplacement(self, elapsedTime, currentDragAccel):
        #calculate the verticle displacement of the shot put
        self.xDisplacement = self.xVel * elapsedTime + ((currentDragAccel) * elapsedTime**2)/2

        return self.xDisplacement

    #update the y coordinates of the shotPut
    def updateYCoordinates(self, displacement):
        self.y += displacement
        #append the new coordinate into the list of coordinates
        self.yCoordinates.append(self.y)

    #update the x coordinates of the shotPut
    def updateXCoordinates(self, displacement):
        self.x += displacement
        #append the new coordinate into the list of coordinates
        self.xCoordinates.append(self.x)

    def updateYvel(self, currentDragAccel, elapsedTime):
        self.yVel += (currentDragAccel + self.gravityAccel) * elapsedTime

    def updateXvel(self, currentDragAccel, elapsedTime):
        self.xVel += currentDragAccel * elapsedTime




#the coordinates of the shot put can be fed into this function to plot out the graph
def plotGraph(xCoordinates, yCoordinates, *args):
    #plot the graph using all the coordinates calculated previously
    plt.plot(xCoordinates, yCoordinates)

    #label the coordinates of the graph
    plt.xlabel("horizontal distance travelled by projectile")
    plt.ylabel("height of projectile")


#main() houses core logic of the calculations
def main():

    #time interval between each plot = 0.00001s
    timeInterval = 0.001

    #create a blank list of launch angles to be written to to create legend later
    angleList = []

    #create instances of shotPut of launch angles ranging from 1 to 89
    for angle in range(35, 46):
        shotput = shotPut(angle)

        #append the new angle into the list
        angleList.append(str(angle) + "°")

        ##INSERT LOGIC HERE
        #initialise time value
        t = 0

        #continue loop if shotput has not touched the ground yet
        while shotput.y > 0:
            #calculate the deceleration caused by drag along the y-axis
            YDragDecel = shotput.calcDragDecel(shotput.yVel)

            #update the yVel for the next calculation loop
            shotput.updateYvel(YDragDecel, timeInterval)

            #calculate the deceleration caused by drag along the y-axis
            XDragDecel = shotput.calcDragDecel(shotput.xVel)

            #update the xVel for the next calculation loop
            shotput.updateXvel(XDragDecel, timeInterval)

            #calculate the displacement of the shotPut on the Y axis
            yDisplacement = shotput.calcYDisplacement(timeInterval, YDragDecel)

            #update the Y coordinate of shotPut and append to list of coordinates
            shotput.updateYCoordinates(yDisplacement)

            #display the y coordinate
            #print(shotput.y, end="")

            #calculate the displacement of the shotPut on the X axis
            xDisplacement = shotput.calcXDisplacement(timeInterval, YDragDecel)

            #update the X coordinate of shotPut and append to list of coordinates
            shotput.updateXCoordinates(xDisplacement)

            #display the x coordinate
            #print(shotput.x, end="")

            #update t value
            t += timeInterval



        #plot graph for this instance of shotPut
        plotGraph(shotput.xCoordinates, shotput.yCoordinates, shotput)

    #plot the ground
    plotGraph([0, 17.5], [0, 0])

    #Add the ground to the legend
    angleList.append("Ground")

    #plot start point
    plotGraph([0, 0], [0, 7])

    #Add the ground to the legend
    angleList.append("Start")

    #Create the legend for the graphs
    plt.legend(angleList, loc="upper right")

    #displays all graphs that have been plotted
    plt.show()

#call the main() function to start the program
main()
