from __future__ import unicode_literals
from picamera import PiCamera
import time


class CameraPi:
    def __init__(self, path = '../Captures/'):
        self.camera = PiCamera()
        self.path = path 
    
    def takePicture(self, name = 'image'):
		named_tuple = time.localtime()
		time_string = time.strftime("_%Y-%m-%d_%Hh-%Mm-%Ss", named_tuple)
		if (name == 'image'):
			name = name + time_string
		ext = '.jpg'
		self.camera.start_preview()
		time.sleep(3)
		name = self.path + name + ext
		self.camera.capture(name)
		self.camera.stop_preview()
		return name
        

            
if __name__ == '__main__': 
	camera = CameraPi()
	camera.takePicture(name = 'preview')
