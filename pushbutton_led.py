from gpiozero import Button, LED
from signal import pause

# Connect LED to GPIO pin 14
led = LED(14)
# Connect button to GPIO pin 4
button = Button(4)
# Turn LED on when button is pressed
button.when_pressed = led.on
# Turn LED off when button is released
button.when_released = led.off
# Keep program running
pause()