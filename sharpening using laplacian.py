import cv2
import numpy as np

# Read the image
img = cv2.imread("C:/Users/maheshpabbisetti/OneDrive/Pictures/openCV/gray scale conversion image.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define the Laplacian kernel with negative center coefficient
laplacian_kernel = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]])

# Apply the Laplacian kernel to the grayscale image
laplacian = cv2.filter2D(gray, -1, laplacian_kernel)

# Add the Laplacian image to the original grayscale image
sharpened = cv2.add(gray, laplacian)

# Display the result
cv2.imshow("Sharpened Image", sharpened)
cv2.waitKey(0)
