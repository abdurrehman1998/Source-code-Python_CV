# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:38:44 2018

@author: ABDURREHMANQAU
"""
import cv2
import matplotlib.pyplot as plt
def main():
    Path="E:\\PY_CV\\standard_test_images\\standard_test_images\\"
    imgPath1=Path + "peppers_color.tif"
    imgPath2=Path + "mandril_color.tif"
    img1=cv2.imread(imgPath1,1)
    img2=cv2.imread(imgPath2,1)
    
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    plt.subplot(1,2,1)
    plt.imshow(img1)
    
    plt.subplot(1,2,2)
    plt.imshow(img2)
    plt.show()
        
if __name__=="__main__":    
    main()
