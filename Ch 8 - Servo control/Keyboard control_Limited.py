#IMPORING PACKAGES
from time import sleep
from servo import Servo

#INITIALIZING PINS
#Front and Back
s1 = Servo(18)
#Left and Right
s2 = Servo(19)
#Up and Down
s3 = Servo(20)
#End effector
s4 = Servo(21)

#DECLARING VARIABLES FOR SETTING SERVO POSITIONS
s1Pos_min = 10
s1Pos_max = 180
s2Pos_min = 0
s2Pos_max = 180

#DECLARING VARIABLES FOR SETTING SERVO POSITIONS
s1Pos = 90
s2Pos = 90
s3Pos = 90
s4Pos = 90

#SETTING ALL SERVOS TO MID POSITION
s1.servo_Angle(s1Pos)
sleep(0.5)
s2.servo_Angle(s2Pos)
sleep(0.5)
s3.servo_Angle(s3Pos)
sleep(0.5)
s4.servo_Angle(s4Pos)
sleep(0.5)

#Infinite loop
while True:
    #Read keyboard input
    keyword = input("Give input:")
    #Perform movement based on input
    if keyword == 'w':
        print("Command: UP")
        s2Pos = s2Pos + 5
        if s2Pos > s2Pos_max:
            s2Pos = s2Pos_max
        s2.servo_Angle(s2Pos)
        print(s2Pos)
    elif keyword == 's':
        print("Command: DOWN")
        s2Pos = s2Pos - 5
        if s2Pos < s2Pos_min:
            s2Pos = s2Pos_min
        s2.servo_Angle(s2Pos)
        print(s2Pos)
        
    elif keyword == 'a':
        print("Command: LEFT")
        s1Pos = s1Pos + 5
        if s1Pos > s1Pos_max:
            s1Pos = s1Pos_max
        s1.servo_Angle(s1Pos)
        print(s1Pos)
    elif keyword == 'd':
        print("Command: RIGHT")
        s1Pos = s1Pos - 5
        if s1Pos < s1Pos_min:
            s1Pos = s1Pos_min
        s1.servo_Angle(s1Pos)
        print(s1Pos)
        
    #Deinitialize servo motors for free control
    if keyword == 'e':
        s1.deinit()
        s2.deinit()
        break
    
    else:
        print("Incorrect key")


        

