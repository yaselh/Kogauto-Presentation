import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image, ImageFile, ImageDraw, ImageFont
from skimage import io
from matplotlib.pylab import cm
from matplotlib.path import Path
import matplotlib.patches as patches
import tifffile
from os import listdir, makedirs
from os.path import isfile, join
import cv2
from scipy.interpolate import interp1d

def get_random_reas():
    w=5
    reas=interp1d(range(w+1),np.cumsum([np.random.normal() for x in range(w+1)]),'cubic')(np.arange(0,w,w/256.))
    reas-=np.min(reas)
    reas/=np.max(reas)
    reas*=255.
    return list(map(int,reas))

def applyCustomColorMap(im_gray) :
    lut = np.zeros((256, 1, 3), dtype=np.uint8)

    lut[:, 0, 0] = get_random_reas()
    lut[:, 0, 1] = get_random_reas()
    lut[:, 0, 2] = get_random_reas()

    im_color = cv2.LUT(im_gray, lut)

    return im_color

def colorize(image, colormap):
    im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    colorized = colormap(im)
    return colorized

# Define your image names in this list; your images will be overwritten with the colorized versions
images = ['gt_conv.png', 'gt_lidar.png', 'pre.png']
for img in images:
    #img = Image.open('gtav_cid0_c258_14603-depth.png')
    im = cv2.imread(img,  cv2.IMREAD_UNCHANGED)
    #im=mpimg.imread(img)
    print(im.shape)

    #im_color = cv2.applyColorMap(im, cv2.COLORMAP_HSV)
    im_color = cv2.applyColorMap(im[:,:,:3], cv2.COLORMAP_JET)
    #im_color = applyCustomColorMap(im)
    #im_color = colorize(im, cm.gist_ncar)

    cv2.imwrite(img, im_color)
    # cv2.imshow("Test", im_color)

    # key = cv2.waitKey(0)
    # if key == 27: # escape
    #     cv2.destroyAllWindows()
    #     break
cv2.destroyAllWindows()