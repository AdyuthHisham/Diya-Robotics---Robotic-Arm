from machine import Pin,ADC
from time import sleep


VRX1 = ADC(Pin(26))  
VRY1 = ADC(Pin(27))

SW1 = Pin(15, Pin.IN, Pin.PULL_UP)

Word1 = "Hiii, the switch is not clickced"
Word2 = "Yay, you clicked the switch"

switch = 0

while True:
    
    print("Flag = ",switch)
    if SW1.value() == 0:
        switch = not switch
    if switch == True:
        print(Word1)
    elif switch == False:
        print(Word2)