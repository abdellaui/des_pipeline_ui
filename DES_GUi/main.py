# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 864)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(825, 800))
        MainWindow.setMaximumSize(QtCore.QSize(825, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(850, 835))
        self.centralwidget.setMaximumSize(QtCore.QSize(850, 835))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())
        self.top.setSizePolicy(sizePolicy)
        self.top.setMinimumSize(QtCore.QSize(800, 225))
        self.top.setMaximumSize(QtCore.QSize(800, 225))
        self.top.setStyleSheet("background-image: url(:/Bild/img/top.png);")
        self.top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.eingang_ip_button = QtWidgets.QPushButton(self.top)
        self.eingang_ip_button.setGeometry(QtCore.QRect(115, 111, 174, 59))
        self.eingang_ip_button.setObjectName("eingang_ip_button")
        self.klartext_button = QtWidgets.QPushButton(self.top)
        self.klartext_button.setGeometry(QtCore.QRect(131, 25, 141, 31))
        self.klartext_button.setObjectName("klartext_button")
        self.schlussel_k_button = QtWidgets.QPushButton(self.top)
        self.schlussel_k_button.setGeometry(QtCore.QRect(534, 24, 141, 31))
        self.schlussel_k_button.setObjectName("schlussel_k_button")
        self.pc_1_button = QtWidgets.QPushButton(self.top)
        self.pc_1_button.setGeometry(QtCore.QRect(532, 110, 141, 31))
        self.pc_1_button.setObjectName("pc_1_button")
        self.eingang_ip_button.raise_()
        self.klartext_button.raise_()
        self.schlussel_k_button.raise_()
        self.pc_1_button.raise_()
        self.verticalLayout.addWidget(self.top)
        self.rundenListe = QtWidgets.QListWidget(self.centralwidget)
        self.rundenListe.setMinimumSize(QtCore.QSize(831, 402))
        self.rundenListe.setMaximumSize(QtCore.QSize(831, 402))
        self.rundenListe.setObjectName("rundenListe")
        self.verticalLayout.addWidget(self.rundenListe)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom.sizePolicy().hasHeightForWidth())
        self.bottom.setSizePolicy(sizePolicy)
        self.bottom.setMinimumSize(QtCore.QSize(800, 179))
        self.bottom.setMaximumSize(QtCore.QSize(800, 179))
        self.bottom.setStyleSheet("background-image: url(:/Bild/img/bottom.png);")
        self.bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.ausgang_ip_1_button = QtWidgets.QPushButton(self.bottom)
        self.ausgang_ip_1_button.setGeometry(QtCore.QRect(115, 1, 174, 59))
        self.ausgang_ip_1_button.setObjectName("ausgang_ip_1_button")
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.eingang_ip_button.setText(_translate("MainWindow", "Eingang IP"))
        self.klartext_button.setText(_translate("MainWindow", "Klartext x"))
        self.schlussel_k_button.setText(_translate("MainWindow", "Schlussel k"))
        self.pc_1_button.setText(_translate("MainWindow", "PC-1"))
        self.ausgang_ip_1_button.setText(_translate("MainWindow", "Ausgang IP_1"))

import Bilder_rc
