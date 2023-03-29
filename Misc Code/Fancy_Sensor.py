import tcs34725
from machine import I2C, Pin
import time
i2c = I2C(0,scl=Pin(5), sda=Pin(4))
sensor = tcs34725.TCS34725(i2c)
while True:
    print(tcs34725.html_rgb(sensor.read(raw=True)))
    #print(tcs34725.html_hex(sensor.read(raw=True)))
    time.sleep_ms(20)