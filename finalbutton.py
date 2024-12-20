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


servo = PWM(Pin(36), freq=50)
led = Pin(1, Pin.OUT)
Switch1 = Pin(14, Pin.IN, Pin.PULL_DOWN) #defining all of the buttons for the code
Switch2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
Switch3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
Switch4 = Pin(12, Pin.IN, Pin.PULL_DOWN)
correct = [0, 1, 2, 3] #correct sequence that the user must enter
user_input = [] #list that will correspond to the users inputs

while True:
    if Switch1.value() == 1 and len(user_input)<4: #if the first switch is pressed and the set of numbers is less than 4, add 0 to the list
        user_input.append(0)
        sleep(0.5)
        print (user_input)
    elif Switch2.value() == 1 and len(user_input)<4: #if the second switch is pressed and the set of numbers is less than 4, add 1 to the list
        user_input.append(1)
        sleep(0.5)
        print (user_input)
    elif Switch3.value() == 1 and len(user_input)<4: #if the third switch is pressed and the set of numbers is less than 4, add 2 to the list
        user_input.append(2)
        sleep(0.5)
        print (user_input)
    elif Switch4.value() == 1 and len(user_input)<4: #if the fourth switch is pressed and the set of numbers is less than 4, add 3 to the list
        user_input.append(3)
        sleep(0.5)
        print (user_input)
        
    if len(user_input) >= len(correct) and user_input != correct: # if the set of numbers the users inputs is greater than or equal to four, the number of items in the correct list, and the lists do not match, reset the list. 
        user_input=[]
        audio = I2S(0, # This must be either 0 or 1 for ESP32 #it will also play an audio file to say that your code was wrong
            sck=sck_pin, ws=ws_pin, sd=sd_pin,
            mode=I2S.TX,
            bits=16,
            format=I2S.MONO,
            rate= 88200, # This must match the sample rate of your file!
            ibuf=10000)
        
        WAVeFILE = "Errorsound.wav"
        BUFFER_SIZE = 10000
        wav = open(WAVeFILE, "rb")
        pos = wav.seek(44) 
        buf = bytearray(BUFFER_SIZE)
        wav_samples_mv = memoryview(buf)


        try:
            while True:
                bytes_read = wav.readinto(wav_samples_mv)
                if bytes_read == 0:
                   break 
                else:
                    num_written = audio.write(wav_samples_mv[:bytes_read])

        except (KeyboardInterrupt) as e:
            pass

        audio.deinit()
        
    if user_input == correct: #if the code entered is correct, unlock the water bottle with the motor and play the sound to say it is correct
        servo.duty(50)
        audio = I2S(0, # This must be either 0 or 1 for ESP32
            sck=sck_pin, ws=ws_pin, sd=sd_pin,
            mode=I2S.TX,
            bits=16,
            format=I2S.MONO,
            rate= 88200, # This must match the sample rate of your file!
            ibuf=10000)
        
        WAVcFILE = "Correctsound.wav"
        BUFFER_SIZE = 10000
        wav = open(WAVcFILE, "rb")
        pos = wav.seek(44) 
        buf = bytearray(BUFFER_SIZE)
        wav_samples_mv = memoryview(buf)


        try:
            while True:
                bytes_read = wav.readinto(wav_samples_mv)
                if bytes_read == 0:
                   break 
                else:
                    num_written = audio.write(wav_samples_mv[:bytes_read])

        except (KeyboardInterrupt) as e:
            pass

        audio.deinit()
        audio = I2S(0, # This must be either 0 or 1 for ESP32
            sck=sck_pin, ws=ws_pin, sd=sd_pin,
            mode=I2S.TX,
            bits=16,
            format=I2S.MONO,
            rate= 88200, # This must match the sample rate of your file!
            ibuf=10000)
        
        WAVdFILE = "drink.wav"
        BUFFER_SIZE = 10000
        wav = open(WAVdFILE, "rb")
        pos = wav.seek(44) 
        buf = bytearray(BUFFER_SIZE)
        wav_samples_mv = memoryview(buf)


        try:
            while True:
                bytes_read = wav.readinto(wav_samples_mv)
                if bytes_read == 0:
                   break 
                else:
                    num_written = audio.write(wav_samples_mv[:bytes_read])

        except (KeyboardInterrupt) as e:
            pass

        audio.deinit()
        
        
    
        user_input = [] #once the sound file is played reset the code and relock the bottle
        servo.duty(80)
        audio.deinit()
        print("done")
        
    else:
        servo.duty(80)
    
    

