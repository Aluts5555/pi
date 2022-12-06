# Write your code here :-)
from gpiozero import Button, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

def jog_left():
    angl=servo.angle
    angl -= 1
    if angl <= -58:
        angl = -58
    servo.angle=angl
    print("servo angle= ", servo.angle)
    sleep(.02)

def jog_right():
    angl=servo.angle
    angl += 1
    if angl >= 58:
        angl = 58
    servo.angle=angl
    print("servo angle= ", servo.angle)
    sleep(.02)

def center_rudder():
    servo.angle=0.
    print("servo angle= ", servo.angle)

factory = PiGPIOFactory()
#angl=0
button_L = Button(24)
button_R = Button(25)
button_C = Button(27)

servo = AngularServo(18, min_angle=-60, max_angle=60,
                     min_pulse_width=800/1000000,
                     max_pulse_width=1900/1000000,
                     frame_width=20/1000,
                     pin_factory=factory)

try:
    while True:
        if button_L.is_pressed:
            jog_left()
        elif button_R.is_pressed:
            jog_right()
        elif button_C.is_pressed:
            center_rudder()
except KeyboardInterrupt:
    exit
        
