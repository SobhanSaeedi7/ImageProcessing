import cv2
import numpy as np


def decryptor():
    encrypted_img = cv2.imread('Outputs/encrypted_img.bmp')
    key_img = np.load('Outputs/key.npy')

    encrypted = np.array(encrypted_img)
    key = np.array(key_img, dtype=np.uint8)

    decrypted = cv2.bitwise_xor(key, encrypted)
    cv2.imwrite('Outputs/decrypted_img.jpg', decrypted)
    

