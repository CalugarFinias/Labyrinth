from robotcontrol import *
from time import time

# temps d'attente en secondes pour la fonction waitData.
waitTime = 2
# valeur à partir de laquelle on considère qu'il n'y a pas de chemin et donc un mur.
wall = 10


def waitData():
    """
        Fonction attendant un certains moment que l'arduino ait envoyé des données et donc la fonction dataAreReceived
            renvoit 1.
    """
    oldTime = time()
    dataAreReceived = 1
    while not (RobotControl().dataAreReceived()):
        currentTime = time()
        if ((currentTime - oldTime) > waitTime):
            # si on sort de la boucle après avoir attendu un temps trop long (défini dans waitTime),
            # alors c'est qu'il y a un soucis.
            dataAreReceived = 0
            break
    return dataAreReceived

def getDataFromArduino():
    robCrl = RobotControl()

    # on tourne le servo à droite (0° étant le repère devant +90° à droite et -90° à gauche).
    robCrl.setArduinoValue(0, 0, 0, 0, 90)
    robCrl.sendDataToArduino()
    dataAreReceived = waitData()
    # si le temps d'attente est trop long, alors c'est qu'il y a un soucis et que l'opération n'a pas été faite correctement.
    if not (dataAreReceived):
        operationIsWellExecuted = 0


def culDeSacSituation():
    # variable permettant de vérifier si culDeSacSituation a bien été exécuté.
    operationIsWellExecuted = 1
    # informe s'il y a un chemin sur la droite = 1, ou pas = 0.
    pathOnRight = 0

    getDataFromArduino()

    robCrl = RobotControl()

    # on tourne le servo à droite (0° étant le repère devant +90° à droite et -90° à gauche).
    robCrl.setArduinoValue(0, 0, 0, 0, 90)
    robCrl.sendDataToArduino()
    dataAreReceived = waitData()
    # si le temps d'attente est trop long, alors c'est qu'il y a un soucis et que l'opération n'a pas été faite correctement.
    if not (dataAreReceived):
        operationIsWellExecuted = 0
        
    # on laisse le servo dans sa position en lui indiquant "n" (none), et on active l'us sensor de devant.
    robCrl.setArduinoValue(0,0,1,0,Utility.noChange)
    robCrl.sendDataToArduino()
    dataAreReceived = waitData()
    if not (dataAreReceived):
        operationIsWellExecuted = 0

    rightUsSensor = robCrl.receiveDataFromArduino(Utility.dataRightUsSensor)

    if (rightUsSensor > wall):
        pathOnRight = 1



    return [operationIsWellExecuted, pathOnRight]


