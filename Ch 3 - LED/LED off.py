#Importing function Pin from package machine for manipulating Pins on board
from machine import Pin

#Declaring object p2 for LED
#Onboard LED is connected to Pin 25
p2=Pin("LED",Pin.OUT)

#To run loop infinitely
while True:
    #To turn on LED
    p2.off()


