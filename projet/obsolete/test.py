#! /usr/bin/env python
# enable functions and methods to manage the Pi
import RPi.GPIO as GPIO
import time

def getLuminosity(controlPin, readOutPin):
    #check if the sensor is powered on
    if GPIO.input(controlPin) == GPIO.HIGH:
        #check the value of the sensor
        if GPIO.input(readOutPin) == GPIO.HIGH:
            #print "light detected on pin :", readOutPin
            return True
        else :
            #print "light not detected on pin :", readOutPin
            return False
    else :
        #the sensor is powered off, there is no value
        return None

def turnOnOff(controlPin):
    #check if the sensor is powered on
    if GPIO.input(controlPin) == GPIO.HIGH:
        #power off the sensor
        GPIO.output(controlPin, GPIO.LOW)
        #print "pin :", controlPin,"is turned off"
        return False
    else :
        GPIO.output(LED, GPIO.HIGH)
        #print "pin :", controlPin,"is turned on"
        return True

def turnOn(controlPin):
    #check if the sensor is powered on
    if GPIO.input(controlPin) == GPIO.LOW:
        #power on the sensor
        GPIO.output(controlPin, GPIO.HIGH)
        #print "turn off pin :", controlPin
        return True
    else:
        #the sensor is already powered on
        return False
    
def turnOff(controlPin):
    #check if the sensor is powered on
    if GPIO.input(controlPin) == GPIO.HIGH:
        #power off the sensor
        GPIO.output(controlPin, GPIO.LOW)
        #print "turn off pin :", controlPin
        return True
    else:
        #the sensor is already powered off
        return False

def getOnOffState(controlPin):
    #check if the sensor is powered on
    if GPIO.input(controlPin) == GPIO.HIGH:
        #print "pin :", controlPin,"is on"
        return True
    else :
        #print "pin :", controlPin,"is off"
        return False

# setup the pin name for ease of use
LED = 17
LDR = 27

# setup the enumeration based on gpio references 
GPIO.setmode(GPIO.BCM)

# setup the port as output or input
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(LDR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# setup the state of the port 
GPIO.output(LED, GPIO.LOW)


# code of protection; if has no problem the block try will keep always on
try:
    while True:
        turnOnOff(LED)
        luminosityValue = getLuminosity(LED, LDR)
        if luminosityValue == True:
            print "light detected " 
            time.sleep(1)
        elif luminosityValue == False:
            print "light not detected " 
            time.sleep(1)
        else:
            print "sensor poweroff" 
            time.sleep(1)

# exceptions are anything that interrupt the try block.
# if a CTRL_C be pressed
except KeyboardInterrupt:
# setup the gpio to default values; finish any transmission of energy
    GPIO.cleanup()
