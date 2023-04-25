import numpy as np
import cv2

home = cv2.imread("Inputs\home.jpg")
floor = cv2.imread("Inputs/floor.jpg")
mask = cv2.imread("Inputs\mask2.jpg")


mask = mask / 255

new_floor = floor * mask
old_floor = home * (1-mask)

new_home = new_floor + old_floor


cv2.imwrite("Output/changed_floor.jpg", new_home)