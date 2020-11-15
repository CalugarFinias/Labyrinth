from utility import *
import serial
from time import time


class RobotControl(object):
    """
        Classe permettant de gérer le robot (roues, capteur etc), soit en envoyant des instruction à l'arduino, soit en
            demandant des informations venant des capteurs.
    """
    def __init__(self):
        self.__wheelLeftValue = 0
        self.__wheelRightValue = 0
        self.__frontUsSensor = 0
        self.__rightUsSensor = 0

    def sendDataToArduino(self, wheelLeftValue, wheelRightValue, frontUsSensor, rightUsSensor):
        """
            Fonction permettant d'envoyer les différentes données concernant le controle du robot à l'arduino.
            Elle evnois donc une liste avec une valeur pour chaque composant du robot (roues, capteur etc).
        """
        self.__wheelLeftValue = wheelLeftValue
        self.__wheelRightValue = wheelRightValue
        self.__frontUsSensor = frontUsSensor
        self.__rightUsSensor = rightUsSensor
        arduinoConn = ArduinoConnexion()
        arduinoConn.sendData([str(self.__wheelLeftValue),
                            str(self.__wheelRightValue),
                            str(self.__frontUsSensor),
                            str(self.__rightUsSensor)])

    def requestDataFromArduino(self, dataType):
        """
            Gère le processus de demande d'informations des différents composants du robot à l'arduino.
            :param dataType: Spécifie le type de données que l'on souhaite recevoir (capteurs des roues, capteurs us etc).
            :return: Retourne la valeur du type voulu de données voulues ( ex : si on met dataWheelLeft ca retourne
                        la donné concernant la roue gauche du robot).
        """
        identificationCode = ' '
        if(dataType == Utility.dataWheelLeft):
            identificationCode = 'w'

        elif(dataType == Utility.dataWheelRight):
            identificationCode = 'x'

        elif(dataType == Utility.dataFrontUsSensor):
            identificationCode = 'u'

        elif(dataType == Utility.dataRightUsSensor):
            identificationCode = 'i'

        arduinoConn = ArduinoConnexion()
        arduinoConn.sendData(identificationCode)
        return arduinoConn.readData()

#============================================================================================== SET & GET



class ArduinoConnexion(object):
    """
        Class permettant de créer une connexion série avec le robot.
    """
    def __init__(self, periph = "/dev/ttyACM0", baudrate = 9600):
        self.__serial = serial.Serial(periph, baudrate)

    def sendData(self, data):
        # Encode en binaire chaque éléments de data séparément pour l'envoyer
        # à l'arduino car impossible de faire cette opération sur toute une liste en même temps.
        self.__serial.write([e.encode() for e in data])
        # todo 1 : voir si on ne doit pas mettre de fonction close
    """
    def readData(self, waitTime = 2):
        
            Fonction permettant la lecture de données via le port com, attend un certain temps
            la lecture sur le port com et s'arrête pour renvoyer le résultat.
        :param waitTime: Temps d'attente de la réception des données au dela de laquelle
                            elle s'arrête si rien n'a été recu après ce laps de temps en secondes.
        :return: Renvois les données recues ou 0 si il y a eu un problèmes et que rien n'a été recu.
        
        data = 0
        oldTime, currentTime = time(), time()
        # Si le temps d'attente est trop long, alors c'est qu'il y a un soucis et que l'opération
        # n'a pas été faite correctement.
        # todo 1 : voir si on ne doit pas mettre de fonction close
        while ((currentTime - oldTime) > waitTime):
            currentTime = time()
            if (self.__serial.in_waiting > 0):
                data = self.__serial.readline().decode('utf-8').rstrip()
                break

        if (currentTime - oldTime) > waitTime:
            raise Exception('temps d\'attente écoulé, wait time = ' + str(waitTime))
        if data == 0:
            raise Exception('les données n\'ont pas été reçues, data = ' + data)

        return data
    """

    def readData(self):
        """
        Fonction permettant de recevoir les données de l'arduino.
        :return: Renvois une liste contenant toutes les données de l'arduino.
        """
        return self.__serial.readline().decode('utf-8').rstrip().split()
