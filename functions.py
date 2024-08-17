import flet
from flet import *
from controls import return_control_refrence
from form_helper import FormHelper
import sqlite3
import cv2
import os
import numpy as np
from PIL import Image, ImageDraw 





#Making Images Circular.....
def imageCircular():
    # Open the input image as numpy array, convert to RGB
    img=Image.open("photos/Ashish.png").convert("RGB")
    print(img)
    npImage=np.array(img)
    print(npImage)
    h,w=img.size

    # Create same size alpha layer with circle
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)

    # Convert alpha Image to numpy array
    npAlpha=np.array(alpha)

    # Add alpha layer to RGB
    npImage=np.dstack((npImage,npAlpha))

    # Save with alpha
    Image.fromarray(npImage).save('test/Ashish.png')