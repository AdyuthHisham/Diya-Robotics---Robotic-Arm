from machine import Pin,ADC
from time import sleep
from servo import Servo
import servo

#INITIALIZING PINS
#Front and Back
s1Servo = Servo(6)
#Left and Right
s2Servo = Servo(7)

VRX1 = ADC(Pin(26))  
VRY1 = ADC(Pin(27))

SW1 = Pin(15, Pin.IN, Pin.PULL_UP)

#SERVO HOME POSITION
s1Servo.middle()
sleep(1)
s2Servo.middle()
sleep(1)

#GLOBAL VARIABLES
minMapValue = 0
maxMapValue = 255
maxCriteria = 253
minCriteria = 10
changeVar = 5

s1Pos = 90
s2Pos = 90

#Dictionary
s1 = [s1Servo,s1Pos]
s2 = [s2Servo,s2Pos]

def joyData():
    
    adc_X1=round(servo.Map(VRX1.read_u16(),0,65535,minMapValue,maxMapValue))
    adc_Y1=round(servo.Map(VRY1.read_u16(),0,65535,minMapValue,maxMapValue))
    return(adc_X1,adc_Y1)

def servoMove(servoVars,flag):
    servoVars[1] = servoVars[1] + (flag * changeVar)
    if(servoVars[1] + changeVar >= 180):
        servoVars[1] = servoVars[1] - changeVar
    elif(servoVars[1] + changeVar <= 0):
        servoVars[1] = servoVars[1] + changeVar
    servoVars[0].servo_Angle(servoVars[1])

def joyMove():

    global s1,s2,s3,s4

    joyX,joyY = joyData()

    if joyY > maxCriteria:
        print("Command: FRONT")
        servoMove(s1,1)
        print("s1[1] = ",s1[1])
    elif joyY < minCriteria:
        print("Command: BACK")
        servoMove(s1,-1)
        print("s1[1] = ",s1[1])
    elif joyX > maxCriteria:
        print("Command: LEFT")
        servoMove(s2,1)
        print("s2[1] = ",s2[1])
    elif joyX < minCriteria:
        print("Command: RIGHT")
        servoMove(s2,-1)
        print("s2[1] = ",s2[1])


while True:
    print("----------------------")
    joyMove()
    sleep(0.3)