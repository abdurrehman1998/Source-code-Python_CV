# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:03:57 2018

@author: ABDURREHMANQAU
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import cv2
def main():
    imgPath="E:\PY_CV\standard_test_images\standard_test_images\peppers_color.tif"
    img=cv2.imread(imgPath,0)
    #cv2.namedWindow("Pepper",cv2.WINDOW_AUTOSIZE)
    #cv2.imshow("Pepper",img)
    print(type(img))
    print(img.dtype)
    print(img.shape)
    print(img.ndim)
    print(img.size)
    #cv2.waitKey(0)
    #cv2.destroyWindow("Pepper")
    
    
if __name__=="__main__":    
    main()