import sys
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow, QMessageBox, QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import ctypes
from Interfaces.Main import *
from Distribuciones.Poisson import Poisson
from Distribuciones.Exponencial import Exponencial
from Distribuciones.Uniforme import Uniforme
from Distribuciones.Normal import Normal
from Distribuciones.Binomial import Binomial
from Congruenciales.CongruencialMultiplicativo import CongruencialMultiplicativo
from Congruenciales.CongruencialMixto import CongruencialMixto
from Pronosticos.PromedioMovil import PromedioMovil
from Pronosticos.SuavizamientoExponencial import SuavizamientoExponencial
from Pronosticos.RegresionLineal import RegresionLineal
"""
Clase Principal que ejecuta toda la aplicación
"""
class Main(QMainWindow):#Hereda de QMainnWindows(Costructor de ventanas)
	#Método constructor de la clase Main
	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)#Se inicia el objeto QMainWindow
		self.ui = Ui_MainWindow()#Objeto de la intefaz Principal
		self.ui.setupUi(self)#Llamar al método setupUi de la interfaz
		self.ui.btnAceptar.clicked.connect(self.Abrir)#boton de la interfaz que llama al método Abrir
		#Crear la barra de menú
		menu = self.menuBar()
		info = menu.addMenu("&Acerca de...")
		autor = QAction(QIcon(), "&Autor", self)
		autor.setShortcut("Ctrl+a")
		autor.setStatusTip("Autor")
		autor.triggered.connect(self.Mensaje)
		info.addAction(autor)


	def Mensaje(self):
		#Mensaje que muestra la barra de menú
		QMessageBox.information(self, "Información del Autor", "Autor: Darwin Quiroz "+
			"\n Materia: Modelo y Simulación \n"
			+"Profesor: Ing. Jorge Moya \n"
			+"Año Lectivo: 2015 - 2016")


	"""Método para abrir el modelo seleccionado desde el combobox"""
	def Abrir(self):
		combo = self.ui.cbbDistribuciones.currentText()
		if combo == "Poisson":
			#Se abre la interfaz para calcular Distribución de Poisson
			poisson = Poisson()
			poisson.exec_()
		elif combo == "Uniforme":
			#Se abre la interfaz para calcular Distribución Uniforme
			uniforme = Uniforme()
			uniforme.exec_()
		elif combo == "Exponencial":
			#Se abre la interfaz para calcular Distribución Exponencial
			exponencial = Exponencial()
			exponencial.exec_()
		elif combo == "Normal":
			#Se abre la interfaz para calcular Distribución Normal
			normal = Normal()
			normal.exec_()
		elif combo == "Binomial":
			#Se abre la interfaz para calcular Distribución Binomial
			binomial = Binomial()
			binomial.exec_()
		elif combo == "Congruencial Multiplicativo":
			#Se abre la interfaz para calcular Congruencial Multiplicativo
			multiplicativo = CongruencialMultiplicativo()
			multiplicativo.exec_()
		elif combo == "Congruencial Mixto":
			#Se abre la interfaz para calcular Congruencial Mixto
			mixto = CongruencialMixto()
			mixto.exec_()
		elif combo == "Promedio Móvil":
			#Se abre la interfaz para calcular Promedio Móvil
			proMovil = PromedioMovil()
			proMovil.exec_()
		elif combo == "Suavizamiento Exponencial":
			#Se abre la interfaz para calcular Suavizamiento Exponencial
			suavizamiento = SuavizamientoExponencial()
			suavizamiento.exec_()
		else:
			#Se abre la interfaz para calcular Regresión Lineal
			regresion = RegresionLineal()
			regresion.exec_()

if __name__ == '__main__':
	import sys

	app = QApplication(sys.argv)#instacia para iniciar la aplicación
	main = Main()#Objeto de la clase Main
	main.show()#Mostar la ventana
	app.exec_()#Ejecutarla aplicación