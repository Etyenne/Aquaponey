 
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer  
import os
import time
from sensor.ldr import LDR
from sensor.dht22 import DHT22
from sensor.water_level import WaterLevel
from sensor.ds18b20 import DS18B20
from sensor.camera import CameraPi
from actuator.servomotor import Servomotor
from actuator.light import Light
import RPi.GPIO as GPIO


waterlevel =  WaterLevel(26, 16)
dht22 = DHT22(19, 27)
ds18b20 = DS18B20(23, 4) #never change pin 4
luminosity = LDR(13, 21)
food = LDR(3, 2)
light1 = Light(20)
heater = Light(12)
pump = Light(17)
oxygenpump = Light(24)
servo = Servomotor(22, 18)
#camera = CameraPi(path = 'Captures/')
  
#Create custom HTTPRequestHandler class  
class ProjectHTTPRequestHandler(BaseHTTPRequestHandler):
    
  #handle GET command  
  def do_GET(self):  
    rootdir = '/home/pi/Bureau/projet' #file location  
    try:  
      print('... : ')  
      print(rootdir + self.path)  
  
      if self.path.endswith('.html'):  
        f = open(rootdir + self.path) #open requested file  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
  
        #send file content to client  
        self.wfile.write(f.read())  
        f.close()  
        return  
        
      if self.path.endswith('.jpg'):  
        f = open(rootdir + self.path) #open requested file  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','image/jpg')  
        self.end_headers()  
  
        #send file content to client  
        self.wfile.write(f.read())  
        f.close()  
        return  
        
      if self.path == '/waterlevel/power':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = waterlevel.getOnOffState()
        self.wfile.write(value)  
        return  
        
      if self.path == '/waterlevel/value':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = waterlevel.getWaterLevelOnce()
        self.wfile.write(value)  
        return  
        
      if self.path == '/dht22/power':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = dht22.getOnOffState()
        self.wfile.write(value)  
        return  
        
      if self.path == '/dht22/temperature':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = dht22.getTemperatureOnce()
        self.wfile.write(value)  
        return  
        
      if self.path == '/dht22/humidity':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = dht22.getHumidityOnce()
        self.wfile.write(value)  
        return  
        
      if self.path == '/ds18b20/power':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = ds18b20.getOnOffState()
        self.wfile.write(value)  
        return  
        
      if self.path == '/ds18b20/temperature':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = ds18b20.getTemperatureOnce()
        self.wfile.write(value)  
        return  
        
      if self.path == '/luminosity/power':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = luminosity.getOnOffState()
        self.wfile.write(value)  
        return  
        
      if self.path == '/luminosity/value':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = luminosity.getLuminosityOnce()
        self.wfile.write(value)  
        return 
        
      if self.path == '/food/power':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = food.getOnOffState()
        self.wfile.write(value)  
        return  
        
      if self.path == '/food/value':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = food.getLuminosityOnce()
        self.wfile.write(value)  
        return 
        
      if self.path == '/light/power':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = light1.getOnOffState()
        self.wfile.write(value)  
        return  
        
      if self.path == '/pump/power':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = pump.getOnOffState()
        self.wfile.write(value)  
        return  
        
      if self.path == '/heater/power':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = heater.getOnOffState()
        self.wfile.write(value)  
        return  
        
      if self.path == '/oxygenpump/power':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = oxygenpump.getOnOffState()
        self.wfile.write(value)  
        return  
        
      if self.path == '/servo/power':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = servo.getOnOffState()
        self.wfile.write(value)  
        return  
        
      if self.path == '/servo/value':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = servo.getAngle()
        self.wfile.write(value)  
        return
        
      if self.path == '/camera/picture':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        value = camera.takePicture()
        self.wfile.write(value)  
        return  
        
      
    except IOError:  
      self.send_error(404, 'file not found')  
      
  def do_PUT(self):  
    rootdir = '/home/pi/Bureau/projet' #file location  
    try:  
      print('... : ')  
      print(rootdir + self.path)  
        
      if self.path == '/waterlevel/off':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = waterlevel.turnOff()
        self.wfile.write(value)  
        return  
        
      if self.path == '/waterlevel/on':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = waterlevel.turnOn()
        self.wfile.write(value)  
        return  
        
      if self.path == '/dht22/off':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = dht22.turnOff()
        self.wfile.write(value)  
        return  
        
      if self.path == '/dht22/on':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = dht22.turnOn()
        self.wfile.write(value)  
        return  
        
      if self.path == '/ds18b20/off':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = ds18b20.turnOff()
        self.wfile.write(value)  
        return  
        
      if self.path == '/ds18b20/on':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = ds18b20.turnOn()
        self.wfile.write(value)  
        return  
        
      if self.path == '/light/off':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = light1.turnOff()
        self.wfile.write(value)  
        return  
        
      if self.path == '/light/on':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = light1.turnOn()
        self.wfile.write(value)  
        return  
        
      if self.path == '/heater/off':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = heater.turnOff()
        self.wfile.write(value)  
        return  
        
      if self.path == '/heater/on':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = heater.turnOn()
        self.wfile.write(value)  
        return  
        
      if self.path == '/pump/off':  

        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = pump.turnOff()
        self.wfile.write(value)  
        return  
        
      if self.path == '/pump/on':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = pump.turnOn()
        self.wfile.write(value)  
        return  
        
      if self.path == '/oxygenpump/off':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = oxygenpump.turnOff()
        self.wfile.write(value)  
        return  
        
      if self.path == '/oxygenpump/on':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = oxygenpump.turnOn()
        self.wfile.write(value)  
        return  
  
      if self.path == '/luminosity/off':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = luminosity.turnOff()
        self.wfile.write(value)  
        return  
        
      if self.path == '/luminosity/on':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = luminosity.turnOn()
        self.wfile.write(value)  
        return       
        
      if self.path == '/food/off':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = food.turnOff()
        self.wfile.write(value)  
        return  
        
      if self.path == '/food/on':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = food.turnOn()
        self.wfile.write(value)  
        return    
        
      if self.path == '/servo/off':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = servo.turnOff()
        self.wfile.write(value)  
        return  
        
      if self.path == '/servo/on':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = servo.turnOn()
        self.wfile.write(value)  
        return    
        
      if self.path == '/servo/high':  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = servo.setAngleOnce(150)
        #time.sleep(2)
        self.wfile.write(value)  
        return 
        
      if self.path == '/servo/low':  
        
        #send code 200 response  
        self.send_response(200)  
         
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        value = servo.setAngleOnce(10)
        #time.sleep(2) 
        self.wfile.write(value)  
        return 
        
      if self.path == '/all/off':  
        
        #send code 200 response  
        self.send_response(200)  
         
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
        
        waterlevel.turnOff()
        dht22.turnOff()
        ds18b20.turnOff()
        luminosity.turnOff()
        food.turnOff()
        light1.turnOff()
        heater.turnOff()
        pump.turnOff()
        oxygenpump.turnOff()
        servo.turnOff()
        
        self.wfile.write('True')  
        return 
      
    except IOError:  
      self.send_error(404, 'file not found')  
      
def run():
  try:
    print('http server is starting...')  
    
    #ip and port of servr  
    #by default http server port is 80  
    server_address = ('127.0.0.1', 9000)  
    httpd = HTTPServer(server_address, ProjectHTTPRequestHandler)  
    print('http server is running...')  
    httpd.serve_forever()

  # exceptions are anything that interrupt the try block.
  # if a CTRL_C be pressed
  except KeyboardInterrupt:
  # setup the gpio to default values; finish any transmission of energy
      GPIO.cleanup()

if __name__ == '__main__':  
  run()  
