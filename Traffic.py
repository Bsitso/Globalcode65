from gpiozero import LED
from time import sleep

led = LED(18)
led1 = LED(17)
led2 = LED(27)
buzz = LED(22)

while True:
    led.on()
    sleep(0.03)
    led.off()
    sleep(0.03)
    

    led1.on()
    sleep(0.03)
    led1.off()
    sleep(0.03)
    

    led2.on()
    sleep(0.03)
    led2.off()
    sleep(0.1)

