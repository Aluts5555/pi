# Write your code here :-)
from gpiozero import Button, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

#angl = 0

def jog_left():
    angl -= 1
    servo.angle = angl
    sleep(.02)

def jog_right():
    angl += 1
    servo.angle = angl
    sleep(.02)

def center_rudder():
    servo.angle = 0.

factory = PiGPIOFactory()
servo = AngularServo(18, min_angle=-60, max_angle=60,
                     min_pulse_width=800/1000000,
                     max_pulse_width=1900/1000000,
                     frame_width=20/1000,
                     pin_factory=factory)

button_L = Button(24)
button_R = Button(25)
button_C = Button(27)

while True:
    if button_L.is_pressed:
        angl = servo.angle
        jog_left
    elif button_R.is_pressed:
        angl = servo.angle
        jog_right
    elif button_C.is_pressed:
        center_rudder