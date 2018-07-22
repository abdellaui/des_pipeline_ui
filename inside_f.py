# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inside_f.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Bilder
import DES_Generator

class Inside_f(QtWidgets.QWidget):
    def __init__(self, attr: object, parent: object = None, main: object = None) -> object:
        super(QtWidgets.QWidget,self).__init__(parent)
        self.inside_f = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inside_f.sizePolicy().hasHeightForWidth())

        self.inside_f.setSizePolicy(sizePolicy)
        self.inside_f.setGeometry(QtCore.QRect(0, 0, 650, 931))
        self.inside_f.setMinimumSize(QtCore.QSize(650, 0))
        self.inside_f.setObjectName("inside_f")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.inside_f)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setAlignment(QtCore.Qt.AlignTop)

        self.f_ansicht = QtWidgets.QWidget(self.inside_f)
        self.f_ansicht.setMinimumSize(QtCore.QSize(530, 740))
        self.f_ansicht.setMaximumSize(QtCore.QSize(530, 738))
        self.f_ansicht.setStyleSheet("background-image: url(:/Bild/img/inside_f.png);")
        self.f_ansicht.setObjectName("f_ansicht")

        self.R_i_minus_1_button = QtWidgets.QPushButton(self.f_ansicht)
        self.R_i_minus_1_button.setGeometry(QtCore.QRect(205, 0, 118, 35))
        self.R_i_minus_1_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.R_i_minus_1_button.setObjectName("R_i_minus_1_button")

        self.expansion_button = QtWidgets.QPushButton(self.f_ansicht)
        self.expansion_button.setGeometry(QtCore.QRect(190, 100, 141, 71))
        self.expansion_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.expansion_button.setObjectName("expansion_button")

        self.xor_button = QtWidgets.QPushButton(self.f_ansicht)
        self.xor_button.setGeometry(QtCore.QRect(244, 269, 35, 35))
        self.xor_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.xor_button.setObjectName("xor_button")

        self.k_i_button = QtWidgets.QPushButton(self.f_ansicht)
        self.k_i_button.setGeometry(QtCore.QRect(470, 269, 35, 35))
        self.k_i_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.k_i_button.setObjectName("k_i_button")

        self.s_button_1 = QtWidgets.QPushButton(self.f_ansicht)
        self.s_button_1.setGeometry(QtCore.QRect(12, 435, 35, 35))
        self.s_button_1.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.s_button_1.setObjectName("s_button_1")

        self.s_button_2 = QtWidgets.QPushButton(self.f_ansicht)
        self.s_button_2.setGeometry(QtCore.QRect(78, 435, 35, 35))
        self.s_button_2.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.s_button_2.setObjectName("s_button_2")

        self.s_button_3 = QtWidgets.QPushButton(self.f_ansicht)
        self.s_button_3.setGeometry(QtCore.QRect(145, 435, 35, 35))
        self.s_button_3.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.s_button_3.setObjectName("s_button_3")

        self.s_button_4 = QtWidgets.QPushButton(self.f_ansicht)
        self.s_button_4.setGeometry(QtCore.QRect(211, 435, 35, 35))
        self.s_button_4.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.s_button_4.setObjectName("s_button_4")

        self.s_button_5 = QtWidgets.QPushButton(self.f_ansicht)
        self.s_button_5.setGeometry(QtCore.QRect(278, 435, 35, 35))
        self.s_button_5.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.s_button_5.setObjectName("s_button_5")

        self.s_button_6 = QtWidgets.QPushButton(self.f_ansicht)
        self.s_button_6.setGeometry(QtCore.QRect(345, 435, 35, 35))
        self.s_button_6.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.s_button_6.setObjectName("s_button_6")

        self.s_button_7 = QtWidgets.QPushButton(self.f_ansicht)
        self.s_button_7.setGeometry(QtCore.QRect(410, 435, 35, 35))
        self.s_button_7.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.s_button_7.setObjectName("s_button_7")

        self.s_button_8 = QtWidgets.QPushButton(self.f_ansicht)
        self.s_button_8.setGeometry(QtCore.QRect(477, 435, 35, 35))
        self.s_button_8.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.s_button_8.setObjectName("s_button_8")

        self.permutation_button = QtWidgets.QPushButton(self.f_ansicht)
        self.permutation_button.setGeometry(QtCore.QRect(190, 600, 141, 71))
        self.permutation_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.permutation_button.setObjectName("expansion_button_2")

        self.verticalLayout.addWidget(self.f_ansicht)


        self.information_f_groupbox = QtWidgets.QGroupBox(self.inside_f)
        self.information_f_groupbox.setObjectName("information_f_groupbox")
        self.information_f_groupbox.hide()

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.information_f_groupbox)
        self.verticalLayout_3.setAlignment(QtCore.Qt.AlignTop)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_information = QtWidgets.QLabel(self.information_f_groupbox)
        self.label_information.setObjectName("label_information")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_information.setFont(font)

        self.verticalLayout_3.addWidget(self.label_information)

        self.ausgabe1 = QtWidgets.QLabel(self.label_information)
        self.ausgabe1.setObjectName("ausgabe1")
        font = QtGui.QFont(QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))
        self.ausgabe1.setFont(font)
        self.verticalLayout_3.addWidget(self.ausgabe1)

        self.f_ansicht.raise_()
        self.verticalLayout.addWidget(self.information_f_groupbox)

        # Text-Ausgaben
        _translate = QtCore.QCoreApplication.translate
        self.R_i_minus_1_button.setText(_translate("Form", "R {}").format(attr[0]))
        self.expansion_button.setText(_translate("Form", "Expansion E ( R {} ) ").format(attr[0]))
        self.xor_button.setText(_translate("Form", "XOR"))
        self.k_i_button.setText(_translate("Form", "k {}").format(attr[0]+1))
        self.s_button_1.setText(_translate("Form", "S 1"))
        self.s_button_2.setText(_translate("Form", "S 2"))
        self.s_button_3.setText(_translate("Form", "S 3"))
        self.s_button_4.setText(_translate("Form", "S 4"))
        self.s_button_5.setText(_translate("Form", "S 5"))
        self.s_button_6.setText(_translate("Form", "S 6"))
        self.s_button_7.setText(_translate("Form", "S 7"))
        self.s_button_8.setText(_translate("Form", "S 8"))
        self.permutation_button.setText(_translate("Form", "Permutation P #{}").format(attr[0]))
        self.information_f_groupbox.setTitle(_translate("Form", "Information -> f {}").format(attr[0]))

        # Button-onclick-Ausgaben
        R_i_minus_1_button_output = [["Output  ", attr[1]["R"][attr[0]]]]
        self.R_i_minus_1_button.clicked.connect(lambda: self.zeigeBits([self.R_i_minus_1_button,R_i_minus_1_button_output]))
        expansion_button_output = [["Input   ",attr[1]["R"][attr[0]]],["Output  ", attr[1]["Expansion"][attr[0]]]]
        self.expansion_button.clicked.connect(lambda: self.zeigeBits([self.expansion_button, expansion_button_output], "E"))
        xor_button_output = [["Input E ", attr[1]["Expansion"][attr[0]]],
                      ["Input k ", attr[1]["key"][attr[0]]],
                      ["Output  ", attr[1]["f_xor"][attr[0]]]]
        self.xor_button.clicked.connect(lambda: self.zeigeBits([self.xor_button,xor_button_output]))
        k_i_button_output = [["Output  ", attr[1]["key"][attr[0]]]]
        self.k_i_button.clicked.connect(lambda: self.zeigeBits([self.k_i_button, k_i_button_output]))
        s_button_1_output = self.erzeugeSBoxOutput(attr, 0)
        self.s_button_1.clicked.connect(lambda: self.zeigeBits([self.s_button_1, s_button_1_output], "S_1"))
        s_button_2_output = self.erzeugeSBoxOutput(attr, 1)
        self.s_button_2.clicked.connect(lambda: self.zeigeBits([self.s_button_2, s_button_2_output], "S_2"))
        s_button_3_output = self.erzeugeSBoxOutput(attr, 2)
        self.s_button_3.clicked.connect(lambda: self.zeigeBits([self.s_button_3, s_button_3_output], "S_3"))
        s_button_4_output = self.erzeugeSBoxOutput(attr, 3)
        self.s_button_4.clicked.connect(lambda: self.zeigeBits([self.s_button_4, s_button_4_output], "S_4"))
        s_button_5_output = self.erzeugeSBoxOutput(attr, 4)
        self.s_button_5.clicked.connect(lambda: self.zeigeBits([self.s_button_5, s_button_5_output], "S_5"))
        s_button_6_output = self.erzeugeSBoxOutput(attr, 5)
        self.s_button_6.clicked.connect(lambda: self.zeigeBits([self.s_button_6, s_button_6_output], "S_6"))
        s_button_7_output = self.erzeugeSBoxOutput(attr, 6)
        self.s_button_7.clicked.connect(lambda: self.zeigeBits([self.s_button_7, s_button_7_output], "S_7"))
        s_button_8_output = self.erzeugeSBoxOutput(attr, 7)
        self.s_button_8.clicked.connect(lambda: self.zeigeBits([self.s_button_8, s_button_8_output], "S_8"))
        permutation_button_output = [["Input   ", attr[1]["f_32_bit"][attr[0]]], ["Output  ", attr[1]["f_permutation"][attr[0]]]]
        self.permutation_button.clicked.connect(lambda: self.zeigeBits([self.permutation_button, permutation_button_output], "P"))
        self.information_f_groupbox.clicked.connect(lambda: self.zeigeBits([self.information_f_groupbox, "123"]))

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
        self.information_f_groupbox.show()

    def erzeugeSBoxOutput(self, attr, s_index):
        re = [
            ["Input   ", attr[1]["f_s_boxen"][attr[0]][s_index][0]],
            ["Zeile "+str(attr[1]["f_s_boxen"][attr[0]][s_index][1][1]).zfill(2), attr[1]["f_s_boxen"][attr[0]][s_index][1][2]],
            ["Spalt "+str(attr[1]["f_s_boxen"][attr[0]][s_index][1][3]).zfill(2), attr[1]["f_s_boxen"][attr[0]][s_index][1][4]],
            ["S-Wert  ",[attr[1]["f_s_boxen"][attr[0]][s_index][1][5]]],
            ["Output  ", attr[1]["f_s_boxen"][attr[0]][s_index][1][0]]
        ]
        return re