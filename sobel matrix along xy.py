import cv2

# Read the image
img = cv2.imread("C:/Users/maheshpabbisetti/OneDrive/Pictures/openCV/gray scale conversion image.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel edge detection along the X and Y axes
sobel_xy = cv2.Sobel(gray, cv2.CV_64F, 1, 1)

# Scale the result to 0-255 and convert back to uint8
sobel_xy = cv2.convertScaleAbs(sobel_xy)

# Display the result
cv2.imshow("Sobel Edge Detection (X and Y axes)", sobel_xy)
cv2.waitKey(0)
