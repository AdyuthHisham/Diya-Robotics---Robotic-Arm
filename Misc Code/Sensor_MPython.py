'''
from machine import Pin
import utime
from time import sleep
from machine import PWM

#Pinouts
Pin_S0 = 4
Pin_S1 = 5
Pin_S2 = 6
Pin_S3 = 7
Pin_sensorOut = 8

#Frequency variables
frequency = 0
R = 0
G = 0
B = 0

S0 = Pin(Pin_S0, Pin.IN)
S1 = Pin(Pin_S1, Pin.IN)
S2 = Pin(Pin_S2, Pin.IN)
S3 = Pin(Pin_S3, Pin.IN)
sensorOut = Pin(Pin_sensorOut, Pin.OUT)

S0.value(1)
S1.value(0)

while True:
    S2.value(0)
    S3.value(0)

    print(f"R = {sensorOut.value()}")

'''

from machine import Pin, PWM,ADC
import time
#from pulse_widthfunc import edge_pulse_width as epw

S0 = Pin(4, Pin.IN)
S1 = Pin(5, Pin.IN)
S2 = Pin(6, Pin.IN)
S3 = Pin(7, Pin.IN)
sensorOut = Pin(26, Pin.OUT)
sensOutPWM = PWM(sensorOut)

frequency = 0
R = 0
G = 0
B = 0

def setup():
    S0.value(1)
    S1.value(0)

print("Serial communication initiated")

def loop():
    S2.value(0)
    S3.value(0)
    #frequency = epw(sensorOut)
    time.sleep_ms(100)
    frequency = sensOutPWM.freq()
    print("R = ", frequency)

'''
    S2.value(1)
    S3.value(1)

    frequency = epw(sensorOut)
    time.sleep_ms(100)
    print("G = ", frequency)
    G = frequency

    S2.value(0)
    S3.value(1)

    frequency = epw(sensorOut)
    time.sleep_ms(100)
    print("B = ", frequency)
    B = frequency

    if (R < 64):
        print("Colour Red")
    elif (G < 63):
        print("Colour Green")
    elif (B < 64):
        print("Colour Blue")
'''
setup()

while True:
    loop()
