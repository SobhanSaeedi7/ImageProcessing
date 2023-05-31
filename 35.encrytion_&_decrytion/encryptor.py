import cv2
import numpy as np

def encryptor(file_pass):
    img = cv2.imread(file_pass)
    rows, cols, _ = img.shape

    key_r = np.random.randint(0, 256, size=(rows, cols), dtype=np.uint8)
    key_g = np.random.randint(0, 256, size=(rows, cols), dtype=np.uint8)
    key_b = np.random.randint(0, 256, size=(rows, cols), dtype=np.uint8)

    b, g, r = cv2.split(img)

    encrypted_b = cv2.bitwise_xor(r, key_b)
    encrypted_g = cv2.bitwise_xor(g, key_g)
    encrypted_r = cv2.bitwise_xor(b, key_r)

    encrypted = cv2.merge((encrypted_r, encrypted_g, encrypted_b))
    key = cv2.merge((key_r, key_g, key_b))


    cv2.imwrite('Outputs/encrypted_img.bmp', encrypted)
    np.save('Outputs/key.npy', key)
