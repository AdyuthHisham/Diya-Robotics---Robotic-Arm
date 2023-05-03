#Definition
##from: used for defining package to be imported from
##import: importing package or function(s)
from machine import Pin
from time import sleep

#Initialize Pins
relay = Pin(15, Pin.OUT)
button = Pin(10,Pin.IN)

#Infinite loop
while True:
  #If button is active...
  if button.value():
      #...Activate relay    
      relay.value(1)
  else:
      #Else deactivate relay
      relay.value(0)
