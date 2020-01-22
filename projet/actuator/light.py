#! /usr/bin/env python
# enable functions and methods to manage the Pi
import RPi.GPIO as GPIO
import time

class Light:
    def __init__(self, controlPin):
        GPIO.setmode(GPIO.BCM)
        print('light pin :')
        print(controlPin)
        self.controlPin = controlPin
        # setup the port as output or input
        GPIO.setup(self.controlPin, GPIO.OUT)

        # setup the state of the port 
        GPIO.output(self.controlPin, GPIO.LOW)
        self.powerState = False

    def turnOnOff(self):
        #check if the actuator is powered on
        if self.powerState == GPIO.HIGH:
            return self.turnOff()
        else :
            return self.turnOn()

    def turnOn(self):
        print('light pin :')
        print(self.controlPin)
        #check if the actuator is powered on
        if self.powerState == GPIO.HIGH:
            #the sensor is already powered on
            return False
        else:
            #power on the actuator
            GPIO.output(self.controlPin, GPIO.HIGH)
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
            GPIO.output(self.controlPin, GPIO.LOW)
            self.powerState = False
            #print "turn off pin :", self.controlPin
            return True

    def getOnOffState(self):
        return self.powerState
