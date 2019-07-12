
from gpiozero import LED, Button
from signal import pause

led = LED(18)
button = Button(2)

#led.on()

button.when_pressed = led.on
button.when_released = led.off

pause()
