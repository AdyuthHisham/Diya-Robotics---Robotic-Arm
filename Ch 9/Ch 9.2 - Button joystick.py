#Imported packages
##Machine package imports functions required for communicating with the microcontroller
from machine import Pin,ADC
##sleep function is used to put the board to sleep. This is done to give a buffer preventing overloading of data
from time import sleep

#Initialize pins
VRX1 = ADC(Pin(26))  
VRY1 = ADC(Pin(27))

SW1 = Pin(15, Pin.IN, Pin.PULL_UP)

#Global variables
Word1 = "Hiii, the switch is not clickced"
Word2 = "Yay, you clicked the switch"
switch = 0

#Infinite loop
while True:
    print("Flag = ",switch)
    #If button is clicked switch states
    if SW1.value() == 0:
        switch = not switch
    if switch == True:
        print(Word1)
    elif switch == False:
        print(Word2)