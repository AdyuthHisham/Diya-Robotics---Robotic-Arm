#Imported packages
##Machine package imports functions required for communicating with the microcontroller
from machine import Pin,ADC
##sleep function is used to put the board to sleep. This is done to give a buffer preventing overloading of data
from time import sleep
##From servo, the class Servo is imported that helps make controlling servos easier
from servo import Servo,Map

#Initialize pins

gyro_x = ADC(Pin(26,Pin.IN))
gyro_y = ADC(Pin(27,Pin.IN))
gyro_z = ADC(Pin(28,Pin.IN))

LED1 = Pin(9,Pin.OUT)
LED2 = Pin(8,Pin.OUT)
#Global variables

XLim_min = 450
YLim_min = 430
    
XLim_max = 560 
YLim_max = 600

while True:
    #Read X,Y and Z values and Map from 0 to 1024
    XPos = Map(gyro_x.read_u16(),0,65535,0,1024)
    YPos = Map(gyro_y.read_u16(),0,65535,0,1024)
    print(f"{XPos} : {YPos}")

    #Perform movement if criteria is satisfied
    if XPos > XLim_max:
        print("LED1 ON")
        LED1.value(1)
    if YPos < YLim_min:
        print("LED2 OFF")
        LED2.value(0)
    if YPos > YLim_max:
        print("LED2 ON")
        LED2.value(1)
    if XPos < XLim_min:
        print("LED1 OFF")
        LED1.value(0)
    
    sleep(1.0)
