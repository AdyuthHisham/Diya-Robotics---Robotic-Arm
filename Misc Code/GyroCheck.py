from machine import Pin,ADC
from time import sleep
from servo import Map

#Initialize pins

##Gyro values
gyro_x = ADC(Pin(26,Pin.IN))
gyro_y = ADC(Pin(27,Pin.IN))
gyro_z = ADC(Pin(28,Pin.IN))

XLim_min = 459
YLim_min = 450
ZLim_min = 415
    
XLim_max = 620 
YLim_max = 620
ZLim_max = 510

while True:
    XPos = Map(gyro_x.read_u16(),0,65535,0,1024)
    YPos = Map(gyro_y.read_u16(),0,65535,0,1024)
    ZPos = Map(gyro_z.read_u16(),0,65535,0,1024)
    print(f"{XPos} : {YPos} : {ZPos} ")
    
    if XPos < XLim_min:
        print("MOVE: BACK")
    elif XPos > XLim_max:
        print("MOVE: FRONT")
    if YPos < YLim_min:
        print("MOVE: RIGHT")
    elif YPos > YLim_max:
        print("MOVE: LEFT")
    '''
    if ZPos < ZLim_min:
        print("MOVE: UP")
    elif ZPos > ZLim_max:
        print("MOVE: DOWN")
    '''
        ##else:
        ##print("MOVE: STANDBY")

    sleep(0.9)
    
    #500:490:615