import cv2
import numpy as np

cap = cv2.VideoCapture(0)

_, frame = cap.read()
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

rows, cols = frame.shape
writer = cv2.VideoWriter("Outputs\webcam.mp4", cv2.VideoWriter_fourcc(*'XVID'), 2.5, (cols, rows))

while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detector_frame = frame[(rows//2 - 70):(rows//2 + 70), (cols//2 - 70):(cols//2 + 70)]
    frame_filtered = cv2.fastNlMeansDenoising(frame, None, 200, 10, 10 )  
    cv2.rectangle(frame_filtered, (cols//2 - 70,rows//2 - 70), (cols//2 + 70,rows//2 + 70), 100, 10)

    mean = np.mean(detector_frame)
    if mean > 150:
        color = 'White'
    elif mean < 80:
        color = 'Black'
    else:
        color = 'Gray'

    
    cv2.putText(frame_filtered, color, (cols//2 - 110,rows//2 - 120), 3, 2, 0)

    frame_filtered[(rows//2 - 70):(rows//2 + 70), (cols//2 - 70):(cols//2 + 70)] = detector_frame
    frame = cv2.cvtColor(frame_filtered, cv2.COLOR_GRAY2BGR)

    writer.write(frame)
    cv2.imshow("", frame)
    if cv2.waitKey(60) & 0xFF==ord("q"):
        break

writer.release()
cap.release()
cv2.destroyAllWindows()