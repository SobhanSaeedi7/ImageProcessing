import cv2

img = cv2.imread("Inputs\Bat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)

cv2.putText(img, "BATMAN", (170, 550), 4, 5, 255)


cv2.imwrite("Outputs\Batman.jpg", img)