import cv2
cap = cv2.VideoCapture("C:/Users/maheshpabbisetti/OneDrive/Pictures/Camera Roll/WIN_20230502_11_01_05_Pro.mp4")
if not cap.isOpened():
    print("Error opening video file")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
