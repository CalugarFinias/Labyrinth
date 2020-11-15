import serial
import re
import time

periph = '/dev/ttyACM0'
baudrate = 9600
ser = serial.Serial(periph, baudrate)
to_arduino_a= 'a'
to_arduino_b= 'b'
maximum_distance = 15
distance_left=15
distance_right=15

def proximityTrigger(distance_left, distance_right) :
    #print(distance_left)
    #print(distance_right)
    if distance_left <= 6 and distance_right <=6 :
        print("Allumé")
        ser.write(to_arduino_a.encode())      
    else:
        print("Eteint")
        ser.write(to_arduino_b.encode())      
        

while True:
    while ser.in_waiting:
        line=ser.readline().decode('utf-8').rstrip()
        print(line)
        #if len(line)>1: #if this is not a or b (message from the pi to the arduino)
        line_split=line.split()
        if line_split[0]=='left' and int(line_split[1]) < maximum_distance:
            distance_left=int(line_split[1])
        if line_split[2]=='right' and int(line_split[3]) < maximum_distance:
            distance_right=int(line_split[1])
        proximityTrigger(distance_left, distannce_right)
        #time.sleep(0.2)