# Write your code here :-)
import RPi.GPIO as GPIO
from gpiozero import Button, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

def jog_left():
    angl=servo.angle
    angl -= 1
    if angl <= -58:
        angl = -58
    servo.angle=angl
    print("servo angle= ", servo.angle)
    sleep(.1)

def jog_right():
    angl=servo.angle
    angl += 1
    if angl >= 58:
        angl = 58
    servo.angle=angl
    print("servo angle= ", servo.angle)
    sleep(.1)

def center_rudder():
    servo.angle=0.
    print("servo angle= ", servo.angle)
    sleep(.1)

Factory = PiGPIOFactory()
button_L = Button(24)
button_R = Button(25)
button_C = Button(27)

servo = AngularServo(18, min_angle=60, max_angle=-60,
                     min_pulse_width=800/1000000,
                     max_pulse_width=1900
                     
                     /1000000,
                     frame_width=20/1000,
                     pin_factory=Factory)

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
        
