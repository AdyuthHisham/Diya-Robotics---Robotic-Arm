from machine import Pin,ADC
from time import sleep
from servo import Servo
import servo

#INITIALIZING PINS
#Front and Back
s1 = Servo(6)
#Left and Right
s2 = Servo(7)
#Up and Down
s3 = Servo(8)
#End effector
s4 = Servo(9)

VRX1 = ADC(Pin(26))  
VRY1 = ADC(Pin(27))

SW1 = Pin(15, Pin.IN, Pin.PULL_UP)

button = Pin(10,Pin.IN)

#SERVO HOME POSITION
s1.servo_Angle(90)
sleep(1)
s2.servo_Angle(90)
sleep(1)
s3.servo_Angle(90)
sleep(1)
s4.servo_Angle(0)
sleep(1)

#GLOBAL VARIABLES
switch = 0
minMapValue = 0
maxMapValue = 255
maxCriteria = 253
minCriteria = 10

s1Pos = 0
s2Pos = 90
s3Pos = 90
s4Pos = 0


#Switch and Mapping Func
def joyData():
    global switch
    print("Flag = ",switch)
    if SW1.value() == 0:
        switch = not switch
    adc_X1=round(servo.Map(VRX1.read_u16(),0,65535,minMapValue,maxMapValue))
    adc_Y1=round(servo.Map(VRY1.read_u16(),0,65535,minMapValue,maxMapValue))
    return(adc_X1,adc_Y1)

#SERVO Func
def servoMove():
    global s1Pos,s2Pos,s3Pos,s4Pos
    joyX,joyY = joyData()
    if switch == 0:
        if joyY > maxCriteria:
            print("Command: FRONT")
            s1Pos = s1Pos + 10
            if(s1Pos > 180):
                s1Pos = 180
            s1.servo_Angle(s1Pos)
            print("s1Pos = ",s1Pos)
        elif joyX > maxCriteria:
            print("Command: LEFT")
            s2Pos = s2Pos + 10
            if(s2Pos > 180):
                s2Pos = 180
            s2.servo_Angle(s2Pos)
            print("s2Pos = ",s2Pos)
        elif joyY < minCriteria:
            print("Command: BACK")
            s1Pos = s1Pos - 10
            if(s1Pos < 0):
                s1Pos = 0
            s1.servo_Angle(s1Pos)
            print("s1Pos = ",s1Pos)
        elif joyX < minCriteria:
            print("Command: RIGHT")
            s2Pos = s2Pos - 10
            if(s2Pos < 0):
                s2Pos = 0
            s2.servo_Angle(s2Pos)
            print("s2Pos = ",s2Pos)
        while button.value():
            print("Button")
            s4Pos = s4Pos + 5
            if s4Pos > 180:
                s4Pos = 180
            s4.servo_Angle(s4Pos)
            sleep(0.3)
            
            
    elif switch == 1:
        if joyY > maxCriteria:
            print("Command: UP")
            s3Pos = s3Pos + 10
            if(s3Pos > 180):
                s3Pos = 180
            s3.servo_Angle(s3Pos)
            print("s3Pos = ",s3Pos)
        elif joyX > maxCriteria:
            print("Command: EE OPEN")
            s4Pos = s4Pos + 10
            if(s4Pos > 180):
                s4Pos = 180
            s4.servo_Angle(s4Pos)
            print("s4Pos = ",s4Pos)
        elif joyY < minCriteria:
            print("Command: DOWN")
            s3Pos = s3Pos - 10
            if(s3Pos < 0):
                s3Pos = 0
            s3.servo_Angle(s3Pos)
            print("s3Pos = ",s3Pos)
        elif joyX < minCriteria:
            print("Command: EE CLOSE")
            s4Pos = s4Pos - 10
            if(s4Pos < 0):
                s4Pos = 0
            s4.servo_Angle(s4Pos)
            print("s4Pos = ",s4Pos)
        while button.value():
            print("Button")
            s4Pos = s4Pos - 5
            if s4Pos < 0:
                s4Pos = 0
            s4.servo_Angle(s4Pos)
            sleep(0.3)



while True:
    print("----------------------")
    servoMove()
    sleep(0.6)