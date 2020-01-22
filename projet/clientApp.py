#! pip install CoAPthon3

#python -m pip install CoAPthon3

#import sys
#!{sys.executable} -m pip install CoAPthon3

############COAP CLIENT###############
from __future__ import unicode_literals
from coapthon.client.helperclient import HelperClient
from coapthon.client import *

import os

host = "127.0.0.1"
port = 5683
path ="waterLevelSensor"

#connection au server
client = HelperClient(server=(host, port))
os.system('clear')

choice = 1

while int(choice) != 0:
    print ("want to know: 0-Exit 1-power state 2-add state")
    functionnality=['out','power','add state']
    choice = input()
    #~ os.system('clear')

    print ("you have chosen", functionnality[int(choice)])

    if int(choice) == 1:
        #GET temperature
        response = client.get('waterLevelSensor')
        #~ os.system('clear')
        print (' ')
        print (' response ==:> ')
        print (' ')
        print (response.payload)
        print (' ')
        
    if int(choice) == 2:
        #PUT brightness
        payload = "10.5C"
        response = client.put('waterLevelSensor',payload)
        #~ os.system('clear')
        print (response.payload)


    if int(choice) == 0:
        client.stop()

os.system('clear')
