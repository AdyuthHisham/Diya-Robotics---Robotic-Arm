#Imported packages
##Machine package imports functions required for communicating with the microcontroller
from machine import Pin
##sleep function is used to put the board to sleep. This is done to give a buffer preventing overloading of data
from time import sleep
##From servo, the class Servo is imported that helps make controlling servos easier
from servo import Servo

#Config variables
ir_pin = 16
relay_pin = 15

s1_bufferPos = 65 

##Initial position when no object
s1_inPos = 125
s2_inPos = 65
s3_inPos = 120

##Middle poisiton for picking of object
s1_midPos = 45
s2_midPos = 0
s3_midPos = 100

##Final poisiton for placement of object
s1_finPos = 55
s2_finPos = 120
s3_finPos = 100

#Initialize pins
##Front and Back
s1Servo = Servo(19)
##Left and Right
s2Servo = Servo(18)
##Up and Down
s3Servo = Servo(20)
##Object detection sensor
ir = Pin(ir_pin,Pin.IN)
##Relay activation 
relay = Pin(relay_pin,Pin.OUT)

#Setup

##Set arm to home position
def inPos():
    print("Going to home position")
    s1Servo.servo_Angle(s1_inPos)
    sleep(2)
    s3Servo.servo_Angle(s3_inPos)
    sleep(2)
    s2Servo.servo_Angle(s2_inPos)
    sleep(2)    
    print("Arm at home position")

inPos()

##Set arm to picking up position
def pickPos():
    print("Going to pick object")
    s2Servo.servo_Angle(s2_midPos)
    sleep(2)
    s3Servo.servo_Angle(s3_midPos)
    sleep(2)
    s1Servo.servo_Angle(s1_bufferPos)
    sleep(2)
    s1Servo.servo_Angle(s1_midPos)
    sleep(2)
    print("Pciked object")
    #sleep(100000)

#Pick object and place it
def finPos():
    for i in range(s1_midPos,s1_inPos):
        s1Servo.servo_Angle(i)
        sleep(0.15)
    sleep(2)
    inPos()
    sleep(2)
    print("Picking up object")
    s2Servo.servo_Angle(s2_finPos)
    sleep(2)
    s1Servo.servo_Angle(s1_finPos)
    sleep(2)
    s3Servo.servo_Angle(s3_finPos)
    sleep(2)
    print("Object droppped in designated area")
    #Turn off magnetic EE
    relay.value(0)
    sleep(5)
    inPos()
  
while True:

    if ir.value() == True:
        print("Object detected")
        ##Activate magnetic EE
        relay.value(0)
        ##Delay for picking up objects
        sleep(3)
        finPos()
        
        




