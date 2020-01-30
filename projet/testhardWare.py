#! /usr/bin/env python
# enable functions and methods to manage the Pi
from __future__ import unicode_literals
import RPi.GPIO as GPIO
import time
import os 
import glob 


class WaterTemperature:
    def __init__(self, controlPin, readOutPin):
        if GPIO.getmode() != 11:
            GPIO.setmode(GPIO.BCM)
        self.controlPin = controlPin
        self.readOutPin = readOutPin
        # setup the port as output or input
        GPIO.setup(self.controlPin, GPIO.OUT)
        GPIO.setup(self.readOutPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

        # setup the state of the port 
        GPIO.output(self.controlPin, GPIO.LOW)
        self.powerState = False
        
        os.system('modprobe w1-gpio') 
        os.system('modprobe w1-therm') 

        base_dir = '/sys/bus/w1/devices/' 
        device_folder = glob.glob(base_dir + '28*')[0] 
        self.device_file = device_folder + '/w1_slave' 

    def read_temp_raw(self): 
        f = open(self.device_file, 'r') 
        lines = f.readlines() 
        f.close() 
        return lines 
                            
    def getTemperature(self): 
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            lines = self.read_temp_raw() 
            while lines[0].strip()[-3:] != 'YES': 
                time.sleep(0.2) 
                lines = read_temp_raw() 
            equals_pos = lines[1].find('t=') 
            if equals_pos != -1: 
                temp_string = lines[1][equals_pos+2:] 
                temp_c = float(temp_string) / 1000.0 
                temp_f = temp_c * 9.0 / 5.0 + 32.0
                return temp_c 
        else :
            #the sensor is powered off, there is no value
            return None
            
    def getTemperatureOnce(self):
        #check if the sensor is powered on
        if self.powerState == GPIO.HIGH:
            return self.getTemperature()
        else :
            self.turnOn()
            value = self.getTemperature()
            self.turnOff()
            return value
            
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


if __name__ == '__main__':  
    try:
        temp = WaterTemperature(17, 4)
        while True: 
            value = temp.getTemperatureOnce()
            print('temp : ' + str(value))  
            time.sleep(1) 
    except KeyboardInterrupt:
        # setup the gpio to default values; finish any transmission of energy
        GPIO.cleanup()
