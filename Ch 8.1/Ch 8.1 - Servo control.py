from machine import Pin
from time import sleep
from servo import Servo

servo_pin = None
maxPos = None
minPos = None

s1 = Servo(servo_pin)

while True:
    s1.servo_Angle(maxPos)
    sleep(1)
    s1.servo_Angle(minPos)
    sleep(1)