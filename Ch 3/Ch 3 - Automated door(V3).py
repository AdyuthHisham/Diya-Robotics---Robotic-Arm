from machine import Pin
from time import sleep
from servo import Servo

#Initializing Pins
##Pin number of object sensor
objSensPIN = 8
##Declaration of Object sensor
objSens = Pin(objSensPIN,Pin.IN)
##Declaration of Servo
s1 = Servo(3)

    
while True:
    ##If sensor detects object
    ##Door closes
    print(objSens.value())
    if objSens.value() == 1 :
       print("Door closed")
       s1.servo_Angle(50)
    else :
       print("Door open")
       s1.servo_Angle(170)