import cv2
import numpy as np

cap = cv2.VideoCapture(0)

_, frame = cap.read()
rows, cols, _ = frame.shape


while True:
    _, frame = cap.read()


    detector_frame = frame[(rows//2 - 100):(rows//2 + 100), (cols//2 - 100):(cols//2 + 100)]
    frame_filtered = cv2.GaussianBlur(frame, (29, 29), 0)
    frame_filtered[(rows//2 - 100):(rows//2 + 100), (cols//2 - 100):(cols//2 + 100)] = detector_frame
    cv2.rectangle(frame_filtered, (cols//2 - 100,rows//2 - 100), (cols//2 + 100,rows//2 + 100), (80, 80, 80), 7)

    detector_frame = cv2.cvtColor(detector_frame, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(detector_frame)
    H = np.mean(h)
    S = np.mean(s)
    V = np.mean(v)

    color_n = ''
    color = (0,0,0)
    if V < 115:
        color_n = "black"
        color = (0,0,0)
    elif S < 30 and V > 115:
        color_n = "white"
        color = (255,255,255)
    elif 80 < H < 130 and S > 30 and V > 115:
        color_n = "blue"
        color = (255,0,0)
    elif 35 < H < 80 and S > 30 and V > 115:
        color_n = "green"
        color = (0,255,0)
    elif H < 15 or H > 170 and S > 30 and V > 115:
        color_n = "red"
        color = (0,0,255)
    elif 25 < H  < 35 and S > 30 and V > 115:
        color_n = "yellow"
        color = (0,255,255)
    elif 15 < H < 25 and S > 30 and V > 115:
        color_n = "orange"
        color = (0,128,255)
    elif 130 < H < 170 and S > 30 and V > 115:
        color_n = "purple"
        color = (255,0,255)
    

    cv2.putText(frame_filtered, color_n, (cols//2 - 110,rows//2 - 120), 3, 2, color)
    cv2.rectangle(frame_filtered, (cols//2 - 100,rows//2 - 100), (cols//2 + 100,rows//2 + 100), color, 7)
    


    cv2.imshow("", frame_filtered)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
