#Definition
##from: used for defining package to be imported from
##import: importing package or function(s)

#tcs34725 is a package for interfacing with the TCS34725 colour sensing module
import tcs34725
#I2C is a communication protocol
from machine import I2C, Pin
import time

#Object of class I2C is declared
##SCL: Serial Clock
##SDA: Serial Data
i2c = I2C(0,scl=Pin(5), sda=Pin(4))

#Declaring object sensor 
sensor = tcs34725.TCS34725(i2c)

#Infinite loop
while True:
    ##Uncomment bottom two lines for 1) Get RGB values 2) Get hex value
    
    #print(tcs34725.html_rgb(sensor.read(raw=True)))
    #print(tcs34725.html_hex(sensor.read(raw=True)))
    
    ##Receive raw RGB values
    red,green,blue = tcs34725.html_rgb(sensor.read(raw=True))
    ##Display R G and B values
    #print(f"Red = {red}, Green = {green}, Blue = {blue}")

    ##Compare and check which colour has highest presence in sensed object
    #red
    if red > green and red > blue:
        print("Detected: Red")
    elif red > 200 and green > 200 and blue > 200:
        print("Detected: White")
    elif green > red and green > blue:
        print("Detected: Green")
    #blue
    elif blue > green and blue > red:
        print("Detected: Blue")
    #white
    elif red > 200 and green > 200 and blue > 200:
        print("Detected: White")
    #black
    elif red < 10 and green < 10 and blue < 10:
        print("Detected: Black")
    
    
    time.sleep_ms(20)
    