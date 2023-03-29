from machine import Pin
from time import sleep

objSensPIN = 8

objSens = Pin(objSensPIN,Pin.IN)

while True:
    print(objSens.value())
    if objSens.value() == 1 :
       print("HIGH")
    else :
       print("LOW")
    sleep(0.01)
