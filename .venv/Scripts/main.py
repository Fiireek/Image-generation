from random import randint
import keyboard
from PIL import ImageChops
from PIL import Image
import Keyboard
# Width and heigth of the image
height = 1028
width = 1028
# Color ranges
red_min = 0 #max value 24
red_max = 255 #min value 101
blue_min = 0 #max value 24
blue_max = 255 #min value 101
green_min = 0 #max value 24
green_max =255 #min value 101
#creates the image
im = Image.new(mode = "RGB", size =(height, width))
inv_im = im #later used for invertion of colors
# Coloring and recoloring the image
def recolor():
    pixels = im.getdata()
    new_pixels = []
    i=0 #for mixing the land and the sky
    for item in pixels:
        if i<=(0.5*(height*width)):
            new_pixels.append((randint(red_min, 25), randint(100, blue_max), randint(green_min, 25)))
        elif i<=(0.9*(height*width)):
            new_pixels.append((randint(red_min, 25), randint(blue_min, 25), randint(100, green_max)))
        else:
            new_pixels.append(randint(50, 100), 0, randint(25, 60))
# Invertion
def invert():
    inv_im = ImageChops.invert(im)
# Calling functions
recolor()
invert()
while True:
    try:
        if keyboard.is_pressed('t'):
            im.show()
            break
        elif keyboard.is_pressed('i'):
            inv_im.show()
            break
    except:
        pass