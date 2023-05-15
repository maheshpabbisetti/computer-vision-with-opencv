import cv2
import numpy as np

# Load the image
image = cv2.imread("C:/Users/maheshpabbisetti/OneDrive/Pictures/openCV/gray scale conversion image.png")

# Create a Laplacian mask with an extension of diagonal neighbors
kernel = np.array([[0, 1, 1, 1, 0],
                    [1, 2, 2, 2, 1],
                    [1, 2, 4, 2, 1],
                    [1, 2, 2, 2, 1],
                    [0, 1, 1, 1, 0]])

# Apply the Laplacian mask to the image
result = cv2.filter2D(image, -1, kernel)

# Normalize the result
result = result / np.max(result)

# Display the original and sharpened images
cv2.imshow("Original", image)
cv2.imshow("Sharpened", result)

# Wait for a key press
cv2.waitKey(0)

# Close all open windows
cv2.destroyAllWindows()
