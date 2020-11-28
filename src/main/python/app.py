import os,sys
import selectport
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

class App(object):
	def __init__(self):
		super().__init__()
		self.list_of_window = list()
		port_settings = selectport.SelectPort()
		self.list_of_window.append(port_settings)
		port_settings.show()