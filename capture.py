#!/usr/bin/python
from sys import argv
import zbar
from PIL import Image
from sys import argv
from cv2 import *
import time
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    imwrite(argv[1],img) #save image
    time.sleep(1)
    print argv[1]
