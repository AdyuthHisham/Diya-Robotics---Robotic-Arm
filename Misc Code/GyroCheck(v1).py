from machine import Pin,ADC
from time import sleep
from servo import Map

#Initialize pins

##Gyro values
gyro_x = ADC(Pin(26,Pin.IN))
gyro_y = ADC(Pin(27,Pin.IN))
gyro_z = ADC(Pin(28,Pin.IN))

#Dumb shit but might work
gyro_x.read_u16()
gyro_y.read_u16()
gyro_z.read_u16()

sleep(1.0)

XLim = Map(gyro_x.read_u16(),0,65535,0,1024)
YLim = Map(gyro_y.read_u16(),0,65535,0,1024)
ZLim = Map(gyro_z.read_u16(),0,65535,0,1024)
    
while True:
    XPos = Map(gyro_x.read_u16(),0,65535,0,1024)
    YPos = Map(gyro_y.read_u16(),0,65535,0,1024)
    ZPos = Map(gyro_z.read_u16(),0,65535,0,1024)
    #print(f"{XPos} : {YPos} : {ZPos} ")
    if XPos < XLim - 50:
        if YPos < YLim - 50:
            if ZPos < ZLim - 50:
                print("0:0:0")
            else:
                print("0:0:1")
        elif ZPos < ZLim - 50:
            print("0:1:0")
        else:
            print("0:1:1")
    elif YPos < YLim - 50:
        if ZPos < ZLim - 50:
            print("1:0:0")
        else:
            print("1:0:1")
    elif ZPos < ZLim - 50:
        print("1:1:0")
    else:
        print("1:1:1")
        
    sleep(0.9)
    
    #500:490:615