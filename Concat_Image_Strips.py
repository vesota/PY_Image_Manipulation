#!/usr/bin/env python

from PIL import Image
import glob
import os

faktor = int(raw_input ('Gib die Anzahl der Bilder ein: ')) # Anzahl der Bilder
w1 = 0 # untere Grenze (in Richtung x) fuer das Bildsegment
dw = 0 # eigentliche (fixe) Breite (dw = w2-w1)
w2 = 0 # obere Grenze (in Richtung x) fuer das Bildsegment

#Ein neues Bild generiert. In dieses Bild werden die Spalten (dw * y) der einzelnen Bilder kopiert. Die Aufloesung muss hier festgelegt werden.
im_new = Image.new('RGB', (3456,2304), None)


list_of_files = glob.glob('*.JPG')
for file_name in list_of_files:
    im = Image.open(file_name)
    width, height = im.size
    height_range = height  #Fuer die For - Schleife fuer y muss der Range angepasst werden
    im_pixel = im.load()
    dw = int(width/faktor)
    w2 = w2 + dw
    for x in range(w1, w2, 1):
        for y in range(height_range): #Angabe des Bereichs in [y]-Richtung
            r, g, b = im.getpixel((x, y))
            R, G, B = r, g, b
            im_new.putpixel( (x, y), (R, G, B))
    w1 = w1 + dw
    print 'dw: ' + str(dw) +' w1: ' + str(w1-dw) + ' w2: ' + str(w2) + '  width: ' + str(width) + ' height: ' + str(height)
##    im_new.show()
    R = 0
    G = 0
    B = 0

if w2 == faktor * dw:
     im_new.save('Concat_Image.jpg')
print 'End of Program'
