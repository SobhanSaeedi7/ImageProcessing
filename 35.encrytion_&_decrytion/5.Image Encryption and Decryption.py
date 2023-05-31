import sys
import cv2
import numpy as np
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from decryptor import decryptor
from encryptor import encryptor


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        encryptor('Inputs\python.jpg')
        decryptor()
    
        self.btn_1 = QPushButton(text='Encrypted image')
        self.layout.addWidget(self.btn_1)
    
        self.label_1 = QLabel()
        self.layout.addWidget(self.label_1)

        img_1 = cv2.imread('Outputs\encrypted_img.bmp')
        img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
        img_qt_1 = QImage(img_1, img_1.shape[1], img_1.shape[0], QImage.Format.Format_RGB888)
        qpixmap_1 = QPixmap.fromImage(img_qt_1)
        self.label_1.setPixmap(qpixmap_1)

        self.btn_2 = QPushButton(text='Secret Key')
        self.layout.addWidget(self.btn_2)

        self.label_2 = QLabel()
        self.layout.addWidget(self.label_2)

        img_2 = np.load('Outputs\key.npy')
        img_qt_2 = QImage(img_2, img_1.shape[1], img_1.shape[0], QImage.Format.Format_RGB888)
        qpixmap_2 = QPixmap.fromImage(img_qt_2)
        self.label_2.setPixmap(qpixmap_2)
    
        self.btn_3 = QPushButton(text='Decrypted image')
        self.layout.addWidget(self.btn_3)

        self.label_3 = QLabel()
        self.layout.addWidget(self.label_3)

        img_3 = cv2.imread('Outputs\decrypted_img.jpg')
        img_3 = cv2.cvtColor(img_3, cv2.COLOR_BGR2RGB)
        img_qt_3 = QImage(img_3, img_1.shape[1], img_1.shape[0], QImage.Format.Format_RGB888)
        qpixmap_3 = QPixmap.fromImage(img_qt_3)
        self.label_3.setPixmap(qpixmap_3)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)




app = QApplication(sys.argv)

window = MyWindow()
window.show()

app.exec()

