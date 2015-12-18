import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import Qt
import ctypes
import random
from Interfaces.Uniforme import *
"""
Clase que ejecuta la interfaz de la Distribución Uniforme
"""
class Uniforme(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.btnCalcular.setEnabled(False)
		self.ui.btnGenerar.clicked.connect(self.CalcularUniforme)
		self.ui.btnCalcular.clicked.connect(self.Calcular)
		self.ui.btnEliminaFila.clicked.connect(self.EliminarFilas)

	"""
	Método que calcula la distribución uniforme cuando se generar números aleatorios automaticamente
	cuando no se generar números aleatorios automaticamente solo ingresa las filas de la tabla
	"""
	def CalcularUniforme(self):
		a = self.ui.txtNumA.value()
		b = self.ui.txtNumB.value()
		evento = self.ui.txtEvento.value()
		fila = 0
		if a > 0 and b > 0:
			pregunta = QMessageBox.question(self,"Mensaje","¿Desea generar automaticamente números aleatorios?", QMessageBox.Yes | QMessageBox.No)
			if pregunta == QMessageBox.Yes:
				while fila < evento:
					aleatorio = round(random.random(), 4)
					uniforme = round(a + (b-a) * aleatorio, 4)
					self.ui.tablaUniforme.insertRow(fila)
					valorEvento = QTableWidgetItem(str(fila+1))
					valorAleatorio = QTableWidgetItem(str(aleatorio))
					valorUniforme = QTableWidgetItem(str(uniforme))
					self.ui.tablaUniforme.setItem(fila, 0, valorEvento)
					self.ui.tablaUniforme.setItem(fila, 1, valorAleatorio)
					self.ui.tablaUniforme.setItem(fila, 2, valorUniforme)
					fila += 1
			else:
				if evento > 0:
					self.ui.btnCalcular.setEnabled(True)
					while fila < evento:
						self.ui.tablaUniforme.insertRow(fila)
						valorEvento = QTableWidgetItem(str(fila+1))
						valorAleatorio = QTableWidgetItem(str('0.00'))
						self.ui.tablaUniforme.setItem(fila, 0, valorEvento)
						self.ui.tablaUniforme.setItem(fila, 1, valorAleatorio)
						fila += 1
				else:
					QMessageBox.warning(self, "Error", "Ingrese un número de evento mayor a 0", QMessageBox.Ok)
		else:
			QMessageBox.warning(self, "Error", "Ingrese valores para A y B mayores a 0", QMessageBox.Ok)


	"""Método que calcula la distribución uniforme cuando no se generar números aleatorios automaticamente"""
	def Calcular(self):
		a = self.ui.txtNumA.value()
		b = self.ui.txtNumB.value()
		evento = self.ui.txtEvento.value()
		fila = 0
		if a > 0 and b > 0:
			while fila < evento:
				aleatorio = float(self.ui.tablaUniforme.item(fila, 1).text())
				uniforme = round(a + (b-a) * aleatorio, 4)
				valorUniforme = QTableWidgetItem(str(uniforme))
				self.ui.tablaUniforme.setItem(fila, 2, valorUniforme)
				fila += 1
		else:
			QMessageBox.warning(self, "Error", "Ingrese valores para A y B mayores a 0", QMessageBox.Ok)


	"""Método que limpia los campos y la tabla"""
	def EliminarFilas(self):
		self.ui.btnCalcular.setEnabled(False)
		self.ui.txtNumA.setValue(0)
		self.ui.txtNumB.setValue(0)
		self.ui.txtEvento.setValue(0)
		fila = self.ui.tablaUniforme.selectionModel().selectedRows()
		index = []
		for i in fila:
			index.append(i.row())
		index.sort(reverse = True)
		for i in index:
			self.ui.tablaUniforme.removeRow(i)