

class Utility:
    """
        Variable permettant de sélectionner les données que l'on veut recevoir de l'arduino
    """
    dataWheelLeft = "WheelLeft"
    dataWheelRight = "WheelRight"
    dataFrontUsSensor = "FrontUsSensor"
    dataRightUsSensor = "RightUsSensor"
    dataServo = "Servo"
    #-----------------------------------------------
    # signifie aucun changement pour le capteur, appareil du robot, il doit donc rester à son état précédent.
    noChange = 'n'
