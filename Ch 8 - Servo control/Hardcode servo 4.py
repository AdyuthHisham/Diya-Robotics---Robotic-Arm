#Imported packages
##From servo, the class Servo is imported that helps make controlling servos easier
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

#SET POSITION FOR SERVOS
s1.servo_Angle(s1Pos)
s2.servo_Angle(s2Pos)
s3.servo_Angle(s3Pos)
s4.servo_Angle(s4Pos)

        
