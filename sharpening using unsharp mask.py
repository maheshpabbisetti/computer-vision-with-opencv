


import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/maheshpabbisetti/OneDrive/Pictures/openCV/gray scale conversion image.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform unsharp masking
sharpened = cv2.addWeighted(gray, 1.5, blurred, -0.5, 0)

# Convert the sharpened image back to BGR color space
sharpened = cv2.cvtColor(sharpened, cv2.COLOR_GRAY2BGR)

# Display the result
cv2.imshow('Original', img)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

