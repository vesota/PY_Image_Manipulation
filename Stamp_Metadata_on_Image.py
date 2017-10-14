
from PIL import Image, ImageDraw, ImageFont
import glob
import os
from PIL.ExifTags import TAGS

#SQUARE_FIT_SIZE = 300
#LOGO_FILENAME = 'logo.jpg'

#logoIm = Image.open(LOGO_FILENAME)
#logoWidth, logoHeight = logoIm.size

extra_text = 'JOKER'
fontsFolder = 'C:\Windows\Fonts'
arialFont28 = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 28)
arialFont44 = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 44)

os.makedirs('withLogo',exist_ok=True)

list_of_files = glob.glob('*.JPG')
for filename in list_of_files:
    ret = {}
    im = Image.open(filename)
    exif_data = im._getexif()
    #string_exif_data = str(exif_data)
    #print(string_exif_data)
    for tag, value in exif_data.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
        
    #draw = ImageDraw.Draw(im)
   # draw.text((130, 5), 'MEMORY', fill='red', font=arialFont44)
    #filename_str = str(filename)   
    #name_wo_ending = filename_str.replace('.jpg', '')
   # x = name_wo_ending.find('Joker')
   # if x != -1:
  #      name_wo_ending = name_wo_ending.replace('Joker', '')
  #      draw.text((20, 500), extra_text, fill='yellow', font=arialFont28)
 #   print (name_wo_ending)
  #  draw.text((130, 40), name_wo_ending, fill='blue', font=arialFont28)
    
  #  im.save(filename)
    
    
    
   # if not (filename.end_string('.png') or filename.end_string('.jpg')) or filename == LOGO_FILENAME:
   #     continue
        
   # im = Image.open(filename)       
   # width, height = im.size