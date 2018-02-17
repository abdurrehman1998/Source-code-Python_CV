import cv2
import numpy as np

filename = 'Stripe-Rust.jpg'
img = cv2.imread(filename)
yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
boundaries = [
	([0, 0, 0], [255, 0, 255]),
	
]
# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(yuv, lower, upper)
	output = cv2.bitwise_and(yuv, yuv, mask = mask)
cv2.startWindowThread()
cv2.namedWindow("Allah")
cv2.imshow('Allah',yuv)
cv2.waitKey(0)
cv2.destroyAllWindows()

