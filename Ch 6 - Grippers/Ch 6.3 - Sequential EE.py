#Definition
##from: used for defining package to be imported from
##import: importing package or function(s)
from machine import Pin
from servo import Servo

#Define s1 as object of class Servo
s1 = Servo(3)

#Infinite loop
while True:
    #Enter angle
    angle_value = int(input("Enter angle: "))
    #Move servo to read angle value
    s1.servo_Angle(angle_value)
        
