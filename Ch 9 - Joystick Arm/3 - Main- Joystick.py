#Imported packages
##Machine package imports functions required for communicating with the microcontroller
from machine import Pin,ADC
##sleep function is used to put the board to sleep. This is done to give a buffer preventing overloading of data
from time import sleep
##From servo, the class Servo is imported that helps make controlling servos easier
from servo import Servo
##Servo has a function called mapping for mapping values
import servo

#INITIALIZING PINS

##Front and Back
s1Servo = Servo(19)
##Left and Right
s2Servo = Servo(18)
##Up and Down
s3Servo = Servo(20)
##End effector
s4Servo = Servo(21)

##Pins for joystick
VRX1 = ADC(Pin(26))  
VRY1 = ADC(Pin(27))
SW1 = Pin(15, Pin.IN, Pin.PULL_UP)

##SERVO HOME POSITION
s1Servo.middle()
sleep(1)
s2Servo.middle()
sleep(1)
s3Servo.middle()
sleep(1)
s4Servo.middle()
sleep(1)

#GLOBAL VARIABLES
##To monitor which set of servos to be controlled
switch = 0
##Variables for mapping
minMapValue = 0
maxMapValue = 255
##Max/Min value of joystick for activating functions
maxCriteria = 253
minCriteria = 10
##Degree of change
changeVar = 5

##Servo position
##Used for monitoring the current position of servo
s1Pos = 90
s2Pos = 90
s3Pos = 90
s4Pos = 90

##Dictionary for storing servo data
s1 = [s1Servo,s1Pos]
s2 = [s2Servo,s2Pos]
s3 = [s3Servo,s3Pos]
s4 = [s4Servo,s4Pos]


#Switch and Mapping Function
def joyData():
    global switch
    print("Flag = ",switch)
    #print("Change value for Switch when joystick button is pressed")
    ##Change value of 'switch' when joystick button is clicked
    if SW1.value() == 0:
        switch = not switch
    ##Map raw joystick values to required range
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

    global s1,s2,s3,s4
    ##Get joystick data
    joyX,joyY = joyData()
    ##Servo 1 and Servo 2
    if switch == 0:
        if joyY > maxCriteria:
            print("Command: LEFT")
            servoMove(s1,1)
            print("s1[1] = ",s1[1])
        elif joyY < minCriteria:
            print("Command: RIGHT")
            servoMove(s1,-1)
            print("s1[1] = ",s1[1])
        elif joyX > maxCriteria:
            print("Command: BACK")
            servoMove(s2,-1)
            print("s2[1] = ",s2[1])
        elif joyX < minCriteria:
            print("Command: FRONT")
            servoMove(s2,1)
            print("s2[1] = ",s2[1])
    #Servo 3 and Servo 4
    elif switch == 1:
        if joyY > maxCriteria:
            print("Command: UP")
            servoMove(s3,1)
            print("s3[1] = ",s3[1])
        elif joyY < minCriteria:
            print("Command: DOWN")
            servoMove(s3,-1)
            print("s3[1] = ",s3[1])
        elif joyX > maxCriteria:
            print("Command: EE OPEN")
            servoMove(s4,1)
            print("s4[1] = ",s4[1])
        elif joyX < minCriteria:
            print("Command: EE CLOSE")
            servoMove(s4,-1)
            print("s4[1] = ",s4[1])



while True:
    #Main command
    print("----------------------")
    joyMove()
    sleep(0.3)`