from machine import Pin
import time

def edge_pulse_width(pin):
    start_time = 0

    def callback(p):
        nonlocal start_time
        if p.value():
            start_time = time.ticks_us()
        else:
            pulse_width = time.ticks_diff(time.ticks_us(), start_time)
            print("Pulse width:", pulse_width, "us")

    pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)
