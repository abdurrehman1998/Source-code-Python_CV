# import the necessary packages
import numpy as np
import cv2
# load the image
image = cv2.imread('Stripe-Rust.jpg')
# define the list of boundaries
boundaries = [
	([0, 0, 0], [255, 0, 0]),
	
]
# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)