from robotControl import *
from time import time


# valeur à partir de laquelle on considère qu'il n'y a pas de chemin et donc un mur.
wallDistance = 10


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

def getDataFromArduino(dataType):
    robCrl = RobotControl()
    data = robCrl.receiveDataFromArduino(dataType)
    # temps d'attente en secondes pour la réception de données.
    wait(2)
    return data



def commandMotors(wheelLeft, wheelRight, servo):
    robCrl = RobotControl()
    robCrl.setMotorsValue(wheelLeft, wheelRight, servo)#, arduinoDataList[2], arduinoDataList[3], arduinoDataList[4])
    robCrl.sendDataToArduino()
    wait(2)



def culDeSacSituation():
    n = Utility.noChange
    # informe s'il y a un chemin sur la droite = 1, ou pas = 0.
    pathOnRight = 0
    # informe s'il y a un chemin sur la gauche = 1, ou pas = 0.
    pathOnLeft = 0
    # on arrête le robot en mettant à 0 les moteurs.
    commandMotors(0,0,n)
    if (getDataFromArduino(Utility.dataRightUsSensor) > wallDistance):
        pathOnRight = 1

    # on tourne le servo à gauche (0° étant le repère devant, +1 = 90° à droite et -1 = 90° à gauche).
    commandMotors(0,0,-1)
    if (getDataFromArduino(Utility.dataUsSensorOnServo) > wallDistance):
        pathOnRight = 1

    return [pathOnRight, pathOnLeft]


