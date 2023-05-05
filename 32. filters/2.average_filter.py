import cv2
import numpy as np


img = cv2.imread('Inputs/1.tif', 0)


kernel1 = np.array([[0.04 ,0.04 ,0.04 ,0.04 ,0.04],
                    [0.04 ,0.04 ,0.04 ,0.04 ,0.04],
                    [0.04 ,0.04 ,0.04 ,0.04 ,0.04],
                    [0.04 ,0.04 ,0.04 ,0.04 ,0.04],
                    [0.04 ,0.04 ,0.04 ,0.04 ,0.04]])

kernel2 = np.array([[  1  ,  1  ,  1  ,  1  ,  1 ],
                    [  1  ,  1  ,  1  ,  1  ,  1 ],
                    [  1  ,  1  ,  1  ,  1  ,  1 ],
                    [  1  ,  1  ,  1  ,  1  ,  1 ],
                    [  1  ,  1  ,  1  ,  1  ,  1 ]])

kernel3 = np.array([[  5  ,  5  ,  5  , 5  ,  5 ],
                    [  5  ,  5  ,  5  , 5  ,  5 ],
                    [  5  ,  5  ,  5  , 5  ,  5 ],
                    [  5  ,  5  ,  5  , 5  ,  5 ],
                    [  5  ,  5  ,  5  , 5  ,  5 ]])

kernel4 = np.array([[0.04 ,0.04 ,0.04],
                    [0.04 ,0.04 ,0.04],
                    [0.04 ,0.04 ,0.04]])

kernel5 = np.array([[  1  ,  1  ,  1 ],
                    [  1  ,  1  ,  1 ],
                    [  1  ,  1  ,  1 ]])

kernel6 = np.array([[  5  ,  5  ,  5 ],
                    [  5  ,  5  ,  5 ],
                    [  5  ,  5  ,  5 ]])


result1   = cv2.filter2D(img, -1,   kernel1)      
result2   = cv2.filter2D(img, -1,   kernel2)      
result3   = cv2.filter2D(img, -1,   kernel3)      
result4   = cv2.filter2D(img, -1,   kernel4) 
result5   = cv2.filter2D(img, -1,   kernel5)      
result6   = cv2.filter2D(img, -1,   kernel6) 

img_result = np.hstack((img, result1, result2, result3, result4, result5, result6))


cv2.imwrite("Outputs/magic.jpg", img_result)