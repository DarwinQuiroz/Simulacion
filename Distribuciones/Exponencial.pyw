import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import Qt
import ctypes
import random, math
from Interfaces.Exponencial import *
"""
Clase que ejecuta la interfaz de la Distribución Exponencial
"""
class Exponencial(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.btnCalcular.setEnabled(False)
		self.ui.btnGenerar.clicked.connect(self.CalcularExponencial)
		self.ui.btnCalcular.clicked.connect(self.Calcular)
		self.ui.btnEliminaFila.clicked.connect(self.EliminarFilas)


	"""Método que calcula la distribucion exponencial cuando no se generar números aleatorios automaticamente"""
	def Calcular(self):
		#Se obtiene los valores que se ingresan en las cajas de texto
		lam = self.ui.txtMedia.value()
		x = self.ui.txtNumero.value()
		fila = 0
		if lam > 0:#Se verifica se se haya ingresado un valor mayor a 0
			while fila < x:
				aleatorio = float(self.ui.tablaExponencial.item(fila, 1).text())
				varExpo = round((-1/lam)*math.log(aleatorio), 4)
				varExpo2 = round((-1/lam)*math.log(1-aleatorio), 4)
				exponencial = QTableWidgetItem(str(varExpo))
				exponencial2 = QTableWidgetItem(str(varExpo2))
				self.ui.tablaExponencial.setItem(fila, 2, exponencial)
				self.ui.tablaExponencial.setItem(fila, 3, exponencial2)
				fila += 1
		else:
			#Mesaje de error al no pasar la condición if
			QMessageBox.warning(self, "Error", "Ingrese un número de ocurrencia mayor a 0", QMessageBox.Ok)

	"""
	Método que calcula la distribución exponencial cuando se generar números aleatorios automaticamente
	cuando no se generar números aleatorios automaticamente solo ingresa las filas de la tabla
	"""
	def CalcularExponencial(self):
		lam = self.ui.txtMedia.value()
		x = self.ui.txtNumero.value()
		fila = 0
		if lam > 0 and x > 0:
			pregunta = QMessageBox.question(self, "Mensaje", "¿Desea generar automaticamente números aleatorios?", QMessageBox.Yes | QMessageBox.No)
			if pregunta == QMessageBox.Yes:
				while fila <= x:
					aleatorio = round(random.random(), 3)
					varExpo = round((-1/lam)*math.log(aleatorio), 4)
					varExpo2 = round((-1/lam)*math.log(1 - aleatorio), 4)
					self.ui.tablaExponencial.insertRow(fila)
					valorX = QTableWidgetItem(str(fila+1))
					valorAleatorio = QTableWidgetItem(str(aleatorio))
					exponencial = QTableWidgetItem(str(varExpo))
					exponencial2 = QTableWidgetItem(str(varExpo2))
					self.ui.tablaExponencial.setItem(fila, 0, valorX)
					self.ui.tablaExponencial.setItem(fila, 1, valorAleatorio)
					self.ui.tablaExponencial.setItem(fila, 2, exponencial)
					self.ui.tablaExponencial.setItem(fila, 3, exponencial2)
					fila += 1
			else:
				if x > 0:
					while fila < x:
						self.ui.btnCalcular.setEnabled(True)
						self.ui.tablaExponencial.insertRow(fila)
						valorX = QTableWidgetItem(str(fila+1))
						valorAleatorio = QTableWidgetItem('0.00')
						self.ui.tablaExponencial.setItem(fila, 0, valorX)
						self.ui.tablaExponencial.setItem(fila, 1, valorAleatorio)
						fila += 1
				else:
					QMessageBox.warning(self, "Error", "Ingrese un número de ocurrencia mayor a 0", QMessageBox.Ok)
		else:
			QMessageBox.warning(self, "Error", "Ingrese una media de ocurrencia y un número de ocurrencia mayores a 0")


	"""Método que limpia los campos y la tabla"""
	def EliminarFilas(self):
		self.ui.btnCalcular.setEnabled(False)
		self.ui.txtMedia.setValue(0.00)
		self.ui.txtNumero.setValue(0)
		fila = self.ui.tablaExponencial.selectionModel().selectedRows()
		index = []
		for i in fila:
			index.append(i.row())
		index.sort(reverse = True)
		for i in index:
			self.ui.tablaExponencial.removeRow(i)