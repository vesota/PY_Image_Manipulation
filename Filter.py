from PIL import Image, ImageFilter
im = Image.open('kopie.JPG')
##im = im.filter(ImageFilter.CONTOUR)
##im = im.filter(ImageFilter.BLUR)
##im = im.filter(ImageFilter.DETAIL)
##im = im.filter(ImageFilter.EDGE_ENHANCE)
##im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
##im = im.filter(ImageFilter.EMBOSS)
##im = im.filter(ImageFilter.FIND_EDGES)
##im = im.filter(ImageFilter.SMOOTH)
##im = im.filter(ImageFilter.SMOOTH_MORE)
##im = im.filter(ImageFilter.SHARPEN)

im.show('kopie.JPG')

