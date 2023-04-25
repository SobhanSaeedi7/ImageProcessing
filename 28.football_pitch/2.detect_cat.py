import cv2

img = cv2.imread("Inputs/cats.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")

faces = detector.detectMultiScale(img_gray)

count=0
for face in faces:
    x, y, w, h = face
    cv2.rectangle(img, [x, y], [x+w, y+h], [0, 0, 0], 5)
    count+=1

print(f"There are {count} cats in image")

cv2.imwrite("Outputs\Cats.jpg", img)
