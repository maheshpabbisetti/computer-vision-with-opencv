import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/maheshpabbisetti/OneDrive/Pictures/Saved Pictures/Naruto Wallpaper iPhone 4.png")

# Define the corners of the target area (the area you want to transform the image to)
target_corners = np.array([[0, 0], [img.shape[1]-1, 0], [img.shape[1]-1, img.shape[0]-1], [0, img.shape[0]-1]])

# Define the corners of the source area (the area you want to transform from)
source_corners = np.array([[100, 100], [img.shape[1]-200, 200], [img.shape[1]-100, img.shape[0]-200], [200, img.shape[0]-100]])

# Compute the homography matrix
homography, _ = cv2.findHomography(source_corners, target_corners)

# Apply the homography transformation
output_img = cv2.warpPerspective(img, homography, (img.shape[1], img.shape[0]))

# Display the output image
cv2.imshow("Output Image", output_img)
cv2.waitKey(0)
