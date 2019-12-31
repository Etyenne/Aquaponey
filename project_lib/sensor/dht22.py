#! /usr/bin/env python
# enable functions and methods to manage the Pi
import RPi.GPIO as GPIO
# enable use of functions of time
import time
import sys
import Adafruit_DHT


class DHT22:
    def __init__(self, controlPin, readOutPin):
        self.controlPin = controlPin
        self.readOutPin = readOutPin
        self.sensorType = 22
        # setup the port as output or input
        GPIO.setup(self.controlPin, GPIO.OUT)
        GPIO.setup(self.readOutPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        # setup the state of the port 
        GPIO.output(self.controlPin, GPIO.LOW)
        self.powerState = False
        
        
    def getOnOffState(self):
        return self.powerState
    
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

    def turnOnOff(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            return self.turnOff()
        else :
            return self.turnOn()

    def getHumidity(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            #check the value of the sensor
            humidity, temperature = Adafruit_DHT.read_retry(self.sensorType, self.readOutPin)
        
            if humidity is not None and temperature is not None:
                #print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
                return humidity
            else:
                #print "no value"
                return None
        else :
            #the sensor is powered off, there is no value
            return None

    def getTemperature(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            #check the value of the sensor
            humidity, temperature = Adafruit_DHT.read_retry(self.sensorType, self.readOutPin)
        
            if humidity is not None and temperature is not None:
                #print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
                return temperature
            else:
                #print "no value"
                return None
        else :
            #the sensor is powered off, there is no value
            return None

    def getHumidityAndTemperature(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            #check the value of the sensor
            humidity, temperature = Adafruit_DHT.read_retry(self.sensorType, self.readOutPin)
        
            if humidity is not None and temperature is not None:
                #print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
                return humidity, temperature
            else:
                #print "no value"
                return None, None
        else :
            #the sensor is powered off, there is no value
            return None

    def getHumidityOnce(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            return self.getHumidity()
        else :
            self.turnOn()
            humidity = self.getHumidity()
            self.turnOff()
            return humidity

    def getTemperatureOnce(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            return self.getTemperature()
        else :
            self.turnOn()
            temperature = self.getTemperature()
            self.turnOff()
            return temperature

    def getHumidityAndTemperatureOnce(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            return self.getHumidityAndTemperature()
        else :
            self.turnOn()
            humidity, temperature = self.getHumidityAndTemperature()
            self.turnOff()
            return humidity, temperature


DHT22_SENSOR = 27
DHT22_TRANSISTOR = 18

GPIO.setmode(GPIO.BCM)

# setup the enumeration based on gpio references 1

# setup the port as output, in this PIN the energy will go out


# setup to have energy by the port


# code of protection; if has no problem the block try will keep always on
try:
    capteurDHT_1 = DHT22(DHT22_TRANSISTOR, DHT22_SENSOR)
# infinite loop
    while True:
        print "..."
        print "getting value ..."
        humidity, temperature = capteurDHT_1.getHumidityAndTemperatureOnce()
        
        if humidity is not None and temperature is not None:
            print 'Temp = {0:0.1f}*C  Humidity = {1:0.1f}%'.format(temperature, humidity)
        else:
            print "no value"
		

# exceptions are anything that interrupt the try block.
# if a CTRL_C be pressed
except KeyboardInterrupt:
# setup the gpio to default values; finish any transmission of energy
	GPIO.cleanup()
