from robotControl import *


# valeur à partir de laquelle on considère qu'il n'y a pas de chemin et donc un mur.
wallDistance = 10


def getDataFromArduino(dataType):
    n = Utility.noChange
    robCrl = RobotControl()   
    # todo 1 : refactorer en fonction des todo 1
    robCrl.setArduinoValue(n, n, n, 0, 0)
    data = robCrl.receiveDataFromArduino(dataType)
    # temps d'attente en secondes pour la réception de données.
    #wait(2)
    return data



def commandMotors(wheelLeft, wheelRight, servo):
    robCrl = RobotControl()
    # todo 1 : refactorer en fonction des todo 1
    robCrl.setArduinoValue(wheelLeft, wheelRight, servo, 0, 0)
    robCrl.sendDataToArduino()
    #wait(2)



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


