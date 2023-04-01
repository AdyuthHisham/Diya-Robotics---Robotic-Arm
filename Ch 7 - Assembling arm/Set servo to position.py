#Imported packages
##From servo, the class Servo is imported that helps make controlling servos easier
from servo import Servo

#PIN VARIABLES
servo_pin = 3
Pos = 90

#INITIALIZING PIN
s1 = Servo(servo_pin)

#Set position of servo angle
s1.servo_Angle(Pos)