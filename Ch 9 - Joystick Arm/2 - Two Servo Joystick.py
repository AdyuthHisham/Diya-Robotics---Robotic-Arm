from machine import Pin,ADC
from time import sleep
from servo import Servo
import servo

#INITIALIZING PINS
#Front and Back
s1Servo = Servo(11)
#Left and Right
s2Servo = Servo(13)

VRX1 = ADC(Pin(26))  
VRY1 = ADC(Pin(27))

SW1 = Pin(16, Pin.IN, Pin.PULL_UP)

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

#Receive joystick data and map it
def joyData():
    adc_X1=round(servo.Map(VRX1.read_u16(),0,65535,minMapValue,maxMapValue))
    adc_Y1=round(servo.Map(VRY1.read_u16(),0,65535,minMapValue,maxMapValue))
    return(adc_X1,adc_Y1)

#Move servo to required position
def servoMove(servoVars,flag):
    ##Update new value of servo Position
    ##If flag = 1; increase position value
    ##If flag = -1; decrease position value
    servoVars[1] = servoVars[1] + (flag * changeVar)
    ##Keep servo position between 0 and 180
    if(servoVars[1] + changeVar >= 180):
        servoVars[1] = servoVars[1] - changeVar
    elif(servoVars[1] + changeVar <= 0):
        servoVars[1] = servoVars[1] + changeVar
    ##Move servo
    servoVars[0].servo_Angle(servoVars[1])
    
#SERVO Func
def joyMove():

    global s1,s2,SW1
    print(f"{SW1.value()}")
    
    ##Get joystick data
    joyX,joyY = joyData()
    print(f"joyX = {joyX} : joyY = {joyY}")
    ##Servo 1 and Servo 2
    if SW1.value() == 0:
        print("Going to home position")
        s1[1] = 90
        s2[1] = 90
        s1[0].servo_Angle(90)
        s2[0].servo_Angle(90)
    elif joyY > maxCriteria:
        print("Command: RIGHT")
        servoMove(s1,-1)
        print("s1[1] = ",s1[1])
    elif joyY < minCriteria:
        print("Command: LEFT")
        servoMove(s1,1)
        print("s1[1] = ",s1[1])
    elif joyX > maxCriteria:
        print("Command: FRONT")
        servoMove(s2,1)
        print("s2[1] = ",s2[1])
    elif joyX < minCriteria:
        print("Command: BACK")
        servoMove(s2,-1)
        print("s2[1] = ",s2[1])

while True:
    print("----------------------")
    joyMove()
    sleep(0.3)