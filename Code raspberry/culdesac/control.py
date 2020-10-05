

class Control():
    def __init__(self, wheelLeftValue, wheelRightValue, frontUsSensor, rightUsSensor, servoAngle):
        self.__wheelLeftValue = wheelLeftValue
        self.__wheelRightValue = wheelRightValue
        self.__frontUsSensor = frontUsSensor
        self.__rightUsSensor = rightUsSensor
        self.__servoAngle = servoAngle
        
    def electronicListValues(self):
        return [self.__wheelLeftValue, 
                self.__wheelRightValue, 
                self.__frontUsSensor, 
                self.__rightUsSensor, 
                self.__servoAngle]


