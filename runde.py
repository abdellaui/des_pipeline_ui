# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runde.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Bilder

class Runde(QtWidgets.QWidget):
    def __init__(self, attr: object, parent: object = None, main: object = None) -> object:
        super(QtWidgets.QWidget,self).__init__(parent)
        self.middle = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle.sizePolicy().hasHeightForWidth())

        self.middle.setSizePolicy(sizePolicy)
        self.middle.setMinimumSize(QtCore.QSize(800, 201))
        self.middle.setMaximumSize(QtCore.QSize(800, 201))
        if(attr[0]<15):
            self.middle.setStyleSheet("background-image: url(:/Bild/img/middle.png);")
        else:
            self.middle.setStyleSheet("background-image: url(:/Bild/img/middle_last.png);")

        self.middle.setObjectName("middle")

        self.links_button = QtWidgets.QPushButton(self.middle)
        self.links_button.setGeometry(QtCore.QRect(100, 0, 100, 31))
        self.links_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.links_button.setObjectName("links_button")

        self.rechts_button = QtWidgets.QPushButton(self.middle)
        self.rechts_button.setGeometry(QtCore.QRect(198, 0, 100, 31))
        self.rechts_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.rechts_button.setObjectName("rechts_button")

        self.transformer_button = QtWidgets.QPushButton(self.middle)
        self.transformer_button.setGeometry(QtCore.QRect(533, 27, 141, 61))
        self.transformer_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.transformer_button.setObjectName("transformer_button")

        self.f_funktion_button = QtWidgets.QPushButton(self.middle)
        self.f_funktion_button.setGeometry(QtCore.QRect(200, 72, 31, 31))
        self.f_funktion_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.f_funktion_button.setObjectName("f_funktion_button")

        self.k_button = QtWidgets.QPushButton(self.middle)
        self.k_button.setGeometry(QtCore.QRect(380, 70, 41, 41))
        self.k_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.k_button.setObjectName("k_button")

        self.xor_button = QtWidgets.QPushButton(self.middle)
        self.xor_button.setGeometry(QtCore.QRect(129, 72, 31, 31))
        self.xor_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.xor_button.setObjectName("xor_button")

        # Text-Ausgabe
        _translate = QtCore.QCoreApplication.translate
        self.links_button.setText(_translate("Form", "L {}".format(attr[0])))
        self.rechts_button.setText(_translate("Form", "R {}".format(attr[0])))
        self.transformer_button.setText(_translate("Form", "Transformater {}".format(attr[0]+1)))
        self.f_funktion_button.setText(_translate("Form", "f {}").format(attr[0]))
        self.k_button.setText(_translate("Form", "k {}").format(attr[0]+1))
        self.xor_button.setText(_translate("Form", "XOR"))

        # Button-onclick-Ausgaben
        links_button_output = [["Output  ", main.ausgabeArr['L'][attr[0]]]]
        self.links_button.clicked.connect(lambda: main.zeigeBits([self.links_button,links_button_output]))
        rechts_button_output = [["Output  ", main.ausgabeArr['R'][attr[0]]]]
        self.rechts_button.clicked.connect(lambda: main.zeigeBits([self.rechts_button,rechts_button_output]))
        k_button_output = [["Output  ", main.ausgabeArr['key'][attr[0]]]]
        self.k_button.clicked.connect(lambda: main.zeigeBits([self.k_button,k_button_output]))
        xor_output = [["Input L ", main.ausgabeArr['L'][attr[0]]],
                      ["Input f ", main.ausgabeArr['f_permutation'][attr[0]]],
                      ["Output  ", main.ausgabeArr['xor_nach_f'][attr[0]]]]
        self.xor_button.clicked.connect(lambda: main.zeigeBits([self.xor_button,xor_output]))
        self.transformer_button.clicked.connect(lambda: main.zeigeTransformation([self.transformer_button, attr[0]]))
        self.f_funktion_button.clicked.connect(lambda: main.zeigeFinside([self.f_funktion_button, attr[0]]))

        QtCore.QMetaObject.connectSlotsByName(self)



