from machine import Pin
import utime
from time import sleep
from servo import Servo
from machine import PWM

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

pwm = PWM(Pin(0))
pwm.freq(50)
def setServoCycle (position):
    pwm.duty_u16(position)
    sleep(0.01)

def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print("The distance from object is ",distance,"cm")
   if distance < 15:
       print("Door open")
       setServoCycle(7000)
   else :
       print("Door closed")
       setServoCycle(1000)
        
while True:
   ultra()
   utime.sleep(1)
