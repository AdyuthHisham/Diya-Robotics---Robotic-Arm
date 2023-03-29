import tcs34725
from machine import I2C, Pin
import time



i2c = I2C(0,scl = Pin(5), sda = Pin(4))
sensor = tcs34725.TCS34725(i2c)
#print(sensor.read())
sensor.active(True)
time.sleep_ms(500)
while True:
    print(sensor.read(True))
    time.sleep_ms(20)