import cv2

# Read the image
img = cv2.imread("C:/Users/maheshpabbisetti/OneDrive/Pictures/openCV/gray scale conversion image.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel edge detection along the X-axis
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0)

# Scale the result to 0-255 and convert back to uint8
sobel_x = cv2.convertScaleAbs(sobel_x)

# Display the result
cv2.imshow("Sobel Edge Detection (X-axis)", sobel_x)
cv2.waitKey(0)
