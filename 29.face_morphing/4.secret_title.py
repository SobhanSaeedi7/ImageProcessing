import cv2
import numpy as np

title = cv2.imread("Inputs/title.jpg")
mask = cv2.imread("Inputs\mask.jpg")

secret = 255 - mask + title

cv2.imwrite("Outputs\secret.jpg", secret)
