import os
import numpy as np
from PIL import Image
files = os.listdir(".")
im_list = []
im = []
#im = np.zeros([20, 500, 500, 3])
for name in files:
    if name.endswith(".jpg"):
        im_list.append(name)
for i in range(len(im_list)):
    a = np.array(Image.open(im_list[i]))
    im.append(a)
    
print(type(im))
images = np.array(im)
print(type(images))
print(images.shape)
