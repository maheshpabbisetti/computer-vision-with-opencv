import cv2

# Read the image
img = cv2.imread("C:/Users/maheshpabbisetti/OneDrive/Pictures/openCV/gray scale conversion image.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel edge detection along the Y-axis
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

# Scale the result to 0-255 and convert back to uint8
sobel_y = cv2.convertScaleAbs(sobel_y)

# Display the result
cv2.imshow("Sobel Edge Detection (Y-axis)", sobel_y)
cv2.waitKey(0)
