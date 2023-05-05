import cv2
import numpy as np


img = cv2.imread('Inputs\clahe.png', 0)


# 1. Edge detection filter
kernel1 =   np.array([[-1 , -1 , -1],
                      [-1 ,  8 , -1],
                      [-1 , -1 , -1]])

# 2. Sharpening filter
kernel2 =   np.array([[0  , -1 ,  0],
                      [-1 ,  5 , -1],
                      [0  , -1 ,  0]])

# 3. Emboss filter
kernel3 =   np.array([[-2 , -1 ,  0],
                      [-1 ,  1 ,  1],
                      [0  ,  1 ,  2]])

# 4. Identity filter
kernel4 =   np.array([[0  ,  0 ,  0],
                      [0  ,  1 ,  0],
                      [0  ,  0 ,  0]])

# 5. Your filterLC
my_kernel = np.array([[4  ,  0 ,  0],
                      [0  ,  0 ,  0],
                      [0  ,  0 , -4]])

result1   = cv2.filter2D(img, -1,   kernel1)      
result2   = cv2.filter2D(img, -1,   kernel2)      
result3   = cv2.filter2D(img, -1,   kernel3)      
result4   = cv2.filter2D(img, -1,   kernel4)      
my_result = cv2.filter2D(img, -1, my_kernel)      

img1   = np.hstack((img,   result1))
img2   = np.hstack((img,   result2))
img3   = np.hstack((img,   result3))
img4   = np.hstack((img,   result4))
my_img = np.hstack((img, my_result))

cv2.imwrite(  "Outputs/2D_filters/image_filter1.jpg",   img1)
cv2.imwrite(  "Outputs/2D_filters/image_filter2.jpg",   img2)
cv2.imwrite(  "Outputs/2D_filters/image_filter3.jpg",   img3)
cv2.imwrite(  "Outputs/2D_filters/image_filter4.jpg",   img4)
cv2.imwrite("Outputs/2D_filters/my_image_filter.jpg", my_img)