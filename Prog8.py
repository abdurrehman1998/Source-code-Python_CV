# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:27:52 2018

@author: ABDURREHMANQAU
"""

import cv2
import matplotlib.pyplot as plt

def main():
    imgPath="E:\PY_CV\standard_test_images\standard_test_images\peppers_color.tif"
    img=cv2.imread(imgPath,1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title("Color_Image")
    plt.xticks([])
    plt.yticks([])
    plt.show()

    
if __name__=="__main__":    
    main()
