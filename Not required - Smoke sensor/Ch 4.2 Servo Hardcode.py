#Definition
##from: used for defining package to be imported from
##import: importing package or function(s)
from machine import Pin
from servo import Servo

#Declaring object s1 of class Servo at Pin 3
s1 = Servo(3)

#Variable for storing angle value
angle_value = 90
#servo_Angle function is used to set a specific angle for object s1
s1.servo_Angle(angle_value)
        

