#! pip install CoAPthon3

#python -m pip install CoAPthon3

#import sys
#!{sys.executable} -m pip install CoAPthon3

############COAP CLIENT###############
from __future__ import unicode_literals
from coapthon.client.helperclient import HelperClient
from coapthon.client import *

import time

host = "127.0.0.1"
port = 5683
path ="basic"


client = HelperClient(server=(host, port))


#TEMPERATURE & BRIGHTNESS PUT EVERY 5 SECONDS

while True:
    print("###PUT###")
    path ="temperature"
    #add input from temperature sensor in 'payload' field
    payload = '10.5C'
    response = client.put(path,payload)

    print("###PUT###")
    path ="brightness"
    #add input from brightness sensor in 'payload' field
    payload = '1200lux'
    response = client.put(path,payload)

    time.sleep(5)


client.stop()
