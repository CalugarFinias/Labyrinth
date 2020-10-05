from utility import Utility

class RobotControl(object):
    """
        Classe permettant de gérer le robot (roues, capteur etc), soit en envoyant des instruction à l'arduino, soit en
            demandant des informations venant des capteurs.
    """
    __dataReceived = 0
    def __init__(self):
        self.__wheelLeftValue = 0
        self.__wheelRightValue = 0
        self.__frontUsSensor = 0
        self.__rightUsSensor = 0
        self.__servoAngle = 0

    def sendDataToArduino(self):
        """
            Fonction permettant d'envoyer les différentes données concernant le controle du robot à l'arduino.
            Elle evnois donc une liste avec une valeur pour chaque composant du robot (roues, capteur etc).
        """
        data = [str(self.__wheelLeftValue),
                str(self.__wheelRightValue),
                str(self.__frontUsSensor),
                str(self.__rightUsSensor),
                str(self.__servoAngle)]

    def receiveDataFromArduino(self, dataType):
        """
            Gère le processus de demande d'informations des différents composants du robot à l'arduino.

            :param dataType: Spécifie le type de données que l'on souhaite recevoir (capteurs des roues, capteurs us etc).
            :return: Retourne la valeur du type voulu de données voulues ( ex : si on met dataWheelLeft ca retourne
                        la donné concernant la roue gauche du robot).
        """
        if(dataType == Utility.dataWheelLeft):
            return 0

        elif(dataType == Utility.dataWheelRight):
            return 0

        elif(dataType == Utility.dataFrontUsSensor):
            return 0

        elif(dataType == Utility.dataRightUsSensor):
            return 0

        else:
            return 0

    def dataIsReceived(self):
        return RobotControl.__dataReceived

#---------------------------------------------------------------------------------------------------------- SET & GET

    def setArduinoValue(self, wheelLeftValue, wheelRightValue, frontUsSensor, rightUsSensor, servoAngle):
        self.__wheelLeftValue = wheelLeftValue
        self.__wheelRightValue = wheelRightValue
        self.__frontUsSensor = frontUsSensor
        self.__rightUsSensor = rightUsSensor
        self.__servoAngle = servoAngle



