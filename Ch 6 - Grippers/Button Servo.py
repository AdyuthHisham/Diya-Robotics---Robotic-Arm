#Imported packages
##Machine package imports functions required for communicating with the microcontroller
from machine import Pin
##sleep function is used to put the board to sleep. This is done to give a buffer preventing overloading of data
from time import sleep
##From servo, the class Servo is imported that helps make controlling servos easier
from servo import Servo

#PIN VARIABLES
servo_pin = 3
maxPos = 30
minPos = 90
button_1Pin = 10
button_2Pin = 11

#INITIALIZING PIN
s1 = Servo(servo_pin)
button_1 = Pin(button_1Pin,Pin.IN)
button_2 = Pin(button_2Pin,Pin.IN)

#Infinite loop
while True:
    #If button 1 is activated; move to max pos
    if button_1.value():
        s1.servo_Angle(maxPos)
    #If button 2 is activated; move to min pos
    if button_2.value():
        s1.servo_Angle(minPos)