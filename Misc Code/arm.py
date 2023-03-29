from machine import Pin,ADC
from time import sleep
from servo import Servo
 
s1 = Servo(6)
s2 = Servo(7)
s3 = Servo(8)
s4 = Servo(9)

button1=(Pin(18,Pin.IN))
button2=(Pin(19,Pin.IN))

VRX1 = ADC(Pin(26))  
VRY1 = ADC(Pin(27))  
SW1 = Pin(15, Pin.IN, Pin.PULL_UP)

def Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + (out_min)
  
def servo_Angle(angle,servo_num):
    servo_num.goto(round(Map(angle,0,180,0,1024)))
 
def direction():
    global i
    i = 0
    adc_X1=round(Map(VRX1.read_u16(),0,65535,0,255))
    adc_Y1=round(Map(VRY1.read_u16(),0,65535,0,255))
    Switch1 = SW1.value()
    b1 = button1.value()
    b2 = button2.value()
    
    print("X value: ",adc_X1)
    print("Y value: ",adc_Y1)
    print("switch value: ",Switch1) 
    print("B1:",b1)
    print("b2: ",b2)
    
    if b1 == 1:
         i = 7 
    elif b2 == 1:
        i = 8
    else:
        if  adc_X1 <= 30:
            i = 1        # Define down direction
        elif adc_X1 >= 255:
            i = 2        # Define up direction
        elif adc_Y1 >= 255:
            i = 3        # Define left direction
        elif adc_Y1 <= 30:
            i = 4        # Define right direction
        elif  Switch1 == 0:#and adc_Y ==128:
            i = 5        # Define Button pressed
        elif  Switch1 == 1:#and adc_Y ==128:
            i = 6

def loop():
    num = 90        
    while True:
        direction()   
        sleep(0.01)
        print(num)
        if i == 1:
            num = num - 1
            if num < 0:
                num = 0
            servo_Angle(num,s1)
        if i == 2:
            num = num + 1
            if num > 180:
                num = 180
            servo_Angle(num,s1)
        if i == 3:
            num = num + 1
            if num > 180:
                num = 180
            servo_Angle(num,s2)
        if i == 4:
            num = num - 1
            if num < 0:
                num = 0
            servo_Angle(num,s2)
        if i == 5:
            servo_Angle(180,s3)
        if i == 6:
            servo_Angle(0,s3)
        if i == 7:
            print("button 1")
            num = num - 1
            sleep(0.1)
            if num < 0:
                num = 0
            servo_Angle(0,s4)
        if i == 8:
            print("button 2")
            num = num + 1
            sleep(0.1)
            if num > 180:
                num = 180
            servo_Angle(180,s4)
        if i == 9:
            servo_Angle(num,s4)

if __name__ == '__main__':
    loop()   
    
