#! /usr/bin/env python
# enable functions and methods to manage the Pi
from actuator.servomotor import Servomotor
from sensor.ldr import LDR
import RPi.GPIO as GPIO
import time

class Feeder:
    def __init__(self, LDR_controlPin, LDR_readOutPin, Servomotor_controlPin, Servomotor_signalOutPin, down = 180, up = 0):
        self.up = up
        self.down = down
        self.servomotor = Servomotor(Servomotor_controlPin, Servomotor_signalOutPin)
        self.ldr = LDR(LDR_controlPin, LDR_readOutPin)
        self.powerState = False

    def foodStatus(self):
        #check if it is powered on
        if self.powerState == GPIO.HIGH:
            if self.ldr.getLuminosityOnce () == True:
                return False
            else:
                return True
        else :
            #it is powered off, there is no value
            return None

    def foodStatusOnce(self):
        #check if it is powered on
        if self.powerState == GPIO.HIGH:
            return foodStatus()
        else :
            self.turnOn()
            state = foodStatus()
            self.turnOff()
            return state
            return None
        
    def feed(self, iteration = 1, duration = 0.75):
        #check if it is powered on
        if self.powerState == GPIO.HIGH:
            for x in range(iteration):
                self.servomotor.setAngle(self.down)
                time.sleep(duration)
                self.servomotor.setAngle(self.up)
            return True
        else :
            return False

    def feedOnce(self, iteration = 1, duration = 0.75):
        #check if it is powered on
        if self.powerState == GPIO.HIGH:
            return feed(self, iteration, duration)
        else :
            self.turnOn()
            state = feed(self, iteration, duration)
            self.turnOff()
            return state
    

    def turnOnOff(self):
        #check if the actuator is powered on
        if self.powerState == GPIO.HIGH:
            return self.turnOff()
        else :
            return self.turnOn()

    def turnOn(self):
        #check if the actuator is powered on
        if self.powerState == GPIO.HIGH:
            #the sensor is already powered on
            return False
        else:
            #power on the actuator
            self.servomotor.turnOn()
            self.ldr.turnOn()
            self.powerState = True
            #print "turn on pin :", self.controlPin
            return True
            
    def turnOff(self):
        #check if the actuator is powered on
        if self.powerState == GPIO.LOW:
            #the actuator is already powered off
            return False
        else:
            #power off the actuator
            self.servomotor.turnOff()
            self.ldr.turnOff()
            self.powerState = False
            #print "turn off pin :", self.controlPin
            return True

    def getOnOffState(self):
        return self.powerState

if False:
    # setup the pin name for ease of use
    SERVOMOTOR_TRANSISTOR = 27
    SERVOMOTOR_CONTROL = 18
    LDR_TRANSISTOR = 17
    LDR_SENSOR = 22

    # setup the enumeration based on gpio references 
    GPIO.setmode(GPIO.BCM)

    # setup the port as output or input

    # setup the state of the port


    # code of protection; if has no problem the block try will keep always on
    try:
        feeder1 = Feeder(LDR_TRANSISTOR, LDR_SENSOR, SERVOMOTOR_TRANSISTOR, SERVOMOTOR_CONTROL)
        feeder1.turnOn()
        while True:
            time.sleep(2) # sleep 1 second
            print "position :", feeder1.servomotor.getAngle()
            if feeder1.foodStatus() == True:
                feeder1.feed()
            else:
                print "no food"

    # exceptions are anything that interrupt the try block.
    # if a CTRL_C be pressed
    except KeyboardInterrupt:
    # setup the gpio to default values; finish any transmission of energy
        GPIO.cleanup()
