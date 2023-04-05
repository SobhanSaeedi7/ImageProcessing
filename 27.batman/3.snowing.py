import cv2
import numpy as np
import random

area = cv2.imread("Inputs\snowy_area.png")
area = cv2.cvtColor(area, cv2.COLOR_BGR2GRAY)

rows, cols = area.shape

writer = cv2.VideoWriter("Outputs\snowing.mp4", cv2.VideoWriter_fourcc(*'XVID'), 10, (cols, rows))


while True:
    snowy_area = cv2.imread("Inputs\snowy_area.png")
    snowy_area = cv2.cvtColor(snowy_area, cv2.COLOR_BGR2GRAY)

    x = np.random.randint(0, rows, rows)
    y = np.random.randint(0, cols, cols)

    for i in range(len(x)):
        cv2.circle(snowy_area, (x[i], y[i]), 1, 255, -1)

    snowy_area = cv2.cvtColor(snowy_area, cv2.COLOR_GRAY2BGR)
    writer.write(snowy_area)
    cv2.imshow("", snowy_area)
    if cv2.waitKey(60) & 0xFF==ord("q"):
        break

writer.release()