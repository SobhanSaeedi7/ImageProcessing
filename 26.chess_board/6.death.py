import cv2


image=cv2.imread("inputs\JohanCruyff.jpg")
image_2=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


for i in range(250):
    image_2[i, 250-i:400-i] = 0

for i in range(250, 400):
    image_2[i, 0:400-i]=0


cv2.imwrite("outputs\JohanCruyff.jpg", image_2)