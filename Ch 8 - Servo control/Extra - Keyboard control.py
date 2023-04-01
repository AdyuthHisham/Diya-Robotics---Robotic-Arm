#IMPORING PACKAGES
from time import sleep
from servo import Servo
from machine import Pin

#INITIALIZING PINS
#Front and Back
s1 = Servo(18)
#Left and Right
s2 = Servo(20)
#Up and Down
s3 = Servo(19)
#End effector
s4 = Servo(21)
#Button
button = Pin(10)

#DECLARING VARIABLES FOR SETTING SERVO POSITIONS
s1Pos = 90
s2Pos = 60
s3Pos = 55
s4Pos = 90

#SETTING ALL SERVOS TO MID POSITION
s1.servo_Angle(s1Pos)
sleep(2)
s2.servo_Angle(s2Pos)
sleep(2)
s3.servo_Angle(s3Pos)
sleep(2)
s4.servo_Angle(s4Pos)
sleep(2)

#VARIABLE FOR SWITCHING SERVO CONTROL
switch = 0

#Infinite loop
while True:
    #Switch control when button is pressed
    if button.value() == 1:
        switch = not switch
    print("Switch = ",switch)
    #Read keyboard input
    keyword = input("Give input:")
    if switch == 0:
        #Perform movement based on input
        if keyword == 'w':
            print("Command: UP")
            s2Pos = s2Pos + 5
            s2.servo_Angle(s2Pos)
            print(s2Pos)
        elif keyword == 's':
            print("Command: DOWN")
            s2Pos = s2Pos - 5
            s2.servo_Angle(s2Pos)
            print(s2Pos)    
        elif keyword == 'a':
            print("Command: LEFT")
            s1Pos = s1Pos + 5
            s1.servo_Angle(s1Pos)
            print(s1Pos)
        elif keyword == 'd':
            print("Command: RIGHT")
            s1Pos = s1Pos - 5
            s1.servo_Angle(s1Pos)
            print(s1Pos)
    elif switch == 1:
        if keyword == 'w':
            print("Command: FRONT")
            s3Pos = s3Pos + 5
            s3.servo_Angle(s3Pos)
            print(s3Pos)
        elif keyword == 's':
            print("Command: BACK")
            s3Pos = s3Pos - 5
            s3.servo_Angle(s3Pos)
            print(s3Pos)
        elif keyword == 'a':
            print("Command: EE OPEN")
            s4Pos = s4Pos + 5
            s4.servo_Angle(s4Pos)
            print(s4Pos)
        elif keyword == 'd':
            print("Command: EE CLOSE")
            s4Pos = s4Pos - 5
            s4.servo_Angle(s4Pos)
            print(s4Pos)
    #Deinitialize servo motors for free control
    if keyword == 'e':
        s1.deinit()
    
        s2.deinit()
        
        s3.deinit()
        
        s4.deinit()
        
        break


        
