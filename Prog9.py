# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:52:41 2018

@author: ABDURREHMANQAU
"""

import cv2
def main():
    j=0
    for filename in dir(cv2):
        if filename.startswith('COLOR_'):
            print(filename)
            j=j+1
    print("There are" +str(j)+ "Color_Spaces")
    
if __name__=="__main__":    
    main()