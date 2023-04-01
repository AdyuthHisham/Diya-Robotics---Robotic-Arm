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

##Initial position when no object
s1_inPos = 90
s2_inPos = 110
s3_inPos = 40

##Final poisiton for placement of object
s1_finPos = 90
s2_finPos = 110
s3_finPos = 140

#Initialize pins
##Front and Back
s1Servo = Servo(18)
##Left and Right
s2Servo = Servo(19)
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
    s2Servo.servo_Angle(s2_inPos)
    sleep(2)
    s3Servo.servo_Angle(s3_inPos)
    sleep(2)
    print("Arm at home position")

inPos()

#Pick object and place it
def finPos():
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
    sleep(4)
    inPos()
    
while True:

    if ir.value() == False:
        print("Object detected")
        ##Activate magnetic EE
        relay.value(1)
        ##Delay for picking up objects
        sleep(5)
        finPos()
        
        




