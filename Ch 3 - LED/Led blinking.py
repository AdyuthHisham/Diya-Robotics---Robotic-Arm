#Importing function Pin from package machine for manipulating Pins on board
from machine import Pin
#Importing package time for using sleep function for making board go to sleep for certain duration
import time

#Declaring object p2 for LED
#Onboard LED can be initialized using the "LED" keyword
p2=Pin(10,Pin.OUT)

#To run loop infinitely
while True:
    #Turn on LED
    p2.on()
    #Make Pico go to sleep for 0.5 seconds
    time.sleep(0.5)
    #Turn off LED
    p2.off()
    #Make Pico go to sleep for 0.5 seconds
    time.sleep(0.5)