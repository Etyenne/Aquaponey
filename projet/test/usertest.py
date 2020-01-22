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
path ="basic"

#connection au server
client = HelperClient(server=(host, port))
os.system('clear')

choice = 1

while int(choice) != 0:
    print ("want to know: 0-Exit 1-Temperature 2-Brightness")
    functionnality=['out','temperature','brightness']
    choice = input()
    os.system('clear')

    print ("you have chosen", functionnality[int(choice)])

    if int(choice) == 1:
        #GET temperature
        response = client.get("temperature")
        os.system('clear')
        print (response.payload)

    if int(choice) == 2:
        #GET brightness
        response = client.get("brightness")
        os.system('clear')
        print (response.payload)

    if int(choice) == 0:
        client.stop()

os.system('clear')
