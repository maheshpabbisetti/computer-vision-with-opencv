import cv2
import numpy as np

# Load the video file
cap = cv2.VideoCapture("C:/Users/maheshpabbisetti/OneDrive/Pictures/Camera Roll/WIN_20230502_11_01_05_Pro.mp4")

# Get the four corners of the document in the video
pts1 = np.float32([[0, 260], [640, 260], [0, 400], [640, 400]])

# Get the four corners of the destination image
pts2 = np.float32([[0, 0], [400, 0], [0, 640], [400, 640]])

# Get the perspective transform matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Create a blank image the same size as the destination image
dst = np.zeros((400, 640, 3), dtype=np.uint8)

# Apply the perspective transform to the video frame
while True:
    # Read the next frame from the video
    ret, frame = cap.read()

    # If the frame is not read, break the loop
    if not ret:
        break

    # Apply the perspective transform to the frame
    result = cv2.warpPerspective(frame, M, (400, 640))

    # Display the original and transformed frames
    cv2.imshow("Original", frame)
    cv2.imshow("Transformed", result)

    # Wait for a key press
    key = cv2.waitKey(1)

    # If the `q` key is pressed, break the loop
    if key == ord("q"):
        break

# Release the video capture object
cap.release()

# Close all open windows
cv2.destroyAllWindows()
