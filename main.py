# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_new.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Bilder
import runde
import inside_f
import transformation
import DES_Generator
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1349, 835)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ausgabeArr = {}
        self.hauptFensterTeiler = QtWidgets.QWidget(MainWindow)
        self.hauptFensterTeiler.setMinimumSize(QtCore.QSize(1100, 720))
        self.hauptFensterTeiler.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.hauptFensterTeiler.setObjectName("hauptFensterTeiler")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.hauptFensterTeiler)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.scrollAusgabe = QtWidgets.QScrollArea(self.hauptFensterTeiler)
        self.scrollAusgabe.hide()
        self.scrollAusgabe.setMinimumSize(QtCore.QSize(825, 0))
        self.scrollAusgabe.setLineWidth(0)
        self.scrollAusgabe.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollAusgabe.setWidgetResizable(True)
        self.scrollAusgabe.setObjectName("scrollAusgabe")
        self.horizontalLayout.addWidget(self.scrollAusgabe)

        self.scrollEingabe = QtWidgets.QScrollArea(self.hauptFensterTeiler)
        self.scrollEingabe.setMinimumSize(QtCore.QSize(530, 0))
        self.scrollEingabe.setWidgetResizable(True)
        self.scrollEingabe.setObjectName("scrollEingabe")

        self.listeScrollEingabe = QtWidgets.QWidget()
        self.listeScrollEingabe.setGeometry(QtCore.QRect(0, 0, 498, 815))
        self.listeScrollEingabe.setObjectName("listeScrollEingabe")


        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.listeScrollEingabe)
        self.verticalLayout_4.setAlignment(QtCore.Qt.AlignBottom)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.informationKontroll = QtWidgets.QGroupBox(self.listeScrollEingabe)
        self.informationKontroll.setObjectName("informationKontroll")
        self.informationKontroll.hide()

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.informationKontroll)
        self.verticalLayout_3.setAlignment(QtCore.Qt.AlignTop)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.label_information = QtWidgets.QLabel(self.informationKontroll)
        self.label_information.setObjectName("label_information")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_information.setFont(font)

        self.verticalLayout_3.addWidget(self.label_information)

        self.widget_platzhalter = QtWidgets.QWidget(self.informationKontroll)
        self.widget_platzhalter.setObjectName("widget_platzhalter")
        self.verticalLayout_3.addWidget(self.widget_platzhalter)

        self.verticalLayout_4.addWidget(self.informationKontroll)


        self.eingabeKontrolle = QtWidgets.QGroupBox(self.listeScrollEingabe)
        self.eingabeKontrolle.setMaximumSize(QtCore.QSize(16777215, 200))
        self.eingabeKontrolle.setMinimumSize(QtCore.QSize(16777215, 200))
        self.eingabeKontrolle.setObjectName("eingabeKontrolle")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.eingabeKontrolle)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_klartext = QtWidgets.QLabel(self.eingabeKontrolle)
        self.label_klartext.setObjectName("label_klartext")
        self.verticalLayout.addWidget(self.label_klartext)

        self.klartext_eingabe = QtWidgets.QPlainTextEdit(self.eingabeKontrolle)
        self.klartext_eingabe.setPlainText("1111111111111111111111111111111111111111111111111111111111111111")
        self.klartext_eingabe.setObjectName("klartext_eingabe")

        self.verticalLayout.addWidget(self.klartext_eingabe)
        self.label_schluessel = QtWidgets.QLabel(self.eingabeKontrolle)
        self.label_schluessel.setObjectName("label_schluessel")
        self.verticalLayout.addWidget(self.label_schluessel)

        self.schluessel_eingabe = QtWidgets.QPlainTextEdit(self.eingabeKontrolle)
        self.schluessel_eingabe.setPlainText("1111111111111111111111111111111111111111111111111111111111111111")
        self.schluessel_eingabe.setObjectName("schluessel_eingabe")

        self.verticalLayout.addWidget(self.schluessel_eingabe)

        self.enterInput = QtWidgets.QPushButton(self.eingabeKontrolle)
        self.enterInput.setObjectName("enterInput")

        self.verticalLayout.addWidget(self.enterInput)
        self.verticalLayout_4.addWidget(self.eingabeKontrolle)



        self.scrollEingabe.setWidget(self.listeScrollEingabe)
        self.horizontalLayout.addWidget(self.scrollEingabe)
        MainWindow.setCentralWidget(self.hauptFensterTeiler)

        self.enterInput.clicked.connect(self.verschlussel)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DES Generator"))


        self.label_klartext.setText(_translate("MainWindow", "Klartext (64 Bit)"))
        self.label_schluessel.setText(_translate("MainWindow", "Schlüssel (64 Bit)"))
        self.enterInput.setText(_translate("MainWindow", "Verschlüsseln"))
        self.informationKontroll.setTitle(_translate("MainWindow", "Information"))

    def verschlussel(self):
        self.scrollAusgabe.hide()
        self.informationKontroll.hide()
        self.verticalLayout_3.removeWidget(self.widget_platzhalter)

        self.widget_platzhalter.close()
        self.widget_platzhalter = QtWidgets.QWidget(self.informationKontroll)
        self.widget_platzhalter.setObjectName("widget_platzhalter")

        self.verticalLayout_3.addWidget(self.widget_platzhalter)
        self.widget_platzhalter.update()
        if len(self.schluessel_eingabe.toPlainText())==64 and len(self.klartext_eingabe.toPlainText())==64:
            x = [int(n) for n in self.klartext_eingabe.toPlainText()]
            k = [int(n) for n in self.schluessel_eingabe.toPlainText()]
            DES_Generator.DES_encrypt(x,k)
            self.ausgabeArr = DES_Generator.ausgabeArr
            self.ausgabeProd()
            self.scrollAusgabe.show()
        else:
            self.info_ausgabe("<div style=color:red>Bitte jeweils für Schlüssel und Klartext 64-Bit lange Strings eingeben</div>")

    def zeigeBits(self, bits, sub_tabelle=None):
        self.verticalLayout_3.removeWidget(self.widget_platzhalter)
        self.widget_platzhalter.close()

        self.widget_platzhalter = QtWidgets.QWidget()
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

        self.ausgabe1 = QtWidgets.QLabel(self.widget_platzhalter)
        self.ausgabe1.setObjectName("ausgabe1")
        self.ausgabe1.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.ausgabe1.setText(ausgabe_string)

        font = QtGui.QFont(QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont))
        self.ausgabe1.setFont(font)
        self.widget_platzhalter.setMinimumSize(QtCore.QSize(530, 950))
        self.verticalLayout_3.addWidget(self.widget_platzhalter)
        self.widget_platzhalter.update()
        self.info_ausgabe(bits[0].text())

    def zeigeTransformation(self, bits):

        self.verticalLayout_3.removeWidget(self.widget_platzhalter)
        self.widget_platzhalter.close()
        self.widget_platzhalter = transformation.Transformation([bits[1],self.ausgabeArr])
        self.widget_platzhalter.setMinimumSize(QtCore.QSize(530, 950))
        self.verticalLayout_3.addWidget(self.widget_platzhalter)
        self.widget_platzhalter.update()
        self.info_ausgabe(bits[0].text())

    def zeigeFinside(self, bits):

        self.verticalLayout_3.removeWidget(self.widget_platzhalter)
        self.widget_platzhalter.close()
        self.widget_platzhalter = inside_f.Inside_f([bits[1],self.ausgabeArr])
        self.widget_platzhalter.setMinimumSize(QtCore.QSize(530, 950))
        self.verticalLayout_3.addWidget(self.widget_platzhalter)
        self.widget_platzhalter.update()
        self.info_ausgabe(bits[0].text())

    def info_ausgabe(self,information):
        self.scrollEingabe.verticalScrollBar().setValue(0)
        self.label_information.setText(information)
        self.informationKontroll.show()

    def ausgabeProd(self):
        self.listeScrollAusgabe = QtWidgets.QWidget()
        self.listeScrollAusgabe.setGeometry(QtCore.QRect(0, 0, 823, 815))
        self.listeScrollAusgabe.setObjectName("listeScrollAusgabe")
        #self.listeScrollEingabe.setContentsMargins(0,0,0,0)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.listeScrollAusgabe)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.top = QtWidgets.QWidget(self.listeScrollAusgabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())

        self.top.setSizePolicy(sizePolicy)
        self.top.setMinimumSize(QtCore.QSize(800, 225))
        self.top.setMaximumSize(QtCore.QSize(800, 225))
        self.top.setStyleSheet("background-image: url(:/Bild/img/top.png);")
        self.top.setObjectName("top")

        self.eingang_ip_button = QtWidgets.QPushButton(self.top)
        self.eingang_ip_button.setGeometry(QtCore.QRect(114, 110, 174, 59))
        self.eingang_ip_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.eingang_ip_button.setObjectName("eingang_ip_button")

        self.klartext_button = QtWidgets.QPushButton(self.top)
        self.klartext_button.setGeometry(QtCore.QRect(131, 24, 141, 31))
        self.klartext_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.klartext_button.setObjectName("klartext_button")

        self.schlussel_k_button = QtWidgets.QPushButton(self.top)
        self.schlussel_k_button.setGeometry(QtCore.QRect(533, 23, 141, 31))
        self.schlussel_k_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.schlussel_k_button.setObjectName("schlussel_k_button")

        self.pc_1_button = QtWidgets.QPushButton(self.top)
        self.pc_1_button.setGeometry(QtCore.QRect(531, 110, 141, 31))
        self.pc_1_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.pc_1_button.setObjectName("pc_1_button")

        self.verticalLayout_2.addWidget(self.top)
        ###
        for i in range(16):
            item = runde.Runde([i],main=self)
            item.setMinimumSize(QtCore.QSize(800, 201))
            self.verticalLayout_2.addWidget(item)
        ###

        self.bottom = QtWidgets.QWidget(self.listeScrollAusgabe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottom.sizePolicy().hasHeightForWidth())

        self.bottom.setSizePolicy(sizePolicy)
        self.bottom.setMinimumSize(QtCore.QSize(800, 295))
        self.bottom.setMaximumSize(QtCore.QSize(800, 295))
        self.bottom.setStyleSheet("background-image: url(:/Bild/img/bottom.png);")
        self.bottom.setObjectName("bottom")

        self.ausgang_ip_1_button = QtWidgets.QPushButton(self.bottom)
        self.ausgang_ip_1_button.setGeometry(QtCore.QRect(113, 115, 174, 60))
        self.ausgang_ip_1_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.ausgang_ip_1_button.setObjectName("ausgang_ip_1_button")

        self.chiffrat_y_button = QtWidgets.QPushButton(self.bottom)
        self.chiffrat_y_button.setGeometry(QtCore.QRect(113, 230, 174, 60))
        self.chiffrat_y_button.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.chiffrat_y_button.setObjectName("chiffrat_y_button")

        self.links_button_letzer = QtWidgets.QPushButton(self.bottom)
        self.links_button_letzer.setGeometry(QtCore.QRect(100, 0, 100, 31))
        self.links_button_letzer.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.links_button_letzer.setObjectName("links_button_letzer")

        self.rechts_button_letzer = QtWidgets.QPushButton(self.bottom)
        self.rechts_button_letzer.setGeometry(QtCore.QRect(198, 0, 100, 31))
        self.rechts_button_letzer.setStyleSheet("background-image: url(:/Bild/img/btnbg.png);background-color:#000000")
        self.rechts_button_letzer.setObjectName("rechts_button_letzer")

        self.verticalLayout_2.addWidget(self.bottom)

        self.scrollAusgabe.setWidget(self.listeScrollAusgabe)

        _translate = QtCore.QCoreApplication.translate
        self.eingang_ip_button.setText(_translate("MainWindow", "Eingang IP"))
        self.klartext_button.setText(_translate("MainWindow", "Klartext x"))
        self.schlussel_k_button.setText(_translate("MainWindow", "Schlüssel k"))
        self.pc_1_button.setText(_translate("MainWindow", "PC-1"))


        self.ausgang_ip_1_button.setText(_translate("MainWindow", "Ausgang IP_1"))
        self.chiffrat_y_button.setText(_translate("MainWindow", "Chiffrat\ny=DES_k(x)"))
        self.links_button_letzer.setText(_translate("MainWindow", "L 16"))
        self.rechts_button_letzer.setText(_translate("MainWindow", "R 16"))
        self.eingabeKontrolle.setTitle(_translate("MainWindow", "Eingaben"))


        eingang_ip_output = [["Input   ", self.ausgabeArr['Klartext']],["Output  ", self.ausgabeArr['Eingang_IP']]]
        self.eingang_ip_button.clicked.connect(lambda: self.zeigeBits([self.eingang_ip_button,eingang_ip_output],"IP"))

        klartext_output = [["Output  ", self.ausgabeArr['Klartext']]]
        self.klartext_button.clicked.connect(lambda: self.zeigeBits([self.klartext_button,klartext_output]))

        schlussel_k_output = [["Output  ", self.ausgabeArr['Schlussel']]]
        self.schlussel_k_button.clicked.connect(lambda: self.zeigeBits([self.schlussel_k_button,schlussel_k_output]))

        pc_1_output = [["Input   ", self.ausgabeArr['Schlussel']],["Output  ", self.ausgabeArr['PC-1']]]
        self.pc_1_button.clicked.connect(lambda: self.zeigeBits([self.pc_1_button, pc_1_output],"PC_1"))

        ausgang_ip_1_output = [["Input   ", self.ausgabeArr['ausgangspermutation_input']], ["Output  ", self.ausgabeArr['Ausgang_IP_1']]]
        self.ausgang_ip_1_button.clicked.connect(lambda: self.zeigeBits([self.ausgang_ip_1_button,ausgang_ip_1_output],"IP_1"))

        chiffrat_y_output = [["Input   ", self.ausgabeArr['Ausgang_IP_1']]]
        self.chiffrat_y_button.clicked.connect(lambda: self.zeigeBits([self.chiffrat_y_button, chiffrat_y_output]))

        links_button_letzer_output = [["Output  ", self.ausgabeArr['L'][16]]]
        self.links_button_letzer.clicked.connect(lambda: self.zeigeBits([self.links_button_letzer,links_button_letzer_output]))

        rechts_button_letzer_output = [["Output  ", self.ausgabeArr['R'][16]]]
        self.rechts_button_letzer.clicked.connect(lambda: self.zeigeBits([self.rechts_button_letzer,rechts_button_letzer_output]))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
