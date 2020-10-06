import serial

periph = '/dev/ttyACM0'

baudrate = 9600

ser = serial.Serial(periph, baudrate)
toArduino='E'
toArduinoEncode = toArduino.encode() #traduction en bytes pour passer par le canal série

maximumDistance = 30
# def proximityFilter(distance) :


while True:
    if(ser.in_waiting > 0):
        line=ser.readline().decode('utf-8').rstrip() 
        if int(line) < maximumDistance:
            print(line) #print ce qu'il recoit du Arduino
        ser.write(toArduinoEncode) #envoie 'E' en bytes à l'arduino