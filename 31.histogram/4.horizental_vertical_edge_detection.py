import cv2
import numpy as np


home = cv2.imread("Inputs\home.png", cv2.IMREAD_GRAYSCALE)

rows, cols = home.shape

h_result = np.zeros((rows, cols), dtype=np.uint8)
v_result = np.zeros((rows, cols), dtype=np.uint8)

h_kernel = np.array([[-1, -1, -1],
                     [ 0,  0,  0],
                     [ 1,  1,  1]])


v_kernel = np.array([[2 ,0, -2],
                     [2, 0, -2],
                     [2, 0 ,-2]])


for i in range(1, rows-1):
    for j in range(1, cols-1):
        small = home[i-1:i+2 , j-1:j+2]
        h_avg = np.abs(np.sum(h_kernel * small))
        v_avg = np.abs(np.sum(v_kernel * small))
        h_result[i, j] = h_avg
        v_result[i, j] = v_avg


cv2.imwrite("Output/horizental_edge.jpg", h_result)
cv2.imwrite("Output/vertical_edge.jpg", v_result)