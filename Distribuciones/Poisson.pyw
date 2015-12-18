import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import Qt
import ctypes
import random
from Interfaces.Poisson import *
"""
Clase que ejecuta la interfaz de la Distribución Poisson
"""
class Poisson(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.btnCalcular1.clicked.connect(self.Poisson)
		self.ui.btnCalcular2.clicked.connect(self.PoissonAcumulado)
		self.ui.btnEliminaFila.clicked.connect(self.EliminarFilas)

	"""Método que calcula el factorial de un número"""
	def Factorial(self, x):
		fac = 1
		if x == 0:
			return fac
		else:
			for i in range(x):
				fac *= i+1
			return fac

	"""Método que calcula la distribución poisson acumulado"""
	def PoissonAcumulado(self):
		e = 2.71828
		evento, media = self.ui.txtEvento.value(), self.ui.txtMedia.value()
		fila = 0
		if evento > 0 and media > 0:
			while fila < evento:
				poisson = ((media**fila)*(e**(-media)))/self.Factorial(fila)
				porcentual = poisson * 100
				self.ui.tablaMetodo.insertRow(fila)
				x = QTableWidgetItem(str(fila))
				probabilidad = QTableWidgetItem(str(poisson))
				porcen = QTableWidgetItem(str(porcentual))
				nada = QTableWidgetItem(str(""))
				self.ui.tablaMetodo.setItem(fila, 0, x)
				self.ui.tablaMetodo.setItem(fila, 1, probabilidad)
				self.ui.tablaMetodo.setItem(fila, 2, porcen)
				self.ui.tablaMetodo.setItem(fila, 3, nada)
				fila += 1
		else:
			QMessageBox.warning(self, "Error", "Ingrese una media de ocurrencia y \n un número de eventos mayores a 0")


	"""Método que calcula la distribución no acumulado"""
	def Poisson(self):
		e = 2.71828
		evento, x, media, combo = self.ui.txtEvento.value(), self.ui.txtNumero.value(), self.ui.txtMedia.value(), self.ui.combo.currentText()
		media = float(media)
		acumulador, resultado, poisson, porcentual, fila = 0,0,0,0,0
		factorial = 1
		if evento > 0 and media > 0 and x > 0:
			if combo == "=":
				for i in range(x):
					factorial *= (i+1)
				poisson = round(((media**x)*(e**(-media)))/factorial, 6)
				porcentual = round(poisson * 100, 2)
				self.ui.txtResultado.setText(str(poisson))
			elif combo == ">":
				for i in range(x-1):
					for j in range(i):
					 	factorial *= (j+1)
					poisson = round(((media**i)*(e**(-media)))/factorial, 6)
					acumulador += poisson
				resultado = round(1 - acumulador, 6)
				porcentual = round(resultado * 100, 2)
				self.ui.txtResultado.setText(str(resultado))
			elif combo == ">=":
				for i in range(x):
					for j in range(i):
					 	factorial *= (j+1)
					poisson = round(((media**i)*(e**(-media)))/factorial, 6)
					acumulador += poisson
				resultado = round(1 - acumulador, 6)
				porcentual = round(resultado * 100, 2)
				self.ui.txtResultado.setText(str(resultado))
			elif combo == "<":
				for i in range(x):
					for j in range(i):
					 	factorial *= (j+1)
					poisson = round(((media**i)*(e**(-media)))/factorial, 6)
					acumulador += poisson
				resultado = round(acumulador, 6)
				porcentual = round(resultado * 100, 2)
				self.ui.txtResultado.setText(str(resultado))
			else:
				for i in range(x+1):
					for j in range(i):
					 	factorial *= (j+1)
					poisson = round(((media**i)*(e**(-media)))/factorial, 6)
					acumulador += poisson
				resultado = round(acumulador, 6)
				porcentual = round(resultado * 100, 2)
				self.ui.txtResultado.setText(str(resultado))
		else:
			QMessageBox.warning(self, "Error", "Ingrese una media de ocurrencia, \n un número de eventos y \n un número de ocurrencia mayores a 0")

	"""Método que limpia los campos y la tabla"""
	def EliminarFilas(self):
		self.ui.txtMedia.setValue(0.00)
		self.ui.txtNumero.setValue(0)
		self.ui.txtEvento.setValue(0)
		self.ui.txtResultado.setText("")
		fila = self.ui.tablaMetodo.selectionModel().selectedRows()
		index = []
		for i in fila:
			index.append(i.row())
		index.sort(reverse = True)
		for i in index:
			self.ui.tablaMetodo.removeRow(i)
