#! /usr/bin/env python
# enable functions and methods to manage the Pi
import RPi.GPIO as GPIO
import time

class Servomotor:
    def __init__(self, controlPin, signalOutPin):
        self.controlPin = controlPin
        self.signalOutPin = signalOutPin
        
        # setup the port as output or input
        GPIO.setup(self.controlPin, GPIO.OUT)
        GPIO.setup(self.signalOutPin, GPIO.OUT)

        # setup the state of the port
        self.signalPWM = GPIO.PWM(self.signalOutPin, 50)
        
        #initialise position
        angle = 0
        dutyCycle = (angle / 18) + 2 
        self.signalPWM.start(2)
        self.angle = angle
        
        # setup the state of the port
        GPIO.output(self.controlPin, GPIO.LOW)
        self.powerState = False

    def __del__(self):
        # stop the pulse emission
        self.signalPWM.stop()

    def setAngle(self, angle = 0):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            #check the value of the angle
            if angle > 180 :
                angle = 180
            if angle < 0 :
                angle = 0
            #calculate the value of the duty cycle
            dutyCycle = (angle / 18) + 2 
            self.signalPWM.ChangeDutyCycle(dutyCycle)
            self.angle = angle
            return True
        else :
            return False

    def setAngleOnce(self, angle):
        #check if it is powered on
        if self.pwerState == GPIO.HIGH :
            return self.setAngle(self, angle)
        else:
            self.turnOn()
            state = self.setAngle(self, angle)
            self.turnOff()
            return state

    def getAngle(self):
        return self.angle

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

if False:
    # setup the pin name for ease of use
    SERVOMOTOR_TRANSISTOR = 27
    SERVOMOTOR_CONTROL = 18

    # setup the enumeration based on gpio references 
    GPIO.setmode(GPIO.BCM)

    # setup the port as output or input

    # setup the state of the port


    # code of protection; if has no problem the block try will keep always on
    try:
        actuatorSERVOMOTOR_1 = Servomotor(SERVOMOTOR_TRANSISTOR, SERVOMOTOR_CONTROL)
        actuatorSERVOMOTOR_1.turnOn()
        while True:
            angle = 0
            print "angle :", angle
            actuatorSERVOMOTOR_1.setAngle(angle)
            time.sleep(3) # sleep 1 second
            angle = 180
            print "angle :", angle
            actuatorSERVOMOTOR_1.setAngle(angle)
            time.sleep(3) # sleep 1 second
            
    # exceptions are anything that interrupt the try block.
    # if a CTRL_C be pressed
    except KeyboardInterrupt:
    # setup the gpio to default values; finish any transmission of energy
        GPIO.cleanup()
