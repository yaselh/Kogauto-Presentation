import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image, ImageFile, ImageDraw, ImageFont
from skimage import io
from matplotlib import cm
from matplotlib.path import Path
import matplotlib.patches as patches
import tifffile
from os import listdir, makedirs
from os.path import isfile, join
import cv2

# Define your image names in this list; your images will be overwritten with the colorized versions
images = ['gtav_cid0_c258_14614-stencil.tiff', 'gtav_cid0_c258_14740-stencil.tiff', 'gtav_cid0_c258_16053-stencil.tiff']
for img in images:
    #img = Image.open('gtav_cid0_c258_14603-depth.png')
    im = cv2.imread(img,  cv2.IMREAD_UNCHANGED)
    #img=mpimg.imread(('gtav_cid0_c258_14603-depth.png')

    im_color = cv2.applyColorMap(im, cv2.COLORMAP_JET)

    cv2.imwrite(img, im_color)
    # cv2.imshow("Test", im_color)

    # key = cv2.waitKey(0)
    # if key == 27: # escape
    #     cv2.destroyAllWindows()
    #     break
cv2.destroyAllWindows()