#! pip install CoAPthon3

#python -m pip install CoAPthon3

#import sys
#!{sys.executable} -m pip install CoAPthon3

############COAP SERVER###############
from __future__ import unicode_literals
from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

from sensor.ldr import LDR
from sensor.dht22 import DHT22
from sensor.water_level import WaterLevel
from actuator.servomotor import Servomotor
from actuator.light import Light



# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)

class BasicResource(Resource):
  def __init__(self, name="BasicResource", coap_server=None):
    super (BasicResource, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
    self.payload = "Resource Data"

  def render_GET(self, request):
    return self

  def render_PUT(self, request):
    self.payload = request.payload 
    return self

  def render_POST(self, request):
    res = BasicResource()
    res.location_query = request.uri_query
    res.payload = request.payload
    return res
  
  def render_DELETE(self, request):
    return True

class PowerManagment(Resource):
  def __init__(self, element, elementName, name="waterLevelTRest", coap_server=None):
    super (PowerManagment, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
    clientMongo = MongoClient('mongodb://localhost:27017')
    self.database = clientMongo.aquaponey
    self.element = element
    self.elementName = elementName

  #~ def render_GET(self, request):
    #~ print ('request status : ' + self.elementName)
    
    #~ elementState = self.element.getOnOffState()
    #~ data = {
        #~ 'elementName' : self.elementName,
        #~ 'date' : datetime.now(),
        #~ 'state' : elementState
    #~ }
    #~ self.database.powerState.insert_one(data)
    #~ self.payload = data
    #~ return self

  #~ def render_PUT(self, request):
    #~ if(request.state == 'on'):
      #~ elementState = self.element.turnOn()
    #~ elif(request.state == 'off'):
      #~ elementState = self.element.turnOff()
    #~ elif(request.state == 'onOff'):
      #~ elementState = self.element.turnOnOff()

    #~ data = {
        #~ 'elementName' : self.elementName,
        #~ 'date' : datetime.now(),
        #~ 'state' : elementState
    #~ }
    #~ self.database.powerState.insert_one(data)

    #~ return self
    
  def render_GET(self, request):
    return self
    
  def render_PUT(self, request):
    self.payload = self.element.getOnOffState()

    return self

  def render_POST(self, request):
    return False
  
  def render_DELETE(self, request):
    return False

class WaterLevelRest(Resource):
  def __init__(self, name="WaterLevelRest", coap_server=None):
    super (WaterLevelRest, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
    #clientMongo = MongoClient('mongodb://localhost:27017')
    WaterLevel_TRANSISTOR = 17
    WaterLevel_SENSOR = 10

    element =  WaterLevel(WaterLevel_TRANSISTOR, WaterLevel_SENSOR)
    #self.database = clientMongo.aquaponey
    self.element = element
    self.elementName = 'waterLevelSensor_1'
    
    #~ def render_GET(self, request):

    #~ waterLevelValue = self.element.getWaterLevelOnce()

    #~ data = {
      #~ 'elementName' : self.elementName,
      #~ 'date' : datetime.now(),
      #~ 'valueName' : 'waterLevel',
      #~ 'value' : waterLevelValue
    #~ }
    #~ self.database.reading.insert_one(data)
    #~ return self

  def render_GET(self, request):
    return self

  def render_PUT(self, request):
    self.payload = self.element.getWaterLevelOnce()
    return self

  def render_POST(self, request):
    return False
  
  def render_DELETE(self, request):
    return False

class DHT22Rest(Resource):
  def __init__(self, element, elementName, name="DHT22Rest", coap_server=None):
    super (DHT22Rest, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
    clientMongo = MongoClient('mongodb://localhost:27017')
    self.database = clientMongo.aquaponey
    self.element = element
    self.elementName = elementName

  def render_GET(self, request):

    if(request.valueName == 'temperature'):
      elementTemperature = self.element.getTemperatureOnce()
      data = {
        'elementName' : self.elementName,
        'date' : datetime.now(),
        'valueName' : 'temperature',
        'value' : elementTemperature
      }
      self.database.reading.insert_one(data)

    elif(request.valueName == 'humidity'):
      elementHumidity = self.element.getHumidityOnce()
      data = {
        'elementName' : self.elementName,
        'date' : datetime.now(),
        'valueName' : 'humidity',
        'value' : elementHumidity
      }
      database.reading.insert_one(data)

    elif(request.valueName == 'humidityAndTemperature'):
      elementHumidity, elementTemperature = self.element.getHumidityAndTemperatureOnce()
      data.temperature = {
        'elementName' : self.elementName,
        'date' : datetime.now(),
        'valueName' : 'temperature',
        'value' : elementTemperature
      }
      self.database.reading.insert_one(data.temperature)
      data.humidity = {
        'elementName' : self.elementName,
        'date' : datetime.now(),
        'valueName' : 'humidity',
        'value' : elementHumidity
      }
      self.database.reading.insert_one(data.humidity)

    return data

  def render_PUT(self, request):
    return False

  def render_POST(self, request):
    return False
  
  def render_DELETE(self, request):
    return False

class LDRRest(Resource):
  def __init__(self, element, elementName, name="LDRRest", coap_server=None):
    super (LDRRest, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
    clientMongo = MongoClient('mongodb://localhost:27017')
    self.database = clientMongo.aquaponey
    self.element = element
    self.elementName = elementName

  def render_GET(self, request):
    luminosityValue = self.element.getLuminosityOnce()

    data = {
      'elementName' : self.elementName,
      'date' : datetime.now(),
      'valueName' : 'luminosity',
      'value' : luminosityValue
    }
    self.database.reading.insert_one(data)
    return data

  def render_PUT(self, request):
    return False

  def render_POST(self, request):
    return False
  
  def render_DELETE(self, request):
    return False

class ServomotorRest(Resource):
  def __init__(self, element, elementName, name="ServomotorRest", coap_server=None):
    super (ServomotorRest, self).__init__(name, coap_server, visible=True, observable=True, allow_children=True)
    clientMongo = MongoClient('mongodb://localhost:27017')
    self.database = clientMongo.aquaponey
    self.element = element
    self.elementName = elementName

  def render_GET(self, request):

    angleValue = self.element.getAngle()

    data = {
      'elementName' : self.elementName,
      'date' : datetime.now(),
      'valueName' : 'angle',
      'value' : angleValue
    }
    self.database.reading.insert_one(data)
    return data

  def render_PUT(self, request):
    angleValue = self.element.setAngleOnce(anglerequest)

    data = {
      'elementName' : self.elementName,
      'date' : datetime.now(),
      'userID' : '',
      'action' : 'angle',
      'target' : angleValue
    }
    self.database.action.insert_one(data)
    return data

  def render_POST(self, request):
    return False
  
  def render_DELETE(self, request):
    return False

class CoAPServer(CoAP):
  def __init__(self, host, port):
    CoAP.__init__(self, (host, port))
    #clientMongo = MongoClient('mongodb://localhost:27017')
    #self.database = clientMongo.aquaponey


    self.add_resource( 'waterLevelSensor/', WaterLevelRest())
    #self.add_resource( 'waterLevelSensor/', PowerManagment( element, 'waterLevelSensor_1'))
    self.add_resource( 'basic/', BasicResource())
##
##    elementList = []
##    elementList = self.database.element.find()
##
##    for element in elementList:
##      if element['installed'] == True:
##        if element['classification'] == 'DHT22' :
##          self.addDHT22( element.name, element.controlPin, element.readOutPin, element.name)
##        
##        elif element['classification'] == 'LDR' :
##          self.addLDR( element.name, element.controlPin, element.readOutPin, element.name)
##
##        elif element['classification'] == 'Light' :
##          self.addLight( element.name, element.controlPin, element.name)
##
##        elif element['classification'] == 'WaterLevel' :
##          self.addWaterLevel( element.name, element.controlPin, element.readOutPin, element.name)
##
##        elif element['classification'] == 'Servomotor' :
##          self.addServomotor( element.name, element.controlPin, element.signalOutPin, element.name)
        
  
  def addServomotor(self, name, SERVOMOTOR_TRANSISTOR, SERVOMOTOR_CONTROL, elementName):
    element = Servomotor(SERVOMOTOR_TRANSISTOR, SERVOMOTOR_CONTROL)
    self.add_resource( name+'/actuator/', ServomotorRest( element, elementName))
    self.add_resource( name+'/power/', PowerManagment( element, elementName))

  def addLight(self, name, LIGHT_TRANSISTOR, elementName):
    element = Light(LIGHT_TRANSISTOR)
    self.add_resource( name+'/power/', PowerManagment( element, elementName))

  def addLDR(self, name, LDR_TRANSISTOR, LDR_SENSOR, elementName):
    element = LDR(LDR_TRANSISTOR, LDR_SENSOR)
    self.add_resource( name+'/sensor/', dht22Rest( element, elementName))
    self.add_resource( name+'/power/', PowerManagment( element, elementName))

  def addDHT22(self, name, DHT22_TRANSISTOR, DHT22_SENSOR, elementName):
    element = DHT22(DHT22_TRANSISTOR, DHT22_SENSOR)
    self.add_resource( name+'/sensor/', LightRest( element, elementName))
    self.add_resource( name+'/power/', PowerManagment(element, elementName))

  def addWaterLevel(self, name, WaterLevel_TRANSISTOR, WaterLevel_SENSOR, elementName):
    element =  WaterLevel(WaterLevel_TRANSISTOR, WaterLevel_SENSOR)
    self.add_resource( name+'/sensor/', WaterLevelRest( element, elementName))
    self.add_resource( name+'/power/', PowerManagment( element, elementName))


def main():

  host = "0.0.0.0"
  port = 5683

  # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
  clientMongo = MongoClient('mongodb://localhost:27017')
  database = clientMongo.aquaponey

  server = CoAPServer(host, port) 

  try:
    print('The server is listenning on port 5683.')
    server.listen(10)
        
  except KeyboardInterrupt:
    print ("ServerShutdown")
    server.close()
    print ("Exiting...")

if __name__ == '__main__':
  main()
