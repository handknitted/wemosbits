from machine import Pin
from machine import Timer

pin1 = Pin(5, Pin.OUT)

pin1.on()

tim1 = Timer(-1)
tim2 = Timer(-1)
tim1.init(period=5000, mode=Timer.PERIODIC, callback=lambda p: pin1.off())
tim2.init(period=2000, mode=Timer.PERIODIC, callback=lambda p: pin1.on())
