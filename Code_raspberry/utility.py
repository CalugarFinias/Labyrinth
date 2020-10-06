

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
