#Definition
##from: used for defining package to be imported from
##import: importing package or function(s)
from machine import Pin, ADC
from time import sleep

#Variable for selecting pin number
SensPIN = 8

#Declaring Pin object for obstacle detection sensor
Sens = ADC(Pin(SensPIN,Pin.IN))

#Infinite loop
while True:
    #Display obstacle sensor value
    print(f"Sensor value: {Sens.read_u16()}")
    
    sleep(0.01)
