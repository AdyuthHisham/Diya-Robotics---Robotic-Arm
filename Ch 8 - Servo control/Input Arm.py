#Imported packages
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

#POSITION TO BE SET
s1Pos = 90
s2Pos = 90
s3Pos = 90
s4Pos = 90

#Infinite loop
while True:
    #Reading values for setting position of servos
    s1Pos = int(input("Enter angle for base servo: "))
    s2Pos = int(input("Enter angle for left link servo: "))
    s3Pos = int(input("Enter angle for right link servo: "))
    s4Pos = int(input("Enter angle for gripper servo: "))
    sleep(1)
    #Setting position of servos
    s1.servo_Angle(s1Pos)
    sleep(0.5)
    s2.servo_Angle(s2Pos)
    sleep(0.5)
    s3.servo_Angle(s3Pos)
    sleep(0.5)
    s4.servo_Angle(s4Pos)

        
