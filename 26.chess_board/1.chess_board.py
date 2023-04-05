import numpy as np
import cv2

size = 800
chess_board = np.empty((size, size))

row = 0
col = 0


for i in range(int(size/8), size+1, int(size/8)):
    row += 1 
    for j in range(int(size/8), size+1, int(size/8)):
        col += 1
        if row%2 == 1:
            if col%2 == 1:
                chess_board[j-int(size/8):j, i - int(size/8):i] = 255
            else:
                chess_board[j-int(size/8):j, i - int(size/8):i] = 0
        else:
            if col%2 == 1:
                chess_board[j-int(size/8):j, i - int(size/8):i] = 0
            else:
                chess_board[j-int(size/8):j, i - int(size/8):i] = 255


cv2.imwrite("outputs\chess_board.jpg", chess_board)