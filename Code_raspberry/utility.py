#from robotControl import *
from time import time

"""
def wait(waitTime):
    # si le temps d'attente est trop long, alors c'est qu'il y a un soucis et que l'opération n'a pas été faite correctement.
    oldTime = time()
    while not (RobotControl().dataAreReceived()):
        currentTime = time()
        if ((currentTime - oldTime) > waitTime):
            # si on sort de la boucle après avoir attendu un temps trop long (défini dans waitTime),
            # alors c'est qu'il y a un soucis.

            dataAreReceived = 0
            break
"""
def waitTime(waitTime):
    # si le temps d'attente est trop long, alors c'est qu'il y a un soucis et que l'opération n'a pas été faite correctement.
    oldTime = time()
    while True:
        currentTime = time()
        if ((currentTime - oldTime) > waitTime):
            # si on sort de la boucle après avoir attendu un temps trop long (défini dans waitTime),
            # alors c'est qu'il y a un soucis.
            break

class Utility:
    """
        Variable permettant de sélectionner les données que l'on veut recevoir de l'arduino
    """
    dataWheelLeft = "WheelLeft"
    dataWheelRight = "WheelRight"
    dataUsSensorOnServo = "UsSensorOnServo"
    dataRightUsSensor = "RightUsSensor"
    dataServo = "Servo"
    #--------------------------------------------------------------------------------------------------------------
    # signifie aucun changement pour l'appareil électronique concernant le robot, il doit donc rester à son état précédent.
    noChange = 'n'
