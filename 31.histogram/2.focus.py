import cv2 
import numpy as np 

img = cv2.imread("Inputs/flower.png" , cv2.IMREAD_GRAYSCALE) 

rows , cols = img.shape
result = np.zeros((rows-30 , cols-30) ,dtype=np.uint8 )


for i in range(15 , rows-15 ):
    for j in range(15 , cols-15):
        small = img[i-15:i+16 , j-15:j+16]    
        if img[i,j] < 160 :              
            avg = np.mean(small)
            result[i-15 , j-15] = avg
        else :
            result[i-15, j-15] =img[i , j]


cv2.imwrite("Output/portrait.jpg" , result)