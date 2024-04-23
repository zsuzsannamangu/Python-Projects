#Load an image using OpenCV in Python and convert it to grayscale

import cv2

# Load the image using the imread function
image = cv2.imread('/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/OpenCV_convert_img_to_grayscale/rose_yellow.jpg')

# Convert the image to grayscale using the cvtColor() function
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and grayscale images (optional)
cv2.imshow('Original Image', image) #display original image
cv2.imshow('Grayscale Image', gray_image) #display grayscale image
cv2.waitKey(0) #to wait for a key press
cv2.destroyAllWindows() #and close the image windows.