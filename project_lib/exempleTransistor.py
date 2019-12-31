#! /usr/bin/env python
# enable functions and methods to manage the Pi
import RPi.GPIO as GPIO
import time

LED = 17

# setup the enumeration based on gpio references 
GPIO.setmode(GPIO.BCM)

# setup the port as output or input
GPIO.setup(LED, GPIO.OUT)

# setup the state of the port 
GPIO.output(LED, GPIO.LOW)


# code of protection; if has no problem the block try will keep always on
try:
    while True:
        print("pin down \n")
        time.sleep(2)
        GPIO.output(LED, GPIO.HIGH)
        print("pin up \n")
        time.sleep(2)
        GPIO.output(LED, GPIO.LOW)

# exceptions are anything that interrupt the try block.
# if a CTRL_C be pressed
except KeyboardInterrupt:
# setup the gpio to default values; finish any transmission of energy
    GPIO.cleanup()
