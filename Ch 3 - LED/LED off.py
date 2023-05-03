#Importing function Pin from package machine for manipulating Pins on board
from machine import Pin

#Declaring object p2 for LED
#Onboard LED can be initialized using the "LED" keyword
p2=Pin("LED",Pin.OUT)

#To run loop infinitely
while True:
    #To turn on LED
    p2.off()


