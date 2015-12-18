import sys
from PyQt5.QtWidgets import QMessageBox, QDialog, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import Qt
import ctypes
from Interfaces.SuavizamientoExponencial import *
"""
Clase que ejecuta la interfaz del Suavizamiento Exponencial
"""
class SuavizamientoExponencial(QDialog):
	def __init__(self):
		QDialog.__init__(self)#Se inicia el objeto QDialog
		self.ui = Ui_Dialog()#Se crea un objeto de la interfaz SuavizamientoExponencial.py
		self.ui.setupUi(self)#Llamar al método setupUi de la interfaz
		self.ui.btnCalcular.setEnabled(False)
		self.ui.btnGenerar.clicked.connect(self.IngresarValores)
		self.ui.btnCalcular.clicked.connect(self.CalcularSuavizamiento)
		self.ui.btnEliminarFilas.clicked.connect(self.LimpiarCampos)

	"""Método que ingresa valores a la tabla"""
	def IngresarValores(self):
		#se obtiene los valores que se ingresan en las cajas de texto
		evento = self.ui.txtEvento.value()
		alfa = self.ui.txtAlfa.value()
		fila = 0
		if evento > 0 and (alfa > 0 and alfa < 1):#Se verifica se se hayan ingresado valores mayores a 0
			self.ui.btnCalcular.setEnabled(True)
			while fila < evento:
				self.ui.tablaSuavizamiento.insertRow(fila)
				t = QTableWidgetItem(str(fila+1))
				yt = QTableWidgetItem("0.00")
				self.ui.tablaSuavizamiento.setItem(fila , 0 , t)
				self.ui.tablaSuavizamiento.setItem(fila, 1, yt)
				fila += 1
		else:
			#Mensaje de Error al no pasar la condición
			QMessageBox.warning(self, "Error", "El número de eventos debe ser mayor a 0 \n y Alfa debe ser un valor entre 0 y 1", QMessageBox.Ok)

	"""Método para calcular el suavizamiento exponencial"""
	def CalcularSuavizamiento(self):
		alfa = self.ui.txtAlfa.value()
		evento = self.ui.txtEvento.value()
		fila = 0
		if evento > 0 and (alfa > 0 and alfa < 1):
			while fila <= evento:
				if fila == 0:
					valorSuavizamiento = QTableWidgetItem(str(fila))
					valorError = QTableWidgetItem(str(fila))
					self.ui.tablaSuavizamiento.setItem(fila, 2, valorSuavizamiento)
					self.ui.tablaSuavizamiento.setItem(fila, 3, valorError)
					fila += 1
				elif fila == 1:
					yt = float(self.ui.tablaSuavizamiento.item(fila-1, 1).text())
					valorSuavizamiento = QTableWidgetItem(str(yt))
					self.ui.tablaSuavizamiento.setItem(fila, 2, valorSuavizamiento)
					ft = float(self.ui.tablaSuavizamiento.item(fila, 2).text())
					valorError = QTableWidgetItem(str(yt-ft))
					self.ui.tablaSuavizamiento.setItem(fila, 3, valorError)
					fila += 1
				else:
					yt = float(self.ui.tablaSuavizamiento.item(fila-1, 1).text())
					ft = float(self.ui.tablaSuavizamiento.item(fila-1, 2).text())
					suavizamiento = round(alfa * yt + (1 - alfa) * ft, 2)
					error = round(yt - ft, 2)
					valorSuavizamiento = QTableWidgetItem(str(suavizamiento))
					valorError = QTableWidgetItem(str(error))
					self.ui.tablaSuavizamiento.setItem(fila, 2, valorSuavizamiento)
					self.ui.tablaSuavizamiento.setItem(fila-1, 3, valorError)
					fila += 1
		else:
			QMessageBox.warning(self, "Error", "El número de eventos debe ser mayor a 0 \n y Alfa debe ser un valor entre 0 y 1", QMessageBox.Ok)

	"""Método que limpia los campos y la tabla"""
	def LimpiarCampos(self):
		self.ui.btnCalcular.setEnabled(False)
		self.ui.txtAlfa.setValue(0.00)
		self.ui.txtEvento.setValue(0)
		fila = self.ui.tablaSuavizamiento.selectionModel().selectedRows()
		index = []
		for i in fila:
			index.append(i.row())
		index.sort(reverse = True)
		for i in index:
			self.ui.tablaSuavizamiento.removeRow(i)