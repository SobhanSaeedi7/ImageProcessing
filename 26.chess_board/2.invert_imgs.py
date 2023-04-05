import cv2

woman = cv2.imread('inputs\woman.PNG')
man = cv2.imread('inputs\man.PNG')


for i in range(woman.shape[0]):
    for j in range(woman.shape[1]):
        woman[i, j] = 255 - woman[i, j]


for i in range(man.shape[0]):
    for j in range(man.shape[1]):
        man[i, j] = 255 - man[i, j]


cv2.imwrite("outputs\woman.jpg", woman)
cv2.imwrite("outputs\man.jpg", man)