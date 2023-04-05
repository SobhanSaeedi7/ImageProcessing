import cv2
import numpy as np


tv = cv2.imread("Inputs\TV.png")
tv = cv2.cvtColor(tv, cv2.COLOR_BGR2GRAY)

rows, cols = tv.shape

writer = cv2.VideoWriter("Outputs\TV_noise.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))

while True:
    tv = cv2.imread("Inputs\TV.png")
    tv = cv2.cvtColor(tv, cv2.COLOR_BGR2GRAY)

    noise = np.random.random((95, 120)) * 255
    noise = np.array(noise, dtype=np.uint8)

    tv[155:250, 535:655] = noise

    cv2.rectangle(tv, (535,250), (655,155), 0, 10)

    tv = cv2.cvtColor(tv, cv2.COLOR_GRAY2BGR)
    writer.write(tv)
    cv2.imshow("", tv)
    if cv2.waitKey(25) & 0xFF==ord("q"):
        break

writer.release()