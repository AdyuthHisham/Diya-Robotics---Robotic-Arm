from time import sleep
from servo import Servo
import servo
from machine import Pin
#INITIALIZING PINS
#Front and Back
s1 = Servo(7)
#Left and Right
s2 = Servo(8)
#Up and Down
s3 = Servo(9)
#End effector
s4 = Servo(9)

s1.middle()
sleep(2)
s2.middle()
sleep(2)
s3.middle()
sleep(2)
s4.middle()
sleep(2)

s1Pos = 90
s2Pos = 90
s3Pos = 90
s4Pos = 90

button = Pin(10)

switch = 0

while True:
    if button.value() == 1:
        switch = not switch
    print("Switch = ",switch)
    keyword = input("Give input:")
    if switch == 0:
        if keyword == 'w':
            print("Command: FRONT")
            s2Pos = s2Pos + 5
            s2.servo_Angle(s2Pos)
            print(s2Pos)
        elif keyword == 'a':
            print("Command: LEFT")
            s1Pos = s1Pos + 5
            s1.servo_Angle(s1Pos)
            print(s1Pos)
        elif keyword == 's':
            print("Command: BACK")
            s2Pos = s2Pos - 5
            s2.servo_Angle(s2Pos)
            print(s2Pos)
        elif keyword == 'd':
            print("Command: RIGHT")
            s1Pos = s1Pos - 5
            s1.servo_Angle(s1Pos)
            print(s1Pos)
    elif switch == 1:
        if keyword == 'w':
            print("Command: UP")
            s3Pos = s3Pos + 5
            s3.servo_Angle(s3Pos)
            print(s3Pos)
        elif keyword == 'a':
            print("Command: EE OPEN")
            s4Pos = s4Pos + 5
            s4.servo_Angle(s4Pos)
            print(s4Pos)
        elif keyword == 's':
            print("Command: DOWN")
            s3Pos = s3Pos - 5
            s3.servo_Angle(s3Pos)
            print(s3Pos)
        elif keyword == 'd':
            print("Command: EE CLOSE")
            s4Pos = s4Pos - 5
            s4.servo_Angle(s4Pos)
            print(s4Pos)
    if keyword == 'e':
        s1.deinit()
    
        s2.deinit()
        
        s3.deinit()
        
        s4.deinit()
        
        break


        
