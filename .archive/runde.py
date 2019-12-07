# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runde.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(863, 272)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(800, 201))
        self.frame.setMaximumSize(QtCore.QSize(800, 201))
        self.frame.setStyleSheet("background-image: url(:/Bild/img/middle.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.links_button = QtWidgets.QPushButton(self.frame)
        self.links_button.setGeometry(QtCore.QRect(110, 0, 101, 31))
        self.links_button.setObjectName("links_button")
        self.rechts_button = QtWidgets.QPushButton(self.frame)
        self.rechts_button.setGeometry(QtCore.QRect(210, 0, 101, 31))
        self.rechts_button.setObjectName("rechts_button")
        self.transformer_button = QtWidgets.QPushButton(self.frame)
        self.transformer_button.setGeometry(QtCore.QRect(534, 27, 141, 61))
        self.transformer_button.setObjectName("transformer_button")
        self.f_funktion_button = QtWidgets.QPushButton(self.frame)
        self.f_funktion_button.setGeometry(QtCore.QRect(200, 73, 31, 31))
        self.f_funktion_button.setObjectName("f_funktion_button")
        self.k_button = QtWidgets.QPushButton(self.frame)
        self.k_button.setGeometry(QtCore.QRect(380, 70, 41, 41))
        self.k_button.setObjectName("k_button")
        self.xor_button = QtWidgets.QPushButton(self.frame)
        self.xor_button.setGeometry(QtCore.QRect(129, 73, 31, 31))
        self.xor_button.setObjectName("xor_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.links_button.setText(_translate("Form", "L #"))
        self.rechts_button.setText(_translate("Form", "R #"))
        self.transformer_button.setText(_translate("Form", "Transformater #"))
        self.f_funktion_button.setText(_translate("Form", "f"))
        self.k_button.setText(_translate("Form", "k #"))
        self.xor_button.setText(_translate("Form", "XOR"))

import Bilder_rc
