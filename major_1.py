import os
import numpy as np
from PIL import Image
im_list = []
def trav():
    try:
        files = os.listdir(".")
        for name in files: 
            if name.endswith(".jpg"):
                im_list.append(name)
    except: 
        print('No Image found in directory')
    
def num_arr_len():
    np_photos = np.zeros([len(im_list), 200, 200, 3])
    return np_photos

def image_numarray_resize():
    try:
        trav()
        np_photos = num_arr_len()
        for i in range(len(im_list)):
            image = Image.open(im_list[i])
            resize = image.resize((200,200))
            np_photo = np.array(resize)
            np_photos[i] = np_photo
        return np_photos
    except:
        print('Unable to convert images into numpy array')

def main():
    numpy_array = image_numarray_resize()
    print(type(numpy_array))
    print('The shape of numpy_array is :', numpy_array.shape)

if __name__ ==  "__main__":
    main()