import cv2
import numpy as np

def bgr_2_grayscale(img):
    B = img[:, :, 0]
    G = img[:, :, 1]
    R = img[:, :, 2]
    result = (B + G + R) / 3
    return result

img = cv2.imread("inputs\python.jpg")
img = bgr_2_grayscale(img)
cv2.imwrite("outputs/test.png", img)

