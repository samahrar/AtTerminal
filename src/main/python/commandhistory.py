from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QWidget, QApplication, QFileDialog, QMessageBox

class Ui_CommandHistory(object):
    def setupUi(self, CommandHistory):
        CommandHistory.setObjectName("CommandHistory")
        CommandHistory.resize(690, 629)
        self.centralwidget = QtWidgets.QWidget(CommandHistory)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.CommandHistoryTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.CommandHistoryTxt.setObjectName("CommandHistoryTxt")
        self.verticalLayout.addWidget(self.CommandHistoryTxt)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        CommandHistory.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CommandHistory)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 22))
        self.menubar.setObjectName("menubar")
        CommandHistory.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CommandHistory)
        self.statusbar.setObjectName("statusbar")
        CommandHistory.setStatusBar(self.statusbar)

        self.retranslateUi(CommandHistory)
        QtCore.QMetaObject.connectSlotsByName(CommandHistory)

    def retranslateUi(self, CommandHistory):
        _translate = QtCore.QCoreApplication.translate
        CommandHistory.setWindowTitle(_translate("CommandHistory", "Command History"))
    
    def setnight_mode(self,CommandHistory):
        CommandHistory.setStyleSheet("font: 11pt \"Monospace\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(61, 58, 58);")
        self.CommandHistoryTxt.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")

class CommandHistory(QMainWindow):
    """docstring for """
    def __init__(self, commandlist,nightmode):
        super(CommandHistory, self).__init__()
        self.ui = Ui_CommandHistory()
        self.ui.setupUi(self)
        # Setup variables
        self.commandlist = commandlist

        if nightmode:
            self.ui.setnight_mode(self)
        #Fill out text box Show the box
        self.fill_out_command_box(self.commandlist)
        self.show()


    def fill_out_command_box(self,commandlist):
        for i in commandlist:
            self.ui.CommandHistoryTxt.append(i)