# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transformation.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Bilder
import DES_Generator

class Transformation(QtWidgets.QWidget):
    def __init__(self, attr: object, parent: object = None, main: object = None) -> object:
        super(QtWidgets.QWidget,self).__init__(parent)
        self.transfo_mit_info = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transfo_mit_info.sizePolicy().hasHeightForWidth())

        self.transfo_mit_info.setSizePolicy(sizePolicy)
        self.transfo_mit_info.setGeometry(QtCore.QRect(0, 0, 650, 931))
        self.transfo_mit_info.setMinimumSize(QtCore.QSize(650, 600))
        self.transfo_mit_info.setObjectName("transfo_mit_info")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.transfo_mit_info)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setAlignment(QtCore.Qt.AlignTop)

        self.transformations_ansicht = QtWidgets.QWidget(self.transfo_mit_info)
        self.transformations_ansicht.setMinimumSize(QtCore.QSize(530, 276))
        self.transformations_ansicht.setMaximumSize(QtCore.QSize(530, 276))
        self.transformations_ansicht.setStyleSheet("background-image: url(:/Bild/img/transformation.png);")
        self.transformations_ansicht.setObjectName("transformations_ansicht")

        self.c_button = QtWidgets.QPushButton(self.transformations_ansicht)
        self.c_button.setGeometry(QtCore.QRect(226, 0, 118, 35))
        self.c_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.c_button.setObjectName("c_button")

        self.d_button = QtWidgets.QPushButton(self.transformations_ansicht)
        self.d_button.setGeometry(QtCore.QRect(340, 0, 118, 35))
        self.d_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.d_button.setObjectName("d_button")

        self.ls_links_button = QtWidgets.QPushButton(self.transformations_ansicht)
        self.ls_links_button.setGeometry(QtCore.QRect(230, 100, 51, 35))
        self.ls_links_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.ls_links_button.setObjectName("ls_links_button")

        self.ls_rechts_button = QtWidgets.QPushButton(self.transformations_ansicht)
        self.ls_rechts_button.setGeometry(QtCore.QRect(347, 100, 51, 35))
        self.ls_rechts_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.ls_rechts_button.setObjectName("ls_rechts_button")

        self.c1_button = QtWidgets.QPushButton(self.transformations_ansicht)
        self.c1_button.setGeometry(QtCore.QRect(226, 196, 118, 35))
        self.c1_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.c1_button.setObjectName("c1_button")

        self.d1_button = QtWidgets.QPushButton(self.transformations_ansicht)
        self.d1_button.setGeometry(QtCore.QRect(340, 196, 118, 35))
        self.d1_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.d1_button.setObjectName("d1_button")

        self.pc_2_button = QtWidgets.QPushButton(self.transformations_ansicht)
        self.pc_2_button.setGeometry(QtCore.QRect(76, 201, 79, 31))
        self.pc_2_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.pc_2_button.setObjectName("pc_2_button")

        self.transformationsname = QtWidgets.QLabel(self.transformations_ansicht)
        self.transformationsname.setGeometry(QtCore.QRect(64, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.transformationsname.setFont(font)
        self.transformationsname.setObjectName("transformationsname")

        self.verticalLayout.addWidget(self.transformations_ansicht)
        self.information_trans_groupbox = QtWidgets.QGroupBox(self.transfo_mit_info)
        self.information_trans_groupbox.setObjectName("information_trans_groupbox")
        self.information_trans_groupbox.hide()

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.information_trans_groupbox)
        self.verticalLayout_3.setAlignment(QtCore.Qt.AlignTop)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.label_information = QtWidgets.QLabel(self.information_trans_groupbox)
        self.label_information.setObjectName("label_information")
        self.label_information.setFont(font)
        self.verticalLayout_3.addWidget(self.label_information)

        self.ausgabe1 = QtWidgets.QLabel(self.label_information)
        self.ausgabe1.setObjectName("ausgabe1")
        font = QtGui.QFont(QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))
        self.ausgabe1.setFont(font)
        self.verticalLayout_3.addWidget(self.ausgabe1)

        self.verticalLayout.addWidget(self.information_trans_groupbox)


        # Text-Ausgabe
        _translate = QtCore.QCoreApplication.translate
        self.c_button.setText(_translate("Form", "C {}").format(attr[0]))
        self.d_button.setText(_translate("Form", "D {}").format(attr[0]))
        self.ls_links_button.setText(_translate("Form", "LS l {}").format(attr[0]+1))
        self.ls_rechts_button.setText(_translate("Form", "LS r {}").format(attr[0]+1))
        self.c1_button.setText(_translate("Form", "C {}").format(attr[0]+1))
        self.d1_button.setText(_translate("Form", "D {}").format(attr[0]+1))
        self.pc_2_button.setText(_translate("Form", "PC-2"))
        self.transformationsname.setText(_translate("Form", "Transformation {}").format(attr[0]+1))
        self.information_trans_groupbox.setTitle(_translate("Form", "Information -> Transformation {}").format(attr[0]+1))

        # Button-onclick-Ausgaben
        c_button_output = [["Output  ", attr[1]["C"][attr[0]]]]
        self.c_button.clicked.connect(lambda: self.zeigeBits([self.c_button, c_button_output]))
        d_button_output = [["Output  ", attr[1]["D"][attr[0]]]]
        self.d_button.clicked.connect(lambda: self.zeigeBits([self.d_button, d_button_output]))
        ls_links_button_output = [["Input   ", attr[1]["C"][attr[0]]], ["Output  ", attr[1]["LSl"][attr[0]]]]
        self.ls_links_button.clicked.connect(lambda: self.zeigeBits([self.ls_links_button, ls_links_button_output]))
        ls_rechts_button_output = [["Input   ", attr[1]["D"][attr[0]]], ["Output  ", attr[1]["LSr"][attr[0]]]]
        self.ls_rechts_button.clicked.connect(lambda: self.zeigeBits([self.ls_rechts_button, ls_rechts_button_output]))
        c1_button_output = [["Input   ", attr[1]["LSl"][attr[0]]], ["Output  ", attr[1]["LSl"][attr[0]]]]
        self.c1_button.clicked.connect(lambda: self.zeigeBits([self.c1_button, c1_button_output]))
        d1_button_output = [["Input   ", attr[1]["LSr"][attr[0]]], ["Output  ", attr[1]["LSr"][attr[0]]]]
        self.d1_button.clicked.connect(lambda: self.zeigeBits([self.d1_button, d1_button_output]))
        pc_2_button_output = [["Input   ", attr[1]["PC-2-INPUT"][attr[0]]], ["Output  ", attr[1]["key"][attr[0]]]]
        self.pc_2_button.clicked.connect(lambda: self.zeigeBits([self.pc_2_button, pc_2_button_output],"PC_2"))

        QtCore.QMetaObject.connectSlotsByName(self)

    def zeigeBits(self, bits, sub_tabelle=None):
        if sub_tabelle:
            ausgabe_string = DES_Generator.zeigeTabelle(sub_tabelle)
        else:
            ausgabe_string = ""
        for x in bits[1]:
            ausgabe_string += x[0] + " (" + str(len(x[1])) + " bit) : "
            for l,z in enumerate(x[1]):
                if(l%4==0):
                    ausgabe_string +=" "
                ausgabe_string +=str(z)
            ausgabe_string += "\n"
        self.ausgabe1.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.ausgabe1.setText(ausgabe_string)

        self.info_ausgabe(bits[0].text())

    def info_ausgabe(self,information):
        self.label_information.setText(information)
        self.information_trans_groupbox.show()