import cv2
cap = cv2.VideoCapture("C:/Users/maheshpabbisetti/OneDrive/Pictures/Camera Roll/WIN_20230502_11_01_05_Pro.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Processed Frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
