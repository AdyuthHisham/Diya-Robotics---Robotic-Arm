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
s1_finPos = 170
s2_finPos = 50
s3_finPos = 10

#Initialize pins
##Front and Back
s1Servo = Servo(7)
##Left and Right
s2Servo = Servo(8)
##Up and Down
s3Servo = Servo(9)

button = Pin(10,Pin.IN)
ir = Pin(ir_pin,Pin.IN)
relay = Pin(relay_pin,Pin.OUT)

#Setup

##SERVO HOME POSITION
'''
s1Servo.middle()
sleep(1)
s2Servo.middle()
sleep(1)
s3Servo.middle()
sleep(1)
'''
##Position for picking up
def inPos():
    print("inPos")
    s1Servo.servo_Angle(s1_inPos)
    sleep(2)
    s2Servo.servo_Angle(s2_inPos)
    sleep(2)
    s3Servo.servo_Angle(s3_inPos)
    sleep(2)
    print("Done: inPos")

inPos()

def finPos():
    print("finPos")
    s2Servo.servo_Angle(70)
    sleep(2)
    s1Servo.servo_Angle(30)
    sleep(2)
    s3Servo.servo_Angle(50)
    sleep(2)
    s2Servo.servo_Angle(20)
    sleep(2)
    print("Done: finPos")
    inPos()

while True:

    if button.value():
        print("button")
        finPos()
        #Move to allocated area