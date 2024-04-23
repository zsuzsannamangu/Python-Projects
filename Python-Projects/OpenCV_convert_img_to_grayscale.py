#Load an image using OpenCV in Python and convert it to grayscale

import cv2

# Load the image (replace 'path_to_image.jpg' with the actual path to your image)
image = cv2.imread('/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/OpenCV_convert_img_to_grayscale/rose_yellow.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and grayscale images (optional)
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
