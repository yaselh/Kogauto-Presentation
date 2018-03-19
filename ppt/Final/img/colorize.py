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

images2 = ['000003_1_mirrored.png', '000008_1.png', '000008_2.png', 'gtav_cid0_c258_14614-depth.png', 'gtav_cid0_c258_14740-depth.png', 'gtav_cid0_c258_16053-depth.png']
images = ['gtav_cid0_c258_14614-stencil.tiff', 'gtav_cid0_c258_14740-stencil.tiff', 'gtav_cid0_c258_16053-stencil.tiff']
for img in images:
    #img = Image.open('gtav_cid0_c258_14603-depth.png')
    im = cv2.imread(img,  cv2.IMREAD_UNCHANGED)
    #img=mpimg.imread(('gtav_cid0_c258_14603-depth.png')
    print(np.unique(im))
    im[np.logical_or(im>2, im<2)] = 0
    # Copy the thresholded image.
    im_floodfill = im.copy()
    
    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels larger than the image.
    h, w = im.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    
    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0,0), 255)
    
    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    
    # Combine the two images to get the foreground.
    im_out = im | im_floodfill_inv

    im_color = cv2.applyColorMap(im_out, cv2.COLORMAP_JET)

    cv2.imwrite(img, im_color)
    # cv2.imshow("Test", im_color)

    # key = cv2.waitKey(0)
    # if key == 27: # escape
    #     cv2.destroyAllWindows()
    #     break
cv2.destroyAllWindows()