# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Poisson.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(647, 482)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 331, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnEliminaFila = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnEliminaFila.setFont(font)
        self.btnEliminaFila.setObjectName("btnEliminaFila")
        self.gridLayout_4.addWidget(self.btnEliminaFila, 0, 0, 1, 1)
        self.tablaMetodo = QtWidgets.QTableWidget(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tablaMetodo.setFont(font)
        self.tablaMetodo.setObjectName("tablaMetodo")
        self.tablaMetodo.setColumnCount(3)
        self.tablaMetodo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaMetodo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaMetodo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tablaMetodo.setHorizontalHeaderItem(2, item)
        self.gridLayout_4.addWidget(self.tablaMetodo, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(380, 30, 210, 16))
        self.label_2.setObjectName("label_2")
        self.txtMedia = QtWidgets.QDoubleSpinBox(Dialog)
        self.txtMedia.setGeometry(QtCore.QRect(450, 60, 62, 22))
        self.txtMedia.setProperty("showGroupSeparator", False)
        self.txtMedia.setObjectName("txtMedia")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(340, 100, 291, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.txtEvento = QtWidgets.QSpinBox(self.layoutWidget1)
        self.txtEvento.setObjectName("txtEvento")
        self.gridLayout.addWidget(self.txtEvento, 0, 1, 1, 1)
        self.btnCalcular2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.btnCalcular2.setObjectName("btnCalcular2")
        self.gridLayout.addWidget(self.btnCalcular2, 0, 2, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(370, 170, 230, 151))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.combo = QtWidgets.QComboBox(self.layoutWidget2)
        self.combo.setObjectName("combo")
        self.combo.addItem("")
        self.combo.addItem("")
        self.combo.addItem("")
        self.combo.addItem("")
        self.combo.addItem("")
        self.gridLayout_2.addWidget(self.combo, 0, 0, 1, 1)
        self.txtNumero = QtWidgets.QSpinBox(self.layoutWidget2)
        self.txtNumero.setObjectName("txtNumero")
        self.gridLayout_2.addWidget(self.txtNumero, 0, 1, 1, 1)
        self.btnCalcular1 = QtWidgets.QPushButton(self.layoutWidget2)
        self.btnCalcular1.setObjectName("btnCalcular1")
        self.gridLayout_2.addWidget(self.btnCalcular1, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.txtResultado = QtWidgets.QLineEdit(self.layoutWidget2)
        self.txtResultado.setReadOnly(True)
        self.txtResultado.setObjectName("txtResultado")
        self.gridLayout_3.addWidget(self.txtResultado, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.label_2.raise_()
        self.txtMedia.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.txtMedia, self.txtEvento)
        Dialog.setTabOrder(self.txtEvento, self.btnCalcular2)
        Dialog.setTabOrder(self.btnCalcular2, self.combo)
        Dialog.setTabOrder(self.combo, self.txtNumero)
        Dialog.setTabOrder(self.txtNumero, self.btnCalcular1)
        Dialog.setTabOrder(self.btnCalcular1, self.btnEliminaFila)
        Dialog.setTabOrder(self.btnEliminaFila, self.tablaMetodo)
        Dialog.setTabOrder(self.tablaMetodo, self.txtResultado)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Distribución de Poisson"))
        self.btnEliminaFila.setText(_translate("Dialog", "Limpiar Campos"))
        item = self.tablaMetodo.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "X"))
        item = self.tablaMetodo.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "P(X)"))
        item = self.tablaMetodo.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "P(X) %"))
        self.label_2.setText(_translate("Dialog", "Media de Ocurrencias (Lambda):"))
        self.label_3.setText(_translate("Dialog", "Número de Eventos:"))
        self.btnCalcular2.setText(_translate("Dialog", "Generar"))
        self.label.setText(_translate("Dialog", "Número de Ocurrencia (X):"))
        self.combo.setItemText(0, _translate("Dialog", "="))
        self.combo.setItemText(1, _translate("Dialog", ">"))
        self.combo.setItemText(2, _translate("Dialog", "<"))
        self.combo.setItemText(3, _translate("Dialog", ">="))
        self.combo.setItemText(4, _translate("Dialog", "<="))
        self.btnCalcular1.setText(_translate("Dialog", "Calcular"))
        self.label_4.setText(_translate("Dialog", "Resultado:"))
