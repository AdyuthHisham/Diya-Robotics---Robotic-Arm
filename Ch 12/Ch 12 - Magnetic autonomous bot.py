#Imported packages
##Machine package imports functions required for communicating with the microcontroller
from machine import Pin
##sleep function is used to put the board to sleep. This is done to give a buffer preventing overloading of data
from time import sleep
##From servo, the class Servo is imported that helps make controlling servos easier
from servo import Servo

#Config variables
ir_pin = 16
relay_pin = 19

##Initial position when no object
s1_inPos = 145
s2_inPos = 10
s3_inPos = 60

##Final poisiton for placement of object
s1_finPos = 30
s2_finPos_1 = 70
s2_finPos_2 = 20
s3_finPos = 50

#Initialize pins
##Front and Back
s1Servo = Servo(7)
##Left and Right
s2Servo = Servo(8)
##Up and Down
s3Servo = Servo(9)
##Object detection sensor
ir = Pin(ir_pin,Pin.IN)
##Relay activation 
relay = Pin(relay_pin,Pin.OUT)

#Setup

##Position for going to home position
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

#Function for placing object
def finPos():
    print("Picking up object")
    s2Servo.servo_Angle(s2_finPos_1)
    sleep(2)
    s1Servo.servo_Angle(s1_finPos)
    sleep(2)
    s3Servo.servo_Angle(s3_finPos)
    sleep(2)
    s2Servo.servo_Angle(s2_finPos_2)
    sleep(2)
    print("Object droppped in designated area")
    relay.value(0)
    sleep(4)
    inPos()
    
#Infinite loop
while True:
    #If object is detected..
    if ir.value() == False:
        print("Object detected")
        #Activate EE
        relay.value(1)
        ##Delay for picking up objects
        sleep(5)
        #Run function
        finPos()
        #Move to allocated area
        




