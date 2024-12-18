# Control the position of a servo using PWM
from machine import Pin, PWM
from time import sleep
servo = PWM(Pin(11), freq=50)
sensor = Pin(38, Pin.IN, Pin.PULL_DOWN)
# For a little SG90 micro-servos,
# 20 is full left, 130 is full right, 90 is about the middle
# you may need to troubleshoot and do you own calculations for your motor
while True: 
    while sensor.value() == 0:
        servo.duty(90)
        print (sensor.value())
    while sensor.value() == 1:
        servo.duty (60)
