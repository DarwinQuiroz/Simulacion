# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 255)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(100, 130, 121, 23))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setObjectName("btnAceptar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cbbDistribuciones = QtWidgets.QComboBox(self.centralwidget)
        self.cbbDistribuciones.setGeometry(QtCore.QRect(70, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(14)
        self.cbbDistribuciones.setFont(font)
        self.cbbDistribuciones.setEditable(False)
        self.cbbDistribuciones.setObjectName("cbbDistribuciones")
        self.cbbDistribuciones.addItem("")
        self.cbbDistribuciones.addItem("")
        self.cbbDistribuciones.addItem("")
        self.cbbDistribuciones.addItem("")
        self.cbbDistribuciones.addItem("")
        self.cbbDistribuciones.addItem("")
        self.cbbDistribuciones.addItem("")
        self.cbbDistribuciones.addItem("")
        self.cbbDistribuciones.addItem("")
        self.cbbDistribuciones.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menú"))
        self.btnAceptar.setText(_translate("MainWindow", "ACEPTAR"))
        self.label.setText(_translate("MainWindow", "ELIJA UNA DISTRIBUCION O METODO"))
        self.cbbDistribuciones.setItemText(0, _translate("MainWindow", "Binomial"))
        self.cbbDistribuciones.setItemText(1, _translate("MainWindow", "Exponencial"))
        self.cbbDistribuciones.setItemText(2, _translate("MainWindow", "Normal"))
        self.cbbDistribuciones.setItemText(3, _translate("MainWindow", "Poisson"))
        self.cbbDistribuciones.setItemText(4, _translate("MainWindow", "Uniforme"))
        self.cbbDistribuciones.setItemText(5, _translate("MainWindow", "Congruencial Mixto"))
        self.cbbDistribuciones.setItemText(6, _translate("MainWindow", "Congruencial Multiplicativo"))
        self.cbbDistribuciones.setItemText(7, _translate("MainWindow", "Promedio Móvil"))
        self.cbbDistribuciones.setItemText(8, _translate("MainWindow", "Suavizamiento Exponencial"))
        self.cbbDistribuciones.setItemText(9, _translate("MainWindow", "Regresión Lineal"))
        self.label_2.setText(_translate("MainWindow", "Autor: Darwin Quiroz"))

