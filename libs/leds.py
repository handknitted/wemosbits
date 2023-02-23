from machine import Pin

pin2 = Pin(4, Pin.OUT)
pin1 = Pin(5, Pin.OUT)


def green_light():
    pin1.on()
    pin2.off()


def yellow_light():
    pin1.off()
    pin2.on()