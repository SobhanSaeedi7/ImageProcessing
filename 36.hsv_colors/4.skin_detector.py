import cv2
import numpy as np

cap = cv2.VideoCapture(0)

_, frame = cap.read()
rows, cols, _ = frame.shape


while True:
    _, frame = cap.read()


    detector_frame = frame[(rows//2 - 150):(rows//2 + 150), (cols//2 - 150):(cols//2 + 150)]
    frame_filtered = cv2.GaussianBlur(frame, (77, 77), 0)
    cv2.rectangle(frame_filtered, (cols//2 - 150,rows//2 - 150), (cols//2 + 150,rows//2 + 150), (80, 80, 80), 7)


    converted_detector_frame = cv2.cvtColor(detector_frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(converted_detector_frame, np.array([0, 48, 80]), np.array([20, 255, 255]))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    mask = cv2.erode(mask, kernel, iterations = 2)
    mask = cv2.dilate(mask, kernel, iterations = 2)
    mask = cv2.GaussianBlur(mask, (3, 3), 0)
    skin = cv2.bitwise_and(detector_frame, detector_frame, mask = mask)


    frame_filtered[(rows//2 - 150):(rows//2 + 150), (cols//2 - 150):(cols//2 + 150)] = skin


    cv2.imshow("", frame_filtered)
    if cv2.waitKey(1) & 0xFF==ord("s"):
        cv2.imwrite('Outputs/skin_detedtion.jpg', frame_filteredqq)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
