import cv2

sad_image = cv2.imread('inputs\sad_mans.png')
happy_image = cv2.imread('inputs\sad_mans.png')


for i in range(sad_image.shape[0]):
    for j in range(sad_image.shape[1]):
        happy_image[i, j] = sad_image[sad_image.shape[0]-i-1, sad_image.shape[1]-j-1]


cv2.imwrite("outputs\happy_mans.jpg", happy_image)
