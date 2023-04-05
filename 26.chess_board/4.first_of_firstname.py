import numpy as np
import cv2

s = np.zeros((700, 500))

for i in range(700):
    for j in range(500):
        s[i, j] = 255

s[0:100, 100:400] = 0
s[100:300, 0:100] = 0
s[100:250, 400:500] = 0
s[300:400, 100:400] = 0
s[400:600, 400:500] = 0
s[600:700, 100:400] = 0
s[450:600, 0:100] = 0


cv2.imwrite("outputs\S.jpg", s)