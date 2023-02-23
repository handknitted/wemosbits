from machine import Pin
from libs.leds import green_light, yellow_light

pin8 = Pin(15, Pin.IN)
while True:
    if pin8.value():
        green_light()
    else:
        yellow_light()