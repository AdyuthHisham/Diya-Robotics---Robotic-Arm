from machine import Pin,ADC
from time import sleep
from servo import Servo,Map

#Initialize pins
relay = Pin(19,Pin.OUT)
gyro_x = ADC(Pin(26,Pin.IN))
gyro_y = ADC(Pin(27,Pin.IN))
gyro_z = ADC(Pin(28,Pin.IN))

XLim_min = 459
YLim_min = 450
ZLim_min = 415
    
XLim_max = 600 
YLim_max = 600
ZLim_max = 510

##Front and Back
s1 = Servo(7)
##Left and Right
s2 = Servo(8)
##Up and Down
s3 = Servo(9)

#Global variables
s1Pos = 90
s2Pos = 90
s3Pos = 90

while True:
    XPos = Map(gyro_x.read_u16(),0,65535,0,1024)
    YPos = Map(gyro_y.read_u16(),0,65535,0,1024)
    ZPos = Map(gyro_z.read_u16(),0,65535,0,1024)
    print(f"{XPos} : {YPos} : {ZPos} ")

    if XPos < XLim_min:
        print("MOVE: DOWN")
        s2Pos = s2Pos - 15
        if s2Pos <= 0:
            s2Pos = 0
        s2.servo_Angle(s2Pos)
    if XPos > XLim_max:
        print("MOVE: UP")
        s2Pos = s2Pos + 15
        if s2Pos >= 180:
            s2Pos = 180
        s2.servo_Angle(s2Pos)
        print(s2Pos)
    if YPos < YLim_min:
        print("MOVE: LEFT")
        s1Pos = s1Pos - 15
        if s1Pos <= 0:
            s1Pos = 0
        s1.servo_Angle(s1Pos)
    if YPos > YLim_max:
        print("MOVE: RIGHT")
        s1Pos = s1Pos + 15
        if s1Pos >= 180:
            s1Pos = 180
        s1.servo_Angle(s1Pos)
        print(s1Pos)
        
    
    sleep(1.0)