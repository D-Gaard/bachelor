#plot greyscale histogram for all images:
import cv2
from glob import glob
import os
import numpy as np

#path for all greyscale images
path_to_grey_img = r"C:\Users\Mads Syge Monster PC\Desktop\pythonDUmp\greyscale"
path_to_grey_seg = r"C:\Users\Mads Syge Monster PC\Desktop\pythonDUmp\greyscale_out"

images = sorted(glob(os.path.join(path_to_grey_img, "IMG*.tiff")))
segs = sorted(glob(os.path.join(path_to_grey_seg, "I0*.tiff")))

#create histogram of image:
def Create_Hist(img_path):
  grey = cv2.imread(img_path,0)
  temp_hist , b = np.histogram(grey, bins=256,range=(0.0,255.0))
  #print(np.count_nonzero(grey == 254))
  return(temp_hist)

#loop all images and add histogram
total_hist = [0 for i in range(256)]

for i in range(len(images)):
  temp_hist = images[i]
  total_hist = np.add(temp_hist,total_hist)




