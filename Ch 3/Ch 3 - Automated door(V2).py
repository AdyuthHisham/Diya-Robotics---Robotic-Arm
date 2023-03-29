from machine import Pin
import utime
from time import sleep
from servo import Servo
from machine import PWM

obSensPIN = 8

obSens = Pin(obSensPIN,Pin.IN)

s1 = Servo(3)

def Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def servo_Angle(angle):
    s1.goto(round(Map(angle,0,180,0,1024)))
    
while True:
    print(obSens.value())
    if obSens.value() == 1 :
       print("Door closed")
       servo_Angle(10)
    else :
       print("Door open")
       servo_Angle(170)