from machine import Pin
from servo import Servo

#Code for hardcode


s1 = Servo(3)

while True:
    angle_value = int(input("Enter angle: "))
    s1.servo_Angle(angle_value)
        
