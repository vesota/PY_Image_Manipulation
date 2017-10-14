#!/usr/bin/env python

from PIL import Image
import glob
import os


#Ein neues Bild generiert. In dieses Bild werden die Spalten (dw * y) der einzelnen Bilder kopiert. Die Aufloesung muss hier festgelegt werden.
#im_new = Image.new('RGB', (600, 400), None)

resolutionA = (400,600)
resolutionB = (600,400)

list_of_files = glob.glob('*.JPG')
for filename in list_of_files:
        im_old = Image.open(filename)
        width, height = im_old.size
        print(filename, width, height)
        if width < height:
            im_new = im_old.resize(resolutionA, Image.ANTIALIAS)
        else:
            im_new = im_old.resize(resolutionB, Image.ANTIALIAS)
        im_new.save(filename)
print ('End of Program')