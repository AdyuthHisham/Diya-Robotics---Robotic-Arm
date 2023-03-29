from machine import Pin,PWM
import utime

smoke = Pin(28,Pin.IN)
buzzer = PWM(Pin(7))
buzzer.freq(500)

while True:     
    print("Smoke: ",smoke.value())
    ##If smoke sensor detects smoke
    ##Activate sprinkler system
    if(smoke.value() == 0):
        print("Activating sprinkler system")
        buzzer.duty_u16(1000)
        utime.sleep(1)
        buzzer.duty_u16(0)
        
    utime.sleep(0.2)