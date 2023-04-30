import cv2
import numpy as np


img = cv2.imread("Inputs/noisy_img.png", cv2.IMREAD_GRAYSCALE)
board = cv2.imread("Inputs/board.png", cv2.IMREAD_GRAYSCALE)
x_ray = cv2.imread("Inputs/x_ray.png", cv2.IMREAD_GRAYSCALE)


i_rows, i_cols = img.shape
b_rows, b_cols = board.shape
x_rows, x_cols = x_ray.shape


i_result = np.zeros((i_rows, i_cols), dtype=np.uint8)
b_result = np.zeros((b_rows, b_cols), dtype=np.uint8)
x_result = np.zeros((x_rows, x_cols), dtype=np.uint8)



for i in range(1, i_rows-1):
    for j in range(1, i_cols-1):
        small = img[i-1:i+2 , j-1:j+2]
        avg = np.mean(small)
        i_result[i, j] = avg

for i in range(1, b_rows-1):
    for j in range(1, b_cols-1):
        small = board[i-1:i+2 , j-1:j+2]
        avg = np.mean(small)
        b_result[i, j] = avg

for i in range(1, x_rows-1):
    for j in range(1, x_cols-1):
        small = x_ray[i-1:i+2 , j-1:j+2]
        avg = np.mean(small)
        x_result[i, j] = avg


cv2.imwrite("Output/..image.jpg", i_result)
cv2.imwrite("Output/board.jpg", b_result)
cv2.imwrite("Output/x_ray.jpg", x_result)

