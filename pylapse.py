#!/usr/bin/env python

import pygame
import pygame.camera
import pygame.image
import sys
import getopt
import time
from pygame.locals import *

def main(argv):

    help = 'timelapse.py -t <lapsetime> -p <path> -d <dimensions>'
    try:
        opts, args = getopt.getopt(argv,"hd:t:p:", ["dimensions=","lapsetime=","path="])
    except getopt.GetoptError:
        print help
        sys.exit(2)

    lapsetime  = ''
    path       = ''
    dimensions = (640,480)

    for opt, arg in opts:
      if opt == '-h':
        print help
        sys.exit()
      elif opt in ("-t", "--lapsetime"):
        lapsetime = float(arg)
      elif opt in ("-p", "--path"):
        path = arg
      elif opt in ("-d", "--dimensions"):
        if arg.find('x') == False:
            print "Dimensions must be in the format <width>x<height> (i.e. 640x480)"
            sys.exit(2)

        dimensions    = arg.split('x')
        dimensions[0] = int(dimensions[0])
        dimensions[1] = int(dimensions[1])

    if (lapsetime == '' or path == ''):
      print help
      sys.exit()

    pygame.init()
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()
    if camlist:
        cam = pygame.camera.Camera(camlist[0], dimensions)
        cam.start()

        index = 1
        while True:
            try:
                pygame.image.save(cam.get_image(), path+'/img_'+`index`+'.jpg')
                index += 1
                time.sleep(lapsetime)
            except KeyboardInterrupt:
                print "Exiting."
                cam.stop()
                sys.exit();
    else:
        raise Exception("No cameras found!")

if __name__ == "__main__":
   main(sys.argv[1:])