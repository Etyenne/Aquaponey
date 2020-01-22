#! /usr/bin/env python
# enable functions and methods to manage the Pi
from __future__ import unicode_literals
import RPi.GPIO as GPIO
import time

class WaterLevel:
    def __init__(self, controlPin, readOutPin):
        if GPIO.getmode() != 11:
            GPIO.setmode(GPIO.BCM)
        self.controlPin = controlPin
        self.readOutPin = readOutPin
        # setup the port as output or input
        GPIO.setup(self.controlPin, GPIO.OUT)
        GPIO.setup(self.readOutPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        # setup the state of the port 
        GPIO.output(self.controlPin, GPIO.LOW)
        self.powerState = False

        
    def getWaterLevel(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            #check the value of the sensor
            if GPIO.input(self.readOutPin) == GPIO.HIGH:
                #print "light detected on pin :", readOutPin
                return True
            else :
                #print "light not detected on pin :", readOutPin
                return False
        else :
            #the sensor is powered off, there is no value
            return None

    def getWaterLevelOnce(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            return self.getWaterLevel()
        else :
            self.turnOn()
            waterLevel = self.getWaterLevel()
            self.turnOff()
            return waterLevel

    def turnOnOff(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            return self.turnOff()
        else :
            return self.turnOn()

    def turnOn(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            #the sensor is already powered on
            return False
        else:
            #power on the sensor
            GPIO.output(self.controlPin, GPIO.HIGH)
            self.powerState = True
            #print "turn on pin :", self.controlPin
            return True
            
    def turnOff(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.LOW:
            #the sensor is already powered off
            return False
        else:
            #power off the sensor
            GPIO.output(self.controlPin, GPIO.LOW)
            self.powerState = False
            #print "turn off pin :", self.controlPin
            return True

    def getOnOffState(self):
        return self.powerState

