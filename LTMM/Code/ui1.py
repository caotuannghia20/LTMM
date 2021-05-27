from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from encrypt import*
from decrypt import*
import cv2
import numpy as np
import sys
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1238, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.open = QtWidgets.QLabel(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(10, 10, 51, 31))
        self.open.setObjectName("open")
        self.open.setStyleSheet('border: 1px solid pink')

        self.dirImage = QtWidgets.QLineEdit(self.centralwidget)
        self.dirImage.setGeometry(QtCore.QRect(72, 10, 891, 31))
        self.dirImage.setObjectName("dirImage")

        self.parameter = QtWidgets.QLabel(self.centralwidget)
        self.parameter.setGeometry(QtCore.QRect(1060, 60, 171, 31))
        self.parameter.setObjectName("parameter")
        self.parameter.setStyleSheet('border: 1px solid pink')

        self.x = QtWidgets.QLabel(self.centralwidget)
        self.x.setGeometry(QtCore.QRect(1060, 100, 41, 31))
        self.x.setObjectName("x")
        self.x.setStyleSheet('border: 1px solid pink')

        self.muy = QtWidgets.QLabel(self.centralwidget)
        self.muy.setGeometry(QtCore.QRect(1060, 140, 41, 31))
        self.muy.setObjectName("muy")
        self.muy.setStyleSheet('border: 1px solid pink')

        self.value_x = QtWidgets.QLineEdit(self.centralwidget)
        self.value_x.setGeometry(QtCore.QRect(1110, 100, 121, 31))
        self.value_x.setObjectName("value_x")

        self.value_muy = QtWidgets.QLineEdit(self.centralwidget)
        self.value_muy.setGeometry(QtCore.QRect(1110, 140, 121, 31))
        self.value_muy.setObjectName("value_muy")

        self.photo = QtWidgets.QGraphicsView(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(10, 50, 1041, 691))
        self.photo.setObjectName("photo")

        self.encryptImage = QtWidgets.QPushButton(self.centralwidget)
        self.encryptImage.setGeometry(QtCore.QRect(1060, 590, 171, 71))
        self.encryptImage.setObjectName("encryptImage")
        self.encryptImage.clicked.connect(self.func_encryptImage)

        self.decryptImage = QtWidgets.QPushButton(self.centralwidget)
        self.decryptImage.setGeometry(QtCore.QRect(1060, 670, 171, 71))
        self.decryptImage.setObjectName("decryptImage")
        self.decryptImage.clicked.connect(self.func_decryptImage)

        self.openDialog = QtWidgets.QToolButton(self.centralwidget)
        self.openDialog.setGeometry(QtCore.QRect(960, 10, 31, 31))
        self.openDialog.setObjectName("openDialog")
        self.openDialog.clicked.connect(self.getDirImage)

        self.checkImage = QtWidgets.QPushButton(self.centralwidget)
        self.checkImage.setGeometry(QtCore.QRect(1000, 10, 51, 31))
        self.checkImage.setObjectName("checkImage")
        self.checkImage.clicked.connect(self.load_image)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1238, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.changeFolder = QtWidgets.QMenu(self.menuFile)
        self.changeFolder.setObjectName("changeFolder")

        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(MainWindow.close)

        self.dirEncrypt = QtWidgets.QAction(MainWindow)
        self.dirEncrypt.setObjectName("dirEncrypt")
        self.dirEncrypt.triggered.connect(self.getFolder_save_ImgEncrypt)

        self.dirDecrypt = QtWidgets.QAction(MainWindow)
        self.dirDecrypt.setObjectName("dirDecrypt")
        self.dirDecrypt.triggered.connect(self.getFolder_save_ImgDecrypt)

        self.zoomIn = QtWidgets.QAction(MainWindow)
        self.zoomIn.setObjectName("zoomIn")
        self.zoomIn.triggered.connect(self.zoomIn_image)

        self.zoomOut = QtWidgets.QAction(MainWindow)
        self.zoomOut.setObjectName("zoomOut")
        self.zoomOut.triggered.connect(self.zoomOut_image)

        self.changeFolder.addAction(self.dirEncrypt)
        self.changeFolder.addAction(self.dirDecrypt)

        self.menuFile.addAction(self.changeFolder.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.zoomIn)
        self.menuView.addAction(self.zoomOut)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.scene = QtWidgets.QGraphicsScene()

        self.dirsaveEncryptImg = None
        self.dirsaveDecryptImg = None

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #Encrypt Image
    def func_encryptImage(self):
        x = float(self.value_x.text())
        muy = float(self.value_muy.text())
        img = encrypt_function(x, muy, self.dirImage.text())
        baseName = os.path.basename(self.dirImage.text())
        print(type(self.dirsaveEncryptImg))
        if self.dirsaveEncryptImg == None:
            imgName = 'encrypt_' + baseName
            cv2.imwrite(imgName, img)
        else:
            imgName = 'encrypt_' + baseName
            print(imgName)
            cv2.imwrite(os.path.join(self.dirsaveEncryptImg, imgName), img)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.NoIcon)
        msg.setText("Succesfully")
        msg.setInformativeText('Encrypt Image Successfully\nName of image: ' + imgName)
        msg.setWindowTitle("Succesfully")
        msg.exec_()


    def func_decryptImage(self):
        x = float(self.value_x.text())
        muy = float(self.value_muy.text())
        img = decrypt_function(x, muy, self.dirImage.text())
        baseName = os.path.basename(self.dirImage.text())
        if self.dirsaveDecryptImg == None:
            imgName = 'decrypt_' + baseName
            cv2.imwrite(imgName, img)
        else:
            imgName = 'decrypt_' + baseName
            cv2.imwrite(os.path.join(self.dirsaveDecryptImg, str(imgName)), img)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.NoIcon)
        msg.setText("Succesfully")
        msg.setInformativeText('Decrypt Image Successfully\nName of image: ' + imgName)
        msg.setWindowTitle("Succesfully")
        msg.exec_()


    #Function zoom in and zoom out image
    def zoomIn_image(self):
        self.photo.scale(1.25, 1.25)

    def zoomOut_image(self):
        self.photo.scale(0.8, 0.8)

    #Function get folder save image after encryption and decryption
    def getFolder_save_ImgEncrypt(self):
        fname_encrypt = QFileDialog.getExistingDirectory(caption='Choose folder to save Encryption Image', directory='/home')
        self.dirsaveEncryptImg = str(fname_encrypt)
    def getFolder_save_ImgDecrypt(self):
        fname_decrypt = QFileDialog.getExistingDirectory(caption='Choose folder to save Decryption Image', directory='/home')
        self.dirsaveDecryptImg = str(fname_decrypt)
    #get directory Image
    def getDirImage(self):
        fname_image = QFileDialog.getOpenFileName(caption='Choose a image', directory='/home')
        fname_image = fname_image[0]
        self.dirImage.setText(str(fname_image))

    #load image and show in QGraphicView 
    def load_image(self):
        self.img = cv2.imread(self.dirImage.text())
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        self.img = cv2.resize(self.img, (1031, 681))
        self.img = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0], self.img.shape[1], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap.fromImage(self.img)
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.photo.setScene(self.scene)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open.setText(_translate("MainWindow", " Open"))
        self.parameter.setText(_translate("MainWindow", "           Parameter"))
        self.x.setText(_translate("MainWindow", "    x"))
        self.muy.setText(_translate("MainWindow", "    μ"))
        self.encryptImage.setText(_translate("MainWindow", "Encryption Image"))
        self.decryptImage.setText(_translate("MainWindow", "Decryption Image"))
        self.openDialog.setText(_translate("MainWindow", "..."))
        self.checkImage.setText(_translate("MainWindow", "OK"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.changeFolder.setTitle(_translate("MainWindow", "Change folder save"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.dirEncrypt.setText(_translate("MainWindow", "Encryption Image"))
        self.dirDecrypt.setText(_translate("MainWindow", "Decryption Image"))
        self.zoomIn.setText(_translate("MainWindow", "Zoom in"))
        self.zoomOut.setText(_translate("MainWindow", "Zoom out"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

