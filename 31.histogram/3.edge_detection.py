import cv2
import numpy as np


lion = cv2.imread("Inputs\lion.png", cv2.IMREAD_GRAYSCALE)
spider = cv2.imread("Inputs\spider.png", cv2.IMREAD_GRAYSCALE)


l_rows, l_cols = lion.shape
s_rows, s_cols = spider.shape

l_result = np.zeros((l_rows, l_cols), dtype=np.uint8)
s_result = np.zeros((s_rows, s_cols), dtype=np.uint8)


kernel = np.array([[-1, -1, -1],
                     [-1,  8, -1],
                     [-1, -1, -1]])

for i in range(1, l_rows-1):
    for j in range(1, l_cols-1):
        small = lion[i-1:i+2 , j-1:j+2]
        avg = np.sum(kernel * small)
        l_result[i, j] = avg

for i in range(1, s_rows-1):
    for j in range(1, s_cols-1):
        small = spider[i-1:i+2 , j-1:j+2]
        avg = np.abs(np.sum(kernel * small))
        s_result[i, j] = avg


cv2.imwrite("Output/lion_edge.jpg", l_result)
cv2.imwrite("Output/spider_edge.jpg", s_result)