#Definition
##from: used for defining package to be imported from
##import: importing package or function(s)
from machine import Pin
from time import sleep

#Variable for selecting pin number
objSensPIN = 8

#Declaring Pin object for obstacle detection sensor
objSens = Pin(objSensPIN,Pin.IN)

#Infinite loop
while True:
    
    #Display obstacle sensor value
    print(objSens.value())
    #If sensor detects something...
    if objSens.value() == 1 :
       print("HIGH")
    #Else if it detects nothing
    else :
       print("LOW")
    #Sleep for 0.01 seconds to prevent overloading of data too the board
    sleep(0.01)
