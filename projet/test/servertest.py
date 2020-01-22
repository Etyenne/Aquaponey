#! pip install CoAPthon3

#python -m pip install CoAPthon3

#import sys
#!{sys.executable} -m pip install CoAPthon3

############COAP SERVER###############
from __future__ import unicode_literals
from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource

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

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        path_1 ='basic/'
        self.add_resource(path_1, BasicResource())
        path_2 ='temperature/'
        self.add_resource(path_2, BasicResource())
        path_3 ='brightness/'
        self.add_resource(path_3, BasicResource())

def main():

    host = "0.0.0.0"
    port = 5683
    server = CoAPServer(host, port) 

    try:
        server.listen(10)
    except KeyboardInterrupt:
        print ("ServerShutdown")
        server.close()
        print ("Exiting...")

if __name__ == '__main__':
    main()
