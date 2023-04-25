import cv2
img = cv2.imread('Inputs\cats.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

smile_datector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
smiles = smile_datector.detectMultiScale(img_gray, 1.3, minSize=(20, 50), maxSize=(70,200))

smile_sticker = cv2.imread("Outputs\Football_pitch.jpg")
for smile in smiles:
        x, y, w, h = smile
        smile_sticker = cv2.resize(smile_sticker, [w, h])
        img[y:y+h, x:x+w] = smile_sticker


cv2.imshow('', img)
cv2.waitKey()