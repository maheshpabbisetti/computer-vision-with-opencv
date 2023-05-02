import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Define the four source points
    src = np.float32([[0, 0], [frame.shape[1], 0], [frame.shape[1], frame.shape[0]], [0, frame.shape[0]]])

    # Define the four destination points
    dst = np.float32([[100, 100], [frame.shape[1]-100, 100], [frame.shape[1]-100, frame.shape[0]-100], [100, frame.shape[0]-100]])

    # Compute the perspective transformation matrix
    M = cv2.getPerspectiveTransform(src, dst)

    # Apply the perspective transformation to the frame
    warped = cv2.warpPerspective(frame, M, (frame.shape[1], frame.shape[0]))

    # Display the resulting frame
    cv2.imshow('Warped', warped)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
