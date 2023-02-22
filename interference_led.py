from machine import Pin
from machine import Timer

pin1 = Pin(5, Pin.OUT)
pin2 = Pin(4, Pin.OUT)

pin1.on()
pin2.on()

led1tim1 = Timer(-1)
led1tim2 = Timer(-1)
led1tim1.init(period=5000, mode=Timer.PERIODIC, callback=lambda p: pin1.off())
led1tim2.init(period=2000, mode=Timer.PERIODIC, callback=lambda p: pin1.on())

led2tim1 = Timer(-1)
led2tim2 = Timer(-1)
led2tim1.init(period=450, mode=Timer.PERIODIC, callback=lambda p: pin2.off())
led2tim2.init(period=187, mode=Timer.PERIODIC, callback=lambda p: pin2.on())
