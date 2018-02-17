# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 11:25:18 2018

@author: ABDURREHMANQAU
"""
import cv2
import matplotlib.pyplot as plt
def main():
    Path="E:\\PY_CV\\standard_test_images\\standard_test_images\\"
    imgPath=Path + "peppers_color.tif"
    img=cv2.imread(imgPath,1)

    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    r,g,b=cv2.split(img)
   # titles=["Original","Red","Green","Blue"]
    #images=[img,r,g,b]
# =============================================================================
#     for i in range(4):
#         plt.subplot(1,4,i+1)
#         plt.title(titles[i])
#         plt.imshow(images[i],cmap="gray")
#     plt.show()
# =============================================================================
    plt.imshow(img,cmap="gray")
    plt.show()

    plt.imshow(r,cmap="Reds")
    plt.show()
    
    plt.imshow(g,cmap="Greens")
    plt.show()
    
    plt.imshow(b,cmap="Blues")
    plt.show()
if __name__=="__main__":    
    main()
