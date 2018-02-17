# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 09:48:16 2018

@author: ABDURREHMANQAU
"""

import cv2
import matplotlib.pyplot as plt

def main():
    imgPath="E:\PY_CV\standard_test_images\standard_test_images\peppers_color.tif"
    img=cv2.imread(imgPath,0)
    plt.imshow(img,cmap="gray")
    plt.title("Grayscale")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    plt.imshow(img,cmap="Reds")
    plt.title("Redscale")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
if __name__=="__main__":    
    main()