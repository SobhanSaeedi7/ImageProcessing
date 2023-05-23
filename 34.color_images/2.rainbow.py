import cv2
import numpy as np


img = cv2.imread('inputs/sky.jpg')

img = cv2.resize(img, (1000, 600))
result = cv2.resize(img, (1000, 600))


cv2.circle(result, (500,600), 500, (0,0,255), -1)
cv2.circle(result, (500,600), 470, (0,127,255), -1)
cv2.circle(result, (500,600), 440, (0,255,255), -1)
cv2.circle(result, (500,600), 410, (0,255,0), -1)
cv2.circle(result, (500,600), 380, (255,0,0), -1)
cv2.circle(result, (500,600), 350, (255,0,127), -1)
cv2.circle(result, (500,600), 320, (255,0,255), -1)
cv2.circle(result, (500,600), 290, (255,255,255), -1)

test = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if test[i, j] == 255:
            result[i,j] = img[i, j]


cv2.imwrite('outputs/rainbow.jpg', result)