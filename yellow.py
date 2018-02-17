import cv2
import numpy as np
    
img = cv2.imread('S4.jpg')
# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# define range of yellow color in HSV
lower_yellow = np.array([20,100,100])
upper_yellow = np.array([30,255,255])
# Threshold the HSV image to get only yellow colors
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
cv2.imshow('frame',img)
cv2.imshow('mask',mask)
cv2.waitKey(0)