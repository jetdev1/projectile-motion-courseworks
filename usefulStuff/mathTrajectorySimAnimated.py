import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class Shot:
    def __init__(self, launchAngle):
        self.currentVel = 13.72
        self.currentVelY = self.currentVel * math.sin(math.radians(launchAngle))
        self.currentVelX = self.currentVel * math.cos(math.radians(launchAngle))
        #print(self.currentVelX, self.currentVelY)
        self.gravityAccel = -9.81
        self.launchAngle = launchAngle
        self.y = 2.1
        self.x = 0
        self.xCoordinates = [0]
        self.yCoordinates = [2.1]

    def animate(self, time):
        t = time / timeInterval
        self.xDisplacement = self.currentVelX * t
        self.x = 0 + self.xDisplacement
        self.xCoordinates.append(self.x)
        line.set_xdata(self.xCoordinates)

        self.yDisplacement = self.currentVelY * t + (self.gravityAccel * t**2)/2
        self.y = 2.1 + self.yDisplacement
        self.yCoordinates.append(self.y)
        line.set_ydata(self.yCoordinates)
        return line,

def main():
    global line
    global x
    global timeInterval
    timeInterval = 500
    fig, ax = plt.subplots()

    shot = Shot(42)
    line = ax.plot(shot.xCoordinates, shot.yCoordinates)[0]
    ax.set(xlim=(0, 30), ylim=(0, 12))

    ani = animation.FuncAnimation(
    fig, shot.animate, interval=1, blit=True, save_count=50
    )
    plt.show()




if __name__=="__main__":
    main()
