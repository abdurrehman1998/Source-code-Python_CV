# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import cv2
def main():
    imgPath="E:\PY_CV\standard_test_images\standard_test_images\peppers_color.tif"
    img=cv2.imread(imgPath)
    cv2.namedWindow("Pepper",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Pepper",img)
    cv2.waitKey(0)
    cv2.destroyWindow("Pepper")
    
if __name__=="__main__":    
    main()