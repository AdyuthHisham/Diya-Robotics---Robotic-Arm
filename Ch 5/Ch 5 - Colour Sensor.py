import tcs34725
from machine import I2C, Pin
import time
i2c = I2C(0,scl=Pin(5), sda=Pin(4))
sensor = tcs34725.TCS34725(i2c)
while True:
    #print(tcs34725.html_rgb(sensor.read(raw=True)))
    #print(tcs34725.html_hex(sensor.read(raw=True)))
    red,green,blue = tcs34725.html_rgb(sensor.read(raw=True))
    #print(f"Red = {red}, Green = {green}, Blue = {blue}")

    #red
    if red > green and red > blue:
        print("Detected: Red")
    elif green > red and green > blue:
        print("Detected: Green")
    #blue
    elif blue > green and blue > red:
        print("Detected: Blue")
    #white
    elif red > 200 and green > 200 and blue > 200:
        print("Detected: Black")
    #black
    elif red < 10 and green < 10 and blue < 10:
        print("Detected: White")
    
    time.sleep_ms(20)
    