import cv2
import numpy as np


first_img = cv2.imread('Inputs\lion_pic.jpg')
second_img = cv2.imread('Inputs\my_pic.png')

w, h, _ = first_img.shape
second_img = cv2.resize(second_img, [h, w])

second_img = second_img.astype(np.float32)
first_img = first_img.astype(np.float32)

img_result1 = second_img*.25 + first_img*.75
img_result2 = second_img*.5 + first_img*.5
img_result3 = second_img*.75 + first_img*.25

img_result1 = img_result1.astype(np.uint8)
img_result2 = img_result2.astype(np.uint8)
img_result3 = img_result3.astype(np.uint8)

img_result = np.concatenate((first_img, img_result1, img_result2,
 img_result3, second_img), axis=1)

cv2.imwrite('Outputs\morphing.jpg',img_result)