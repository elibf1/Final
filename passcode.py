#TEST CODE FOR PASSCODE WITH LED
from machine import I2C, Pin
from time import sleep

led = Pin(38, Pin.OUT)
Switch1 = Pin(7, Pin.IN, Pin.PULL_DOWN)
Switch2 = Pin(6, Pin.IN, Pin.PULL_DOWN)
Switch3 = Pin(5, Pin.IN, Pin.PULL_DOWN)
Switch4 = Pin(4, Pin.IN, Pin.PULL_DOWN)

correct = [0, 1, 2, 3]
user_input = []

while True:
    print(user_input)
    if Switch1.value() == 1:
        user_input.append(0)
        sleep(0.5)
    if Switch2.value() == 1:
        user_input.append(1)
        sleep(0.5)
    if Switch3.value() == 1:
        user_input.append(2)
        sleep(0.5)
    if Switch4.value() == 1:
        user_input.append(3)
        sleep(0.5)
    if user_input == correct:
        led.on()
        sleep(5)
        user_input = []
        led.off()
    if len(user_input) > 4:
        user_input = []
    else:
        led.off()
    
    
