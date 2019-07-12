from gpiozero import LED
from time import sleep

led = LED(18)
led1 = LED(17)
led2 = LED(22)


while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    

    led1.on()
    sleep(1)
    led.off()
    sleep(1)
    

    led2.on()
    sleep(1)
    led.off()
    sleep(2)

