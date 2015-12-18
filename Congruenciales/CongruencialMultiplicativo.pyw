import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import Qt
import ctypes
import numpy, math
from Interfaces.Multiplicativo import *
"""
Clase que ejecuta la interfaz del Método Congruencial Multiplicativo
"""
class CongruencialMultiplicativo(QDialog):#Hereda de QDialog(Costructor de ventanas)
	#Método Constructor de la Clase CongruencialMultiplicativo
	def __init__(self):
		QDialog.__init__(self)#Se inicia el objeto QDialog
		self.ui = Ui_Dialog()#Se crea un objeto de la interfaz Multiplicativo.py
		self.ui.setupUi(self)#Llamar al método setupUi de la interfaz
		#Botón de la interfaz que llama al método CalcularMultiplicativo
		self.ui.btnCalcular.clicked.connect(self.CalcularMultiplicativo)
		#Botón de la interfaz que llama al método Limpiarcampos
		self.ui.btnEliminarFilas.clicked.connect(self.LimpiarCampos)

	"""Método que calcula Congruencial Multiplicativo"""
	def CalcularMultiplicativo(self):
		#se obtiene los valores que se ingresan en las cajas de texto
		a = self.ui.txtA.value()
		x0 = self.ui.txtXn.value()
		m = self.ui.txtM.value()
		n = self.ui.txtN.value()
		fila = 0#Inicilaización de variable
		if a>0 and x0>0 and m>0 and n>0:#Se verifica se se hayan ingresado valores mayores a 0
			if m>a and m>x0:#Se verifica que el valor del Módulo m sea mayor que x0,a

				#Ciclo while que va de 0 a n para poder ingresar los valores calculado a la tabla
				while fila <= n:
					#Cálculos
					aXn = round(a * x0, 4)
					aXnMod = round(numpy.mod(aXn, m), 4)
					aleatorio = round(aXnMod/m, 4)
					self.ui.tablaMultiplicativo.insertRow(fila)#Se ingresa un fila a la tabla
					#Se ingresan los valores calculados en la tabla
					valorN = QTableWidgetItem(str(fila))
					valorXn = QTableWidgetItem(str(x0))
					valorAXn = QTableWidgetItem(str(aXn))
					valoraXnMod = QTableWidgetItem(str(aXnMod))
					valorAleatorio = QTableWidgetItem(str(aleatorio))
					self.ui.tablaMultiplicativo.setItem(fila, 0, valorN)
					self.ui.tablaMultiplicativo.setItem(fila, 1, valorXn)
					self.ui.tablaMultiplicativo.setItem(fila, 2, valorAXn)
					self.ui.tablaMultiplicativo.setItem(fila, 3, valoraXnMod)
					self.ui.tablaMultiplicativo.setItem(fila, 4, valorAleatorio)
					x0 = aXnMod
					fila += 1
			else:
				#Mensaje de Error al no pasar la segunda condición
				QMessageBox.warning(self, "Error", "El módulo debe ser mayor que a", QMessageBox.Ok)
		else:
			#Mensaje de Error al no pasar la primera condición
			QMessageBox.warning(self, "Error", "Debe ingresar valores mayores a 0", QMessageBox.Ok)

	"""Método que limpia los campos y la tabla"""
	def LimpiarCampos(self):
		self.ui.txtA.setValue(0)
		self.ui.txtXn.setValue(0)
		self.ui.txtM.setValue(0)
		self.ui.txtN.setValue(0)
		fila = self.ui.tablaMultiplicativo.selectionModel().selectedRows()
		index = []
		for i in fila:
			index.append(i.row())
		index.sort(reverse = True)
		for i in index:
			self.ui.tablaMultiplicativo.removeRow(i)