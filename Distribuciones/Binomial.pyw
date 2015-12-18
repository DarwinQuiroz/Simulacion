import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import Qt
import ctypes
import numpy
from Interfaces.Binomial import *
"""
Clase que ejecuta la interfaz de la Distribución Binomial
"""
class Binomial(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.btnCalcular.clicked.connect(self.CalcularBinomial)
		self.ui.btnEliminarFilas.clicked.connect(self.LimpiarCampos)

	"""Método que calcula el factorial de un número"""
	def Factorial(self, x):
		fac = 1
		if x == 0:
			return fac
		else:
			for i in range(x):
				fac *= i+1
			return fac

	"""Método que calcula la distribucion Binomial"""
	def CalcularBinomial(self):
		#Se obtiene los valores que se ingresan en las cajas de texto
		exito = self.ui.txtExito.value()
		ensayo = self.ui.txtEnsayo.value()
		probabilidadExito = self.ui.txtProbabilidad.value()
		#Inicializació de variables
		fila = 0
		acumulada = 0
		if exito > 0 and ensayo > 0 and probabilidadExito > 0:#Se verifica se se hayan ingresado valores mayores a 0
			while fila < ensayo:
				n = ensayo - fila
				probabilidad = round ((self.Factorial(ensayo) / (self.Factorial(fila)*self.Factorial(n))) * (numpy.power(probabilidadExito, fila)) * numpy.power((1- probabilidadExito), (ensayo -fila)), 4)
				acumulada += probabilidad
				self.ui.tablaBinomial.insertRow(fila)
				valorEnsayo = QTableWidgetItem(str(fila+1))
				valorProbabilidad = QTableWidgetItem(str(probabilidad))
				valorAcumulada = QTableWidgetItem(str(acumulada))
				self.ui.tablaBinomial.setItem(fila, 0, valorEnsayo)
				self.ui.tablaBinomial.setItem(fila, 1, valorProbabilidad)
				self.ui.tablaBinomial.setItem(fila, 2, valorAcumulada)
				fila += 1
		else:
			#Mesaje de error al no pasar la condición if
			QMessageBox.warning(self, "Error", "Debe Ingresa Valores mayores a 0", QMessageBox.Ok)

	"""Método que limpia los campos y la tabla"""
	def LimpiarCampos(self):
		self.ui.txtExito.setValue(0)
		self.ui.txtEnsayo.setValue(0)
		self.ui.txtProbabilidad.setValue(0.00)
		fila = self.ui.tablaBinomial.selectionModel().selectedRows()
		index = []
		for i in fila:
			index.append(i.row())
		index.sort(reverse = True)
		for i in index:
			self.ui.tablaBinomial.removeRow(i)