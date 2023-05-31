import cv2
import numpy as np
import webcolors

cap = cv2.VideoCapture(0)

_, frame = cap.read()
rows, cols, _ = frame.shape


while True:
    _, frame = cap.read()


    detector_frame = frame[(rows//2 - 100):(rows//2 + 100), (cols//2 - 100):(cols//2 + 100)]
    frame_filtered = cv2.GaussianBlur(frame, (29, 29), 0)
    frame_filtered[(rows//2 - 100):(rows//2 + 100), (cols//2 - 100):(cols//2 + 100)] = detector_frame
    cv2.rectangle(frame_filtered, (cols//2 - 100,rows//2 - 100), (cols//2 + 100,rows//2 + 100), (80, 80, 80), 7)

    b = np.mean(detector_frame[:, :, 0])
    g = np.mean(detector_frame[:, :, 1])
    r = np.mean(detector_frame[:, :, 2])
    

    color = ''
    print(b, g, r)
    if 0<=b<=50 and 0<=g<=50 and 0<=r<=50:
        color = "black"
    elif 200<=b<=255 and 200<=g<=255 and 200<=r<=255:
        color = "white"
    elif 100<=b<=255 and 0<=g<=50 and 0<=r<=50:
        color = "blue"
    elif 0<=b<=70 and 100<=g<=255 and 0<=r<=50:
        color = "green"
    elif 0<=b<=50 and 0<=g<=50 and 100<=r<=255:
        color = "red"
    elif 0<=b<=50 and 100<=g<=255 and 100<=r<=255:
        color = "yellow"
    elif 10<=b<=20 and 100<=g<=255 and 100<=r<=255:
        color = "orange"
    elif 120<=b<=150 and 10<=g<=150 and 10<=r<=150:
        color = "purple"
    

    cv2.putText(frame_filtered, color, (cols//2 - 110,rows//2 - 120), 3, 2, 0)
    cv2.rectangle(frame_filtered, (cols//2 - 100,rows//2 - 100), (cols//2 + 100,rows//2 + 100), 0, 7)
    


    cv2.imshow("", frame_filtered)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
