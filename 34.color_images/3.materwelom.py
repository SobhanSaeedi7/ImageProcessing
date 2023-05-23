import cv2

img = cv2.imread("inputs\watermelon.jpg")

B, G, R = cv2.split(img)

result = cv2.merge((B, R, G))

cv2.imwrite("outputs\materwelon.jpg", result)