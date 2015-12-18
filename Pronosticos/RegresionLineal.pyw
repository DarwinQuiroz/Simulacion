import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import Qt
import ctypes
from Interfaces.RegresionLineal import *
"""
Clase que ejecuta la interfaz de la Regresion Lineal
"""
class RegresionLineal(QDialog):
	def __init__(self):
		QDialog.__init__(self)#Se inicia el objeto QDialog
		self.ui = Ui_Dialog()#Se crea un objeto de la interfaz RegresionLineal.py
		self.ui.setupUi(self)#Llamar al método setupUi de la interfaz
		self.ui.btnCalcular.setEnabled(False)
		self.ui.btnIngresar.clicked.connect(self.IgresarTabla)
		self.ui.btnCalcular.clicked.connect(self.CalcularRegresion)
		self.ui.btnEliminarFilas.clicked.connect(self.LimpiarCampos)

	"""Método para ingresar valores a la tabla"""
	def IgresarTabla(self):
		evento = self.ui.txtEvento.value()
		fila = 0
		if evento > 0:
			self.ui.btnCalcular.setEnabled(True)
			while fila < evento:
				self.ui.tablaRegresion.insertRow(fila)
				valorX = QTableWidgetItem("0")
				valorY = QTableWidgetItem("0")
				self.ui.tablaRegresion.setItem(fila, 0, valorX)
				self.ui.tablaRegresion.setItem(fila, 1, valorY)
				fila += 1
		else:
			QMessageBox.warning(self, "Error", "Debe ingresar un valor mayor a 0", QMessageBox.Ok)

	"""Método que calcula la regresión lineal"""
	def CalcularRegresion(self):
		#se obtiene los valores que se ingresan en las cajas de texto
		evento = self.ui.txtEvento.value()
		valorX = int(self.ui.txtValorX.text())
		fila = 0
		sumaX, sumaY, sumaX2, sumaXy, sumaY2 = 0, 0, 0, 0, 0
		#a, b, y = 0,0,0
		if valorX > 0:#se verifica que se haya ingresa un valor mayor a 0
			while fila < evento:
				x = int(self.ui.tablaRegresion.item(fila, 0).text())
				y = int(self.ui.tablaRegresion.item(fila, 1).text())
				sumaX += x
				sumaY += y
				sumaX2 += x**2
				sumaXy += x*y
				sumaY2 += y**2
				valorX2 = QTableWidgetItem(str(x**2))
				valorXy = QTableWidgetItem(str(x*y))
				valorY2 = QTableWidgetItem(str(y**2))
				self.ui.tablaRegresion.setItem(fila, 2, valorX2)
				self.ui.tablaRegresion.setItem(fila, 3, valorXy)
				self.ui.tablaRegresion.setItem(fila, 4, valorY2)
				fila += 1
			while fila == evento:
				self.ui.tablaRegresion.insertRow(fila)
				valorSumaX = QTableWidgetItem(str(sumaX))
				valorSumaY = QTableWidgetItem(str(sumaY))
				valorSumaX2 = QTableWidgetItem(str(sumaX2))
				valorSumaXy = QTableWidgetItem(str(sumaXy))
				valorSumaY2 = QTableWidgetItem(str(sumaY2))
				self.ui.tablaRegresion.setItem(fila, 0, valorSumaX)
				self.ui.tablaRegresion.setItem(fila, 1, valorSumaY)
				self.ui.tablaRegresion.setItem(fila, 2, valorSumaX2)
				self.ui.tablaRegresion.setItem(fila, 3, valorSumaXy)
				self.ui.tablaRegresion.setItem(fila, 4, valorSumaY2)
				fila += 1
			a = self.FormulaA(evento, sumaX, sumaY, sumaX2, sumaXy)
			b = self.FormulaB(evento, sumaX, sumaY, sumaX2, sumaXy)
			y = self.FormmulaY(valorX, a, b)
			a = str(a)
			b = str(b)
			y = str(y)
			QMessageBox.information(self, "Resultados", "Valor de a: "+a+"\n Valor de b: "+b+"\n Resultado y: "+y, QMessageBox.Ok)
		else:
			#Mensaje de Error al no pasar la condición
			QMessageBox.warning(self, "Error", "Debe ingresar el valor de X", QMessageBox.Ok)

	#a0 = (Σy)(Σx**2)-(Σx)(Σxy) / NΣx**2-(Σx)**2
	def FormulaA(self,eventos, sumaX, sumaY, sumaX2, sumaXy):
		return round(((sumaY*sumaX2) - (sumaX*sumaXy)) / (eventos*sumaX2 - (sumaX)**2),3)
	#a1 = NΣxy-(Σx)(Σy) / NΣx**2-(Σx)**2
	def FormulaB(self,eventos, sumaX, sumaY, sumaX2, sumaXy):
		return round(((eventos*sumaXy) - (sumaX*sumaY)) / (eventos*sumaX2 - (sumaX)**2), 3)
	#y = a0 + a1(X)
	def FormmulaY(self, x, a, b):
		return round(a + (b*x), 2)


	"""Método que limpia los campos y la tabla"""
	def LimpiarCampos(self):
		self.ui.btnCalcular.setEnabled(False)
		self.ui.txtEvento.setValue(0)
		self.ui.txtValorX.setText("0")
		fila = self.ui.tablaRegresion.selectionModel().selectedRows()
		index = []
		for i in fila:
			index.append(i.row())
		index.sort(reverse = True)
		for i in index:
			self.ui.tablaRegresion.removeRow(i)