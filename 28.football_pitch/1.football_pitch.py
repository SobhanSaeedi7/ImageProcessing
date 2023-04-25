import cv2
import numpy as np

width = 500
lenght = 1000
pitch = np.zeros((width, lenght, 3), np.uint8)
turn = 0
radius = 0
color = (0,180,0)


for i in range(560):
    radius += 1
    turn += 1
    cv2.circle(pitch, (lenght//2, width//2), radius, color, 2)
    if turn == 50:
        turn = 0
        if color == (0,180,0):
            color = (0,100,0)
        else:
            color = (0,180,0)

cv2.line(pitch, (lenght//2, 20), (lenght//2, width-20), (255, 255, 255), 2)

cv2.rectangle(pitch, (20, 20), (lenght-20, width-20), (255, 255, 255), 2)

cv2.rectangle(pitch, (20, 160), (120, 350), (255, 255, 255), 2)
cv2.rectangle(pitch, (lenght-120, 160), (lenght-20, 350), (255, 255, 255), 2)

cv2.rectangle(pitch, (20, 100), (180, 410), (255, 255, 255), 2)
cv2.rectangle(pitch, (lenght-180, 100), (lenght-20, 410), (255, 255, 255), 2)

cv2.circle(pitch, (lenght//2, width//2), 100, (255, 255, 255), 2)
cv2.circle(pitch, (lenght//2, width//2), 7, (255, 255, 255), -2)

cv2.imwrite("Outputs\Football_pitch.jpg", pitch)