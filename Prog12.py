# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 09:21:42 2018

@author: ABDURREHMANQAU
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import time as t
def main():
    Path="E:\\PY_CV\\standard_test_images\\standard_test_images\\"
    imgPath1=Path + "peppers_color.tif"
    imgPath2=Path + "mandril_color.tif"
    img1=cv2.imread(imgPath1,1)
    img2=cv2.imread(imgPath2,1)
    
    img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
# =============================================================================
#     
#     aplha=0.65
#     beta=0.35
#     gamma=0.0
# =============================================================================
# =============================================================================
#     alpha=0.0
#     beta=1.0
#     gamma=0.0
# 
#     titles=["img1","img2","weighted addtion"]
#     for j in range(10):
#         for i in range(3):
#             output=cv2.addWeighted(img1,alpha,img2,beta,gamma)
#             images=[img1,img2,output]
#             plt.subplot(1,3,i+1)
#             plt.title(titles[i])
#             plt.imshow(images[i])
#             
#         plt.show()
#         alpha+=0.1
#         beta-=0.1
# =============================================================================
    for i in np.linspace(0,1,100): #smooothness control
        alpha=i
        beta=1-i
        gamma=0
        output=cv2.addWeighted(img1,alpha,img2,beta,gamma)
        cv2.imshow("Transition",output)
        t.sleep(0.1) # transition time control
        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()
        
if __name__=="__main__":    
    main()
