#! /usr/bin/env python
# enable functions and methods to manage the Pi
import RPi.GPIO as GPIO
import time

class Light:
    def __init__(self, controlPin):
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


# setup the pin name for ease of use
LIGHT_TRANSISTOR = 17

# setup the enumeration based on gpio references 
GPIO.setmode(GPIO.BCM)

# setup the port as output or input

# setup the state of the port


# code of protection; if has no problem the block try will keep always on
try:
    actuatorLIGHT_1 = Light(LIGHT_TRANSISTOR)
    while True:
        actuatorLIGHT_1.turnOnOff()
        lightState = actuatorLIGHT_1.getOnOffState()
        if lightState == True:
            print "light detected " 
            time.sleep(1)
        elif lightState == False:
            print "light not detected " 
            time.sleep(1)

# exceptions are anything that interrupt the try block.
# if a CTRL_C be pressed
except KeyboardInterrupt:
# setup the gpio to default values; finish any transmission of energy
    GPIO.cleanup()
#! /usr/bin/env python
# enable functions and methods to manage the Pi
import RPi.GPIO as GPIO
import time

class LDR:
    def __init__(self, controlPin, readOutPin):
        self.controlPin = controlPin
        self.readOutPin = readOutPin
        # setup the port as output or input
        GPIO.setup(self.controlPin, GPIO.OUT)
        GPIO.setup(self.readOutPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        # setup the state of the port 
        GPIO.output(self.controlPin, GPIO.LOW)
        self.powerState = False
        
    def getLuminosity(self):
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

    def getLuminosityOnce(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            return self.getLuminosity()
        else :
            self.turnOn()
            luminosity = self.getLuminosity()
            self.turnOff()
            return luminosity

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


# setup the pin name for ease of use
LDR_TRANSISTOR = 17
LDR_SENSOR = 27

# setup the enumeration based on gpio references 
GPIO.setmode(GPIO.BCM)

# setup the port as output or input

# setup the state of the port


# code of protection; if has no problem the block try will keep always on
try:
    capteurLDR_1 = LDR(LDR_TRANSISTOR, LDR_SENSOR)
    while True:
        capteurLDR_1.turnOnOff()
        luminosityValue = capteurLDR_1.getLuminosity()
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
