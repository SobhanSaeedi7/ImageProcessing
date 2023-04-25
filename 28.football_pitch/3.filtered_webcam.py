import cv2

def sticker_face(img):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = detector.detectMultiScale(img_gray, 1.3)
    face_sticker = cv2.imread("Inputs\sid2.sid2.png")
    for face in faces:
        x, y, w, h = face
        sticker = cv2.resize(face_sticker,[w,h])
        for i in range(h):
            for j in range(w):
                if sticker[i][j][0] == 0 and sticker[i][j][1] == 0 and sticker[i][j][2] == 0:
                    sticker[i][j] = img[y+i,x+j]
        img[y:y+h, x:x+w] = sticker

    return img


def sticker_eye_lips(img):
    img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
    lip_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

    lip_sticker = cv2.imread("Inputs\emoji.png")
    glasses_sticker = cv2.imread("Inputs\emoji.png")

    faces = face_detector.detectMultiScale(img_gray, 1.3)    

    for face in faces:
        x, y, w, h = face
        face_part = img_gray[x:x+h, y:y+w] 

        lips = lip_detector.detectMultiScale(face_part, 1.3, minSize=(20, 50), maxSize=(70,200))
        eyes = eye_detector.detectMultiScale(face_part, 1.5, minSize=(80, 90))

        
        for lip in lips:
                x,y,w,h = lip
                sticker = cv2.resize(lip_sticker,[w,h])
                for i in range(h):
                    for j in range(w):
                        if sticker[i][j][0] == sticker[i][j][1] == sticker[i][j][2] ==0 or sticker[i][j][0] == sticker[i][j][1] == sticker[i][j][2] ==255:
                            sticker[i][j] = img[y+i,x+j]
                img[y:y+h,x:x+w] = sticker
        
        w_g=1
        h_g=1
        x_g=600
        y_g=400
        for eye in eyes:
            x, y, w, h = eye
            w_g += w
            if h > h_g:
                h_g=h
            if x < x_g:
                x_g=x
            if y < y_g:
                y_g=y
            

        sticker_2 = cv2.resize(glasses_sticker,[w_g, h_g])
        for i in range(h_g):
            for j in range(w_g):
                if sticker_2[i][j][0] == sticker_2[i][j][1] == sticker_2[i][j][2] ==0:
                    sticker_2[i][j] = img[y_g+i,x_g+j]
        img[y_g:y_g+h_g,x_g:x_g+w_g] = sticker_2

    return img


def chess_face(img):
    face_datector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_datector.detectMultiScale(img, 1.3)
    for face in faces:
        x, y, w, h = face
        face_img = img[y:y+h, x:x+w]
        smalled_img = cv2.resize(face_img, [10, 10])
        chess_img = cv2.resize(smalled_img, [w, h], interpolation=cv2.INTER_NEAREST)
        img[y:y+h, x:x+w] = chess_img

    return img


def mirror_face(img):
    col = img.shape[1]
    flipVertical = cv2.flip(img[:,:col//2], 1)
    img[:,col//2:] = flipVertical

    return img

cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows, cols, _ = frame.shape

choice = 1
while True:
    _, frame = cap.read()

    if choice == 1:
        frame = sticker_face(frame)
    elif choice == 2:
        frame = sticker_eye_lips(frame)
    elif choice == 3:
        frame = chess_face(frame)
    elif choice == 4:
        frame = mirror_face(frame)

    cv2.imshow('',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('1'):
        choice = 1
    elif cv2.waitKey(1) & 0xFF == ord('2'):
        choice = 2
    elif cv2.waitKey(1) & 0xFF == ord('3'):
        choice = 3
    elif cv2.waitKey(1) & 0xFF == ord('4'):
        choice = 4


cap.release()
cv2.destroyAllWindows()