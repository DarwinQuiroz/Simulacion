# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mixto.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 468)
        self.btnCalcular = QtWidgets.QPushButton(Dialog)
        self.btnCalcular.setGeometry(QtCore.QRect(230, 430, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnCalcular.setFont(font)
        self.btnCalcular.setObjectName("btnCalcular")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnEliminarFilas = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnEliminarFilas.setFont(font)
        self.btnEliminarFilas.setObjectName("btnEliminarFilas")
        self.gridLayout.addWidget(self.btnEliminarFilas, 0, 0, 1, 1)
        self.tablaMixto = QtWidgets.QTableWidget(self.layoutWidget)
        self.tablaMixto.setObjectName("tablaMixto")
        self.tablaMixto.setColumnCount(5)
        self.tablaMixto.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaMixto.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaMixto.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaMixto.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaMixto.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaMixto.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.tablaMixto, 1, 0, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(170, 280, 181, 141))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.txtA = QtWidgets.QSpinBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtA.setFont(font)
        self.txtA.setObjectName("txtA")
        self.gridLayout_2.addWidget(self.txtA, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtXn = QtWidgets.QSpinBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtXn.setFont(font)
        self.txtXn.setObjectName("txtXn")
        self.gridLayout_2.addWidget(self.txtXn, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.txtM = QtWidgets.QSpinBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtM.setFont(font)
        self.txtM.setObjectName("txtM")
        self.gridLayout_2.addWidget(self.txtM, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.txtC = QtWidgets.QSpinBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtC.setFont(font)
        self.txtC.setObjectName("txtC")
        self.gridLayout_2.addWidget(self.txtC, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.txtN = QtWidgets.QSpinBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtN.setFont(font)
        self.txtN.setObjectName("txtN")
        self.gridLayout_2.addWidget(self.txtN, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Congruencial Mixto"))
        self.btnCalcular.setText(_translate("Dialog", "Calcular"))
        self.btnEliminarFilas.setText(_translate("Dialog", "Limpiar Campos"))
        item = self.tablaMixto.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "n"))
        item = self.tablaMixto.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Xn"))
        item = self.tablaMixto.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "aXn+c"))
        item = self.tablaMixto.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "(aXn+c)Mod(m)"))
        item = self.tablaMixto.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Aleatorio"))
        self.label.setText(_translate("Dialog", "Multiplicador (a):"))
        self.label_2.setText(_translate("Dialog", "Semilla (Xn):"))
        self.label_3.setText(_translate("Dialog", "Módulo (m):"))
        self.label_4.setText(_translate("Dialog", "Constante (c):"))
        self.label_5.setText(_translate("Dialog", "Eventos (n):"))

