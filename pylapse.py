#!/usr/bin/env python

import pygame
import pygame.camera
import pygame.image
import threading
import sys
import getopt
from pygame.locals import *

def main(argv):

    help = 'timelapse.py -t <lapsetime> -p <path>'
    try:
        opts, args = getopt.getopt(argv,"ht:p:", ["lapsetime=","path="])
    except getopt.GetoptError:
        print help
        sys.exit(2)

    lapsetime = ''
    path      = ''

    for opt, arg in opts:
      if opt == '-h':
        print help
        sys.exit()
      elif opt in ("-t", "--lapsetime"):
        lapsetime = float(arg)
      elif opt in ("-p", "--path"):
        path = arg

    if (lapsetime == '' or path == ''):
      print help
      sys.exit()

    pygame.init()
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()
    if camlist:
        cam = pygame.camera.Camera(camlist[0])
        cam.start()

        t = threading.Timer(lapsetime, takePicture, [lapsetime, cam, path, 1])
        t.start()
        

def takePicture(lapsetime, cam, path, index):
    pygame.image.save(cam.get_image(), path+'/img_'+`index`+'.jpg')
    index += 1
    t = threading.Timer(lapsetime, takePicture, [lapsetime, cam, path, index])
    t.start()

if __name__ == "__main__":
   main(sys.argv[1:])