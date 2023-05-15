import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/maheshpabbisetti/OneDrive/Pictures/openCV/gray scale conversion image.png")

# Create the high-boost mask
kernel = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])

# Apply the high-boost mask to the image
sharpened_image = cv2.filter2D(image, -1, kernel)

# Display the sharpened image
cv2.imshow("Sharpened Image", sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
