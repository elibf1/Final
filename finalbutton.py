from machine import I2C, Pin, PWM, I2S
from time import sleep
import math
import struct
import time

from machine import Pin, I2S
import math
import struct
from time import sleep



sck_pin = Pin(2) # Serial clock (BCLK on breakout)
ws_pin = Pin(3) # Word select (LRCLK on breakout)
sd_pin = Pin(1) # Serial data (DIN on breakout)

# Open the audio channel using I2S (Inter-IC-Sound)
audio = I2S(0, # This must be either 0 or 1 for ESP32
            sck=sck_pin, ws=ws_pin, sd=sd_pin,
            mode=I2S.TX,
            bits=16,
            format=I2S.MONO,
            rate= 88200, # This must match the sample rate of your file!
            ibuf=10000)
WAVFILE = "ding.wav"
BUFFER_SIZE = 100000

wav = open(WAVFILE, "rb") # Open the file to read its bytes
pos = wav.seek(44) # Skip over the WAV header information and get to the data

buf = bytearray(BUFFER_SIZE)
wav_samples_mv = memoryview(buf)

servo = PWM(Pin(36), freq=50)
led = Pin(1, Pin.OUT)
Switch1 = Pin(21, Pin.IN, Pin.PULL_DOWN)
Switch2 = Pin(15, Pin.IN, Pin.PULL_DOWN)
Switch3 = Pin(37, Pin.IN, Pin.PULL_DOWN)
Switch4 = Pin(38, Pin.IN, Pin.PULL_DOWN)
correct = [0, 1, 2, 3]
user_input = []

while True:
    
    
    if Switch1.value() == 1 and len(user_input)<4:
        user_input.append(0)
        sleep(0.5)
        print (user_input)
    if Switch2.value() == 1 and len(user_input)<4:
        user_input.append(1)
        sleep(0.5)
        print (user_input)
    if Switch3.value() == 1 and len(user_input)<4:
        user_input.append(2)
        sleep(0.5)
        print (user_input)
    if Switch4.value() == 1 and len(user_input)<4:
        user_input.append(3)
        sleep(0.5)
        print (user_input)
    if user_input == correct:
        servo.duty(50)
        sleep(5)
    
        user_input = []
        led.off()
        servo.duty(80)
        audio.deinit()
        print("done")
        wav = open(WAVFILE, "rb")
        pos = wav.seek(44)
    if len(user_input) >= 4 and user_input != correct:
        user_input = []
        print (user_input)
        
    else:
        led.off()
        servo.duty(80)
    
    