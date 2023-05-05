import cv2
import numpy as np

img1 = cv2.imread("Inputs/xray_noisy.png", 0)
img2 = cv2.imread("Inputs/board_noisy.png", 0)
img3 = cv2.imread("Inputs/image_noisy.png", 0)
img4 = cv2.imread("Inputs/balloons_noisy.png")
img5 = cv2.imread("Inputs/Medianfilterp.png", 0)
img6 = cv2.imread("Inputs/5.png", 0)


result1 = cv2.medianBlur(img1, 3)
result2 = cv2.medianBlur(img2, 5)
result3 = cv2.medianBlur(img3, 5)
result4 = cv2.medianBlur(img4, 5)
result5 = cv2.medianBlur(img5, 7)
result6 = cv2.medianBlur(img6, 7)


cv2.imwrite('Outputs/median_filters/median_filter1.jpg', result1)
cv2.imwrite('Outputs/median_filters/median_filter2.jpg', result2)
cv2.imwrite('Outputs/median_filters/median_filter3.jpg', result3)
cv2.imwrite('Outputs/median_filters/median_filter4.jpg', result4)
cv2.imwrite('Outputs/median_filters/median_filter5.jpg', result5)
cv2.imwrite('Outputs/median_filters/median_filter6.jpg', result6)
