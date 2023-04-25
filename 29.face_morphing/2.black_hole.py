import os
import cv2
import numpy as np 


folders_path = os.listdir("Inputs/Black_hole")

parts = []
for folder_path in folders_path:
    imgs_path = os.listdir("Inputs/Black_hole/" + folder_path)
    imgs = []
    for img_path in imgs_path:
        img = cv2.imread("Inputs/Black_hole/" + folder_path + "/" + img_path).astype(np.float32)
        imgs.append(img)
    parts.append(imgs)


img_parts = []
for part in parts:
    result = np.zeros(img.shape)
    for img in part:
        result += img
    result = result / len(part)
    result.astype(np.uint8)
    img_parts.append(result)

ul = img_parts[0]
ur = img_parts[1]
dl = img_parts[2]
dr = img_parts[3]

up = np.concatenate((ul, ur), axis=1)
down = np.concatenate((dl, dr), axis=1)

black_hole = np.concatenate((up, down), axis=0)


cv2.imwrite("Outputs/black_hole.jpg", black_hole)
