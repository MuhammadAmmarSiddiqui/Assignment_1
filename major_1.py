import os
import numpy as np
from PIL import Image
files = os.listdir(".")
im_list = []
np_photos = np.zeros([20, 200, 200, 3])
for name in files:
    if name.endswith(".jpg"):
        im_list.append(name)
for i in range(len(im_list)):
    a = Image.open(im_list[i])
    rs = a.resize((200,200))
    cv_pic = np.array(rs)
    np_photos[i] = cv_pic
print(type(np_photos))
print(np_photos.shape)
print(np_photos[:20, :10, :10, :3])
