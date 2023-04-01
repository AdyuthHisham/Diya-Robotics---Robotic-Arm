#Definition
##from: used for defining package to be imported from
##import: importing package or function(s)

#PWM function is used for working with Pulse Width Modulation
from machine import Pin,PWM
import time

#Declaring objects

smoke = Pin(28,Pin.IN)
##Buzzer is an object of type PWM used for Pin 7
buzzer = PWM(Pin(7))
##Frquency of PWM is set to 500
buzzer.freq(500)

#Infinite loop
while True:
    #Display smoke sensor value
    print("Smoke: ",smoke.value())
    #If smoke sensor detects smoke...
    if(smoke.value() == 0):
        print("Activating sprinkler system")
        #Activate buzzer
        ##By setting duty cycle as 1000
        buzzer.duty_u16(1000)
        time.sleep(1)
        buzzer.duty_u16(0)
        
    time.sleep(0.2)