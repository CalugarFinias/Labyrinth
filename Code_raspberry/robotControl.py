from utility import *
import serial


class RobotControl(object):
    """
        Classe permettant de gérer le robot (roues, capteur etc), soit en envoyant des instruction à l'arduino, soit en
            demandant des informations venant des capteurs.
    """
    __dataAreReceived = 0

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
        # todo 1 : régler le fonclit entre receive data et cette fonction, définir clairement qui fait quoi
        arduinoConn = ArduinoConnexion()
        arduinoConn.sendData([str(self.__wheelLeftValue),
                            str(self.__wheelRightValue),
                            str(self.__frontUsSensor),
                            str(self.__rightUsSensor),
                            str(self.__servoAngle)])


    def receiveDataFromArduino(self, dataType):
        """
            Gère le processus de demande d'informations des différents composants du robot à l'arduino.
            :param dataType: Spécifie le type de données que l'on souhaite recevoir (capteurs des roues, capteurs us etc).
            :return: Retourne la valeur du type voulu de données voulues ( ex : si on met dataWheelLeft ca retourne
                        la donné concernant la roue gauche du robot).
        """
        # todo 1 : pareil que pour l'autre 1
        identificationCode = ' '
        if(dataType == Utility.dataWheelLeft):
            identificationCode = 'w'

        elif(dataType == Utility.dataWheelRight):
            identificationCode = 'x'

        elif(dataType == Utility.dataFrontUsSensor):
            identificationCode = 'u'

        elif(dataType == Utility.dataRightUsSensor):
            identificationCode = 'i'

        else:
            identificationCode = 's'

        arduinoConn = ArduinoConnexion()
        arduinoConn.sendData(identificationCode)
        return arduinoConn.readData()


    def dataAreReceived(self):
        """
            Permet de savoir si des données on été recue de larduino.
        :return: 1 si des données sont recues, 0 sinon.
        """
        return RobotControl.__dataAreReceived
#---------------------------------------------------------------------------------------------------------- SET & GET
    def setArduinoValue(self, wheelLeftValue, wheelRightValue, servoAngle, frontUsSensor, rightUsSensor):
        self.__wheelLeftValue = wheelLeftValue
        self.__wheelRightValue = wheelRightValue
        self.__servoAngle = servoAngle
        self.__frontUsSensor = frontUsSensor
        self.__rightUsSensor = rightUsSensor




class ArduinoConnexion(object):
    """
        Class permettant de créer une connexion série avec le robot.
    """
    def __init__(self, periph = "/dev/ttyACM0", baudrate = 9600):
        self.__serial = serial.Serial(periph, baudrate)


    def sendData(self, data):
        while waitTime(2):
            if (self.__serial.in_waiting > 0):
                for element in data:
                    self.__serial.write(element.encode())
                break
        self.__serial.close()


    def readData(self):
        return self.__serial.readline().decode('utf-8').rstrip()

