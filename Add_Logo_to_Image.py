from PIL import Image
import glob
import os


#Ein neues Bild generiert. In dieses Bild werden die Spalten (dw * y) der einzelnen Bilder kopiert. Die Aufloesung muss hier festgelegt werden.
#im_new = Image.new('RGB', (600, 400), None)



#Resize Logo:
LOGO_FILENAME = 'tatort.jpg'
resolutionLogo = (120,60)
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

logoIm = logoIm.resize(resolutionLogo, Image.ANTIALIAS)
logoIm.save(LOGO_FILENAME)


list_of_files = glob.glob('*.JPG')
for filename in list_of_files:
        im_old = Image.open(filename)
        width, height = im_old.size
        im_old.paste(logoIm, (0, 0, logoWidth, logoHeight ))
        print(filename, width, height)
        im_old.save(filename)



