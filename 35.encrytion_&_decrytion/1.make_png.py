import cv2


img = cv2.imread('Inputs/microsoft_logo.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i, j][0] <= 100 and img[i, j][1]<= 100 and img[i, j][2] <= 100:
            img[i, j][3] = 0


cv2.imwrite('Outputs/png_logo.png', img)