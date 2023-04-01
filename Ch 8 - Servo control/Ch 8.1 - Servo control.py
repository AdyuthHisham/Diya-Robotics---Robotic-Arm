#Imported packages
##Machine package imports functions required for communicating with the microcontroller
from machine import Pin
##sleep function is used to put the board to sleep. This is done to give a buffer preventing overloading of data
from time import sleep
##From servo, the class Servo is imported that helps make controlling servos easier
from servo import Servo

#PIN VARIABLES
servo_pin = None
maxPos = None
minPos = None

#INITIALIZING PIN
s1 = Servo(servo_pin)

#Infinite loop
while True:
    s1.servo_Angle(maxPos)
    sleep(1)
    s1.servo_Angle(minPos)
    sleep(1)