import cv2
cameraCapture = cv2.VideoCapture(0)
success, frame = cameraCapture.read()
while success and cv2.waitKey(27) == -1:
    output = frame.copy()
    cv2.putText(output, "Atoms", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow('Test', output)
    success, frame = cameraCapture.read()
cv2.destroyAllWindows()
cameraCapture.release()
