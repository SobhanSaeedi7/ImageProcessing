import cv2


img = cv2.imread("inputs/rubik.png")


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        B, G, R = img[i, j] 
        if B > 100 and G > 100 and R < 50:
            B = 0 
            G = 0
            R = 255
        if B > 100 and G < 50 and R > 100:
            B = 0 
            R = 0
            G = 255
        if B < 50 and G > 100 and R > 100:
            B = 255 
            G = 0
            R = 0

        img[i, j] = B, G, R

cv2.imwrite("outputs/rubik.jpg", img)