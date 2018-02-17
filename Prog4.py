# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:39:12 2018

@author: ABDURREHMANQAU
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import cv2
def main():
    imgPath="E:\PY_CV\standard_test_images\standard_test_images\peppers_color.tif"
    outPath="E:\PY_CV\Output\peppers_color.jpg"
    img=cv2.imread(imgPath,1)
    cv2.namedWindow("Pepper",cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Pepper",img)
    cv2.imwrite(outPath,img)
    cv2.waitKey(0)
    cv2.destroyWindow("Pepper")
    
    
if __name__=="__main__":    
    main()