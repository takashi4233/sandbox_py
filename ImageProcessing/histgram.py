from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def color_hist(filename):
    img = np.asarray(Image.open(filename).convert("RGB")).reshape(-1,3)
    plt.hist(img,color=["red","green","blue"],bins=128)
    plt.show()


def color_gray_hist(filename):
    img = np.asarray(Image.open(filename).convert("L")).reshape(-1,1)
    plt.hist(img,bins=128)
    plt.show()

def from_color_to_gray(src,dest):
    img = Image.open(src)
    new_img = img.convert('L')
    #new_img.show()
    new_img.save(dest,quality=95)

    

#color_hist("sample/sample.jpg")
#color_gray_hist("sample/sample.jpg")
from_color_to_gray("sample/sample.jpg","sample/sample_gray.jpg")
