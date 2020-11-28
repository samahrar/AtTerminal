from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from app import App
import sys

def main():
	appctxt = ApplicationContext()
	app = QApplication(sys.argv)
	w = App()
	#w.show()
	sys.exit(appctxt.app.exec_())

if __name__ == '__main__':
	main()