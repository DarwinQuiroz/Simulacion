# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuavizamientoExponencial.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(669, 321)
        self.btnGenerar = QtWidgets.QPushButton(Dialog)
        self.btnGenerar.setGeometry(QtCore.QRect(480, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnGenerar.setFont(font)
        self.btnGenerar.setObjectName("btnGenerar")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 431, 301))
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
        self.tablaSuavizamiento = QtWidgets.QTableWidget(self.layoutWidget)
        self.tablaSuavizamiento.setObjectName("tablaSuavizamiento")
        self.tablaSuavizamiento.setColumnCount(4)
        self.tablaSuavizamiento.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaSuavizamiento.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaSuavizamiento.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaSuavizamiento.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaSuavizamiento.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tablaSuavizamiento, 1, 0, 1, 1)
        self.btnCalcular = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnCalcular.setFont(font)
        self.btnCalcular.setObjectName("btnCalcular")
        self.gridLayout.addWidget(self.btnCalcular, 2, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(470, 70, 141, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.txtAlfa = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtAlfa.setFont(font)
        self.txtAlfa.setObjectName("txtAlfa")
        self.gridLayout_2.addWidget(self.txtAlfa, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtEvento = QtWidgets.QSpinBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtEvento.setFont(font)
        self.txtEvento.setObjectName("txtEvento")
        self.gridLayout_2.addWidget(self.txtEvento, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.txtAlfa, self.txtEvento)
        Dialog.setTabOrder(self.txtEvento, self.btnGenerar)
        Dialog.setTabOrder(self.btnGenerar, self.btnCalcular)
        Dialog.setTabOrder(self.btnCalcular, self.btnEliminarFilas)
        Dialog.setTabOrder(self.btnEliminarFilas, self.tablaSuavizamiento)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Suavizamiento Exponencial"))
        self.btnGenerar.setText(_translate("Dialog", "Ingresar Valores"))
        self.btnEliminarFilas.setText(_translate("Dialog", "Limpiar Campos"))
        item = self.tablaSuavizamiento.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "t"))
        item = self.tablaSuavizamiento.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Yt"))
        item = self.tablaSuavizamiento.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Ft"))
        item = self.tablaSuavizamiento.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Yt - Ft"))
        self.btnCalcular.setText(_translate("Dialog", "Calcular"))
        self.label.setText(_translate("Dialog", "Alfa α:"))
        self.label_2.setText(_translate("Dialog", "Eventos:"))

