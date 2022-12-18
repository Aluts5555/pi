from gpiozero import Servo
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
servo = Servo(18, min_pulse_width=800/1000000, max_pulse_width=1900/1000000, pin_factory=factory)
try:
    while 1:
        for values in range(-90, 90, 15):
            servo.value=values/90
            sleep(1)
except KeyboardInterrupt:
    exit
