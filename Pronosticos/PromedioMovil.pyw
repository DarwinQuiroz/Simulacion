import sys
from PyQt5.QtWidgets import QMessageBox, QDialog, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtCore import Qt
import ctypes
from Interfaces.PromedioMovil import *
"""
Clase que ejecuta la interfaz del Promedio Movil
"""
class PromedioMovil(QDialog):
	def __init__(self):
		QDialog.__init__(self)#Se inicia el objeto QDialog
		self.ui = Ui_Dialog()#Se crea un objeto de la interfaz PromedioMovil.py
		self.ui.setupUi(self)#Llamar al método setupUi de la interfaz
		self.ui.btnCalcular.setEnabled(False)
		self.ui.btnIngresar.clicked.connect(self.IgresarValores)
		self.ui.btnEliminaFila.clicked.connect(self.LimpiarCampos)
		self.ui.btnCalcular.clicked.connect(self.CalcularMovil)

	"""Método para ingresar valores a la tabla"""
	def IgresarValores(self):
		#se obtiene los valores que se ingresan en las cajas de texto
		evento = self.ui.txtEvento.value()
		movil = self.ui.txtMovil.value()
		fila = 0
		if evento > 0 and movil > 0:#Se verifica se se hayan ingresado valores mayores a 0
			self.ui.btnCalcular.setEnabled(True)
			while fila < evento:
				self.ui.tablaProMovil.insertRow(fila)
				valorEvento = QTableWidgetItem(str(fila+1))
				valorAccion = QTableWidgetItem("0")
				self.ui.tablaProMovil.setItem(fila, 0, valorEvento)
				self.ui.tablaProMovil.setItem(fila, 1, valorAccion)
				fila += 1
		else:
			#Mensaje de Error al no pasar la condición
			QMessageBox.warning(self, "Error", "Debe ingresar valores mayores a 0", QMessageBox.Ok)


	"""Método para calcular el promedio móvil"""
	def CalcularMovil(self):
		evento = self.ui.txtEvento.value()
		movil = self.ui.txtMovil.value()
		fila = movil
		if evento > 0 and movil > 0:
			divisor = movil
			for i in range(movil-1, evento-1):
				suma = 0
				for j in range(movil-1, movil-(divisor+1), -1):
					suma += float(self.ui.tablaProMovil.item(j, 1).text())
				promedioMovil = round(suma/divisor, 2)
				valorPromedio = QTableWidgetItem(str(promedioMovil))
				incremento = movil
				if incremento < evento+1:
					self.ui.tablaProMovil.setItem(incremento, 2, valorPromedio)
					accion = float(self.ui.tablaProMovil.item(incremento, 1).text())
					diferencia = round(accion - promedioMovil, 2)
					valorDiferencia = QTableWidgetItem(str(diferencia))
					self.ui.tablaProMovil.setItem(incremento, 3, valorDiferencia)
					movil += 1
				else:
					self.ui.tablaProMovil.setItem(incremento, 2, promedioMovil)
					accion = float(self.ui.tablaProMovil.item(incremento, 1).text())
					diferencia = accion - promedioMovil
					valorDiferencia = QTableWidgetItem(str(diferencia))
					self.ui.tablaProMovil.setItem(incremento, 3, valorDiferencia)
		else:
			QMessageBox.warning(self, "Error", "Debe ingresar valores mayores a 0", QMessageBox.Ok)


	"""Método que limpia los campos y la tabla"""
	def LimpiarCampos(self):
		self.ui.btnCalcular.setEnabled(False)
		self.ui.txtEvento.setValue(0)
		self.ui.txtMovil.setValue(0)
		fila = self.ui.tablaProMovil.selectionModel().selectedRows()
		index = []
		for i in fila:
			index.append(i.row())
		index.sort(reverse = True)
		for i in index:
			self.ui.tablaProMovil.removeRow(i)