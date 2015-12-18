import sys
from PyQt5.QtWidgets import QMessageBox, QDialog,QApplication,QTableWidget, QTableWidgetItem
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import uic
import random
import numpy
from Interfaces.Normal import *
"""
Clase que ejecuta la interfaz de la Distribución Normal
"""
class Normal(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.btnCalcular.setEnabled(False)
		self.ui.btnIngresar.clicked.connect(self.CalcularNormal)
		self.ui.btnCalcular.clicked.connect(self.Calcular)
		self.ui.btnEliminarFilas.clicked.connect(self.LimpiarCampos)

	def FormulaDesviacion(self, z, des):
		exp = (numpy.power(z,2))/2
		desviacion =(1/numpy.sqrt(2*numpy.pi))*numpy.exp(-exp)
		return round(desviacion, 4)

	"""
	Método que calcula la distribución normal cuando se generar números aleatorios automaticamente
	cuando no se generar números aleatorios automaticamente solo ingresa las filas de la tabla
	"""
	def CalcularNormal(self):
		media = self.ui.txtMedia.value()
		desviacion = self.ui.txtDesviacion.value()
		evento = self.ui.txtEvento.value()
		fila = 0
		acumulador = 0
		if (media > 0 and media < 1) and desviacion > 0 and evento > 0:
			pregunta = QMessageBox.question(self,"Mensaje","¿Desea generar automaticamente números aleatorios?", QMessageBox.Yes | QMessageBox.No)
			if pregunta == QMessageBox.Yes:
				while fila < evento:
					aleatorio = round(random.random(), 2)
					z = round((aleatorio - media)/desviacion, 3)
					calcularDesviacion = self.FormulaDesviacion(z, desviacion)
					acumulador += calcularDesviacion
					self.ui.tablaNormal.insertRow(fila)
					valorEvento = QTableWidgetItem(str(fila+1))
					valorAleatorio = QTableWidgetItem(str(aleatorio))
					valorProb = QTableWidgetItem(str(z))
					valorDist = QTableWidgetItem(str(calcularDesviacion))
					valorAcumulador = QTableWidgetItem(str(acumulador))
					self.ui.tablaNormal.setItem(fila, 0, valorEvento)
					self.ui.tablaNormal.setItem(fila, 1, valorAleatorio)
					self.ui.tablaNormal.setItem(fila, 2, valorProb)
					self.ui.tablaNormal.setItem(fila, 3, valorDist)
					self.ui.tablaNormal.setItem(fila, 4, valorAcumulador)
					fila += 1
			else:
				if evento > 0:
					self.ui.btnCalcular.setEnabled(True)
					while fila < evento:
						self.ui.tablaNormal.insertRow(fila)
						valorEvento = QTableWidgetItem(str(fila+1))
						valorAleaotrio = QTableWidgetItem("0.00")
						self.ui.tablaNormal.setItem(fila, 0, valorEvento)
						self.ui.tablaNormal.setItem(fila, 1, valorAleaotrio)
						fila += 1
				else:
					QMessageBox.warning(self, "Error", "Debe ingresar valores mayores a 0", QMessageBox.Ok)
		else:
			QMessageBox.warning(self, "Error", "Debe ingresar valores mayores a 0 y una media entre 0 y 1", QMessageBox.Ok)

	"""Método que calcula la distribución normal cuando no se generar números aleatorios automaticamente"""
	def Calcular(self):
		media = self.ui.txtMedia.value()
		desviacion = self.ui.txtDesviacion.value()
		evento = self.ui.txtEvento.value()
		fila = 0
		if media > 0 and desviacion > 0:
			while fila < evento:
				aleatorio = float(self.ui.tablaNormal.item(fila, 1).text())
				z = round((aleatorio - media)/desviacion, 3)
				calcularDesviacion = self.FormulaDesviacion(z, desviacion)
				valorProb = QTableWidgetItem(str(z))
				valorDist = QTableWidgetItem(str(calcularDesviacion))
				self.ui.tablaNormal.setItem(fila, 2, valorProb)
				self.ui.tablaNormal.setItem(fila, 3, valorDist)
				fila += 1

	"""Método que limpia los campos y la tabla"""
	def LimpiarCampos(self):
		self.ui.btnCalcular.setEnabled(False)
		self.ui.txtMedia.setValue(0.00)
		self.ui.txtDesviacion.setValue(0)
		self.ui.txtEvento.setValue(0)
		fila = self.ui.tablaNormal.selectionModel().selectedRows()
		index = []
		for i in fila:
			index.append(i.row())
		index.sort(reverse = True)
		for i in index:
			self.ui.tablaNormal.removeRow(i)