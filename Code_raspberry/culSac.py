from robotcontrol import *
from time import time


def waitData():
    oldTime = time()
    while not (RobotControl().dataIsReceived):
        currentTime = time()
        if ((currentTime - oldTime) > 1):
            break

def culDeSacSituation():
    robCrl = RobotControl()
    # on tourne le servo à droite (0° étant le repère devant +90° à droite et -90° à gauche)
    robCrl.setArduinoValue(0,0,0,0,90)
    robCrl.sendDataToArduino()



    # on ne laisse le c
    robCrl.setArduinoValue(0,0,0,1,'n')
    rightUsSensor = robCrl.receiveDataFromArduino(Utility.dataRightUsSensor)


