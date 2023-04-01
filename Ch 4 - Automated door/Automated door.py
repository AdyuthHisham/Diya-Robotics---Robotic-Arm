#Definition
##from: used for defining package to be imported from
##import: importing package or function(s)
from machine import Pin
from time import sleep

#importing custom package servo
from servo import Servo

#Variable for storing pin number
objSensPIN = 8

#Declaring an object of type Servo
##Servo is a class defined in the package servo.py
s1 = Servo(3)

#Declaring Pin object for Object Sensor
objSens = Pin(objSensPIN,Pin.IN)

#Infinite loop
while True:
    #Print value obtained from object sensor
    print(objSens.value())
    #If objSens detects something..
    if objSens.value() == 1 :
       print("Door closed")
       #..Close door
       s1.servo_Angle(50)
    #Else..
    else :
        print("Door open")
        #Keep door closed
        s1.servo_Angle(170)