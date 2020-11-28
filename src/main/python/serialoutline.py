# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QWidget, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QTimer,Qt
import serial
from datetime import datetime
import sys,os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 904)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("font: 11pt \"Monospace\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SerialStatus = QtWidgets.QLabel(self.tab)
        self.SerialStatus.setObjectName("SerialStatus")
        self.horizontalLayout_2.addWidget(self.SerialStatus)
        self.SuspendSerial = QtWidgets.QPushButton(self.tab)
        self.SuspendSerial.setObjectName("SuspendSerial")
        self.horizontalLayout_2.addWidget(self.SuspendSerial)
        self.FollowLog = QtWidgets.QCheckBox(self.tab)
        self.FollowLog.setObjectName("FollowLog")
        self.horizontalLayout_2.addWidget(self.FollowLog)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.SerialOutput = QtWidgets.QTextBrowser(self.tab)
        self.SerialOutput.setObjectName("SerialOutput")
        self.verticalLayout.addWidget(self.SerialOutput)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.AtCommandLine = QtWidgets.QLineEdit(self.tab)
        self.AtCommandLine.setObjectName("AtCommandLine")
        self.horizontalLayout_4.addWidget(self.AtCommandLine)
        self.SendAt = QtWidgets.QPushButton(self.tab)
        self.SendAt.setObjectName("SendAt")
        self.horizontalLayout_4.addWidget(self.SendAt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.PrevCommand = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(19)
        sizePolicy.setHeightForWidth(self.PrevCommand.sizePolicy().hasHeightForWidth())
        self.PrevCommand.setSizePolicy(sizePolicy)
        self.PrevCommand.setMinimumSize(QtCore.QSize(93, 0))
        self.PrevCommand.setObjectName("PrevCommand")
        self.horizontalLayout_6.addWidget(self.PrevCommand)
        self.PrevSendAt = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PrevSendAt.sizePolicy().hasHeightForWidth())
        self.PrevSendAt.setSizePolicy(sizePolicy)
        self.PrevSendAt.setObjectName("PrevSendAt")
        self.horizontalLayout_6.addWidget(self.PrevSendAt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ClearScreen = QtWidgets.QPushButton(self.tab)
        self.ClearScreen.setObjectName("ClearScreen")
        self.horizontalLayout_5.addWidget(self.ClearScreen)
        self.Exit = QtWidgets.QPushButton(self.tab)
        self.Exit.setObjectName("Exit")
        self.horizontalLayout_5.addWidget(self.Exit)
        self.PrintLogInfo = QtWidgets.QPushButton(self.tab)
        self.PrintLogInfo.setObjectName("PrintLogInfo")
        self.horizontalLayout_5.addWidget(self.PrintLogInfo)
        self.CommandHistory = QtWidgets.QPushButton(self.tab)
        self.CommandHistory.setObjectName("CommandHistory")
        self.horizontalLayout_5.addWidget(self.CommandHistory)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        # To Do add Tab 2 for options
        #self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AT Terminal"))
        self.SerialStatus.setText(_translate("MainWindow", "TextLabel"))
        self.SuspendSerial.setText(_translate("MainWindow", "Close Comport"))
        self.FollowLog.setText(_translate("MainWindow", "Follow Line"))
        self.SendAt.setText(_translate("MainWindow", "Send"))
        self.PrevSendAt.setText(_translate("MainWindow", "Send"))
        self.ClearScreen.setText(_translate("MainWindow", "Clear"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.PrintLogInfo.setText(_translate("MainWindow", "Print Log Info"))
        self.CommandHistory.setText(_translate("MainWindow", "Command History"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Serial Output"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Options"))
  
        
    def set_night_mode(self,MainWindow):
        MainWindow.setStyleSheet("background-color: rgb(61, 58, 58);")
        self.SerialStatus.setStyleSheet("color : green;")
        self.FollowLog.setStyleSheet("QCheckBox"
            "{"
            "color: white;"
            "}"
            "QCheckBox::indicator:unchecked"
            "{"
            "background: red;"
            "}"
            "QCheckBox::indicator:checked"
            "{"
            "background: green;"
            "}"
            )
        self.centralwidget.setStyleSheet("background-color: rgb(46, 52, 54);")
        """
        self.tabWidget.setStyleSheet("font: 12pt \"Monospace\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(61, 58, 58);")"""
        self.tabWidget.setStyleSheet("QTabBar"
                "{"
                "background: gray;"
                "}"
                "QTabBar::tab:!selected"
                "{"
                "background: gray;"
                "}"
                )
        self.SerialOutput.setStyleSheet("background-color: rgb(4, 4, 4);\n"
"color: rgb(255, 255, 255);")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 22))
        self.SuspendSerial.setStyleSheet("QPushButton"
                             "{"
                             "background-color : gray;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}")
        self.SendAt.setStyleSheet("QPushButton"
                             "{"
                             "background-color : gray;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}")
        self.PrevSendAt.setStyleSheet("QPushButton"
                             "{"
                             "background-color : gray;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}")
        self.ClearScreen.setStyleSheet("QPushButton"
                             "{"
                             "background-color : gray;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}")
        self.Exit.setStyleSheet("QPushButton"
                             "{"
                             "background-color : gray;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}")
        self.PrintLogInfo.setStyleSheet("QPushButton"
                             "{"
                             "background-color : gray;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}")
        self.CommandHistory.setStyleSheet("QPushButton"
                             "{"
                             "background-color : gray;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}")
        self.AtCommandLine.setStyleSheet("QLineEdit"
                        "{"
                        "background-color : gray;"
                        "}"
                        "QLineEdit:focus"
                        "{"
                        "background-color : white;"
                        "}")

    def set_font(self,font,nightmode,font_size):
        font = font
        nightmode = nightmode
        font_size = str(font_size)
        if nightmode:
            self.SerialOutput.setStyleSheet("background-color: rgb(4, 4, 4);\n"
"color: rgb(255, 255, 255);\n"
"font: {1}pt \"{0}\";".format(font,font_size))
        else:
            self.SerialOutput.setStyleSheet("font: {1}pt \"{0}\";".format(font,font_size))
"""
    def keyPressEvent(self, e):
        if e.key()  == Qt.Key_Return:
            print(' return')
            self.SerialOutput.moveCursor(QtGui.QTextCursor.End)
        elif e.key() == Qt.Key_Enter:   
            print(' enter')
            self.SerialOutput.moveCursor(QtGui.QTextCursor.End)
"""