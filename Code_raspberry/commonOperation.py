from robotControl import RobotControl
from utility import Utility


# valeur à partir de laquelle on considère qu'il n'y a pas de chemin et donc un mur.
wallDistance = 10


def getDataFromArduino(dataType):
    robCrl = RobotControl()
    return robCrl.requestDataFromArduino(dataType)



def commandMotors(wheelLeft, wheelRight):
    n = Utility.noChange
    robCrl = RobotControl()
    robCrl.sendDataToArduino(wheelLeft, wheelRight, n, n, n)



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


