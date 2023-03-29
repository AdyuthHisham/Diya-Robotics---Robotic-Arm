from machine import Pin
from time import sleep

# ESP32 GPIO 26
relay = Pin(19, Pin.OUT)
button = Pin(10,Pin.IN)

while True:
  if button.value() == 1:    
      relay.value(1)
  else:
      relay.value(0)
