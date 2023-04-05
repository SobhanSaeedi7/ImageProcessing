import cv2
import numpy as np

gradient = np.zeros((300, 255))

for i in range(255):
    gradient[0:300 , i] = i

cv2.imwrite("outputs\gradient.jpg",gradient)