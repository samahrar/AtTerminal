from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QWidget, QApplication, QFileDialog, QMessageBox
from serialutils import get_list_ports, get_list_device
import sys,os,json
from datetime import datetime
from serialwindow import SerialWindow
import config_utils

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(539, 483)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        Settings.setStyleSheet("font: 11pt \"Monospace\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(211, 215, 207);")
        self.centralwidget = QtWidgets.QWidget(Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setObjectName("Start")
        self.gridLayout.addWidget(self.Start, 16, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.LogName = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LogName.sizePolicy().hasHeightForWidth())
        self.LogName.setSizePolicy(sizePolicy)
        self.LogName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.LogName.setText("")
        self.LogName.setObjectName("LogName")
        self.horizontalLayout_2.addWidget(self.LogName)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.Baudrate = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Baudrate.sizePolicy().hasHeightForWidth())
        self.Baudrate.setSizePolicy(sizePolicy)
        self.Baudrate.setStyleSheet("selection-background-color: rgb(114, 159, 207);")
        self.Baudrate.setObjectName("Baudrate")
        self.Baudrate.addItem("")
        self.Baudrate.addItem("")
        self.Baudrate.addItem("")
        self.Baudrate.addItem("")
        self.Baudrate.addItem("")
        self.horizontalLayout_9.addWidget(self.Baudrate)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.fontComboBox_2 = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox_2.setObjectName("fontComboBox_2")
        self.horizontalLayout_8.addWidget(self.fontComboBox_2)
        self.FontSize = QtWidgets.QSpinBox(self.centralwidget)
        self.FontSize.setObjectName("FontSize")
        self.FontSize.setMinimum(6)
        self.FontSize.setMaximum(18)
        self.FontSize.setValue(11)
        self.horizontalLayout_8.addWidget(self.FontSize)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.ReadMode = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ReadMode.sizePolicy().hasHeightForWidth())
        self.ReadMode.setSizePolicy(sizePolicy)
        self.ReadMode.setStyleSheet("selection-background-color: rgb(114, 159, 207);")
        self.ReadMode.setObjectName("ReadMode")
        self.ReadMode.addItem("")
        self.horizontalLayout_3.addWidget(self.ReadMode)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.PullMode = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PullMode.sizePolicy().hasHeightForWidth())
        self.PullMode.setSizePolicy(sizePolicy)
        self.PullMode.setStyleSheet("selection-background-color: rgb(114, 159, 207);")
        self.PullMode.setObjectName("PullMode")
        self.PullMode.addItem("")
        self.horizontalLayout_6.addWidget(self.PullMode)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 11, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 10, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 12, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LogDir = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LogDir.sizePolicy().hasHeightForWidth())
        self.LogDir.setSizePolicy(sizePolicy)
        self.LogDir.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.LogDir.setText("")
        self.LogDir.setObjectName("LogDir")
        self.horizontalLayout.addWidget(self.LogDir)
        self.ChangeDir = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChangeDir.sizePolicy().hasHeightForWidth())
        self.ChangeDir.setSizePolicy(sizePolicy)
        self.ChangeDir.setObjectName("ChangeDir")
        self.horizontalLayout.addWidget(self.ChangeDir)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout.addWidget(self.line_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_10.addWidget(self.checkBox)
        self.LogRotation = QtWidgets.QCheckBox(self.centralwidget)
        self.LogRotation.setObjectName("LogRotation")
        self.LogRotation.setChecked(True)
        self.horizontalLayout_10.addWidget(self.LogRotation)
        self.LogSize = QtWidgets.QSpinBox(self.centralwidget)
        self.LogSize.setObjectName("LogSize")
        self.LogSize.setMaximum(1000)
        self.LogSize.setMinimum(1)
        self.LogSize.setValue(10)
        self.horizontalLayout_10.addWidget(self.LogSize)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.gridLayout.addLayout(self.verticalLayout, 13, 0, 1, 1)
        self.UpdatePortList = QtWidgets.QPushButton(self.centralwidget)
        self.UpdatePortList.setObjectName("UpdatePortList")
        self.gridLayout.addWidget(self.UpdatePortList, 1, 0, 1, 1)
        self.ComPort = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComPort.sizePolicy().hasHeightForWidth())
        self.ComPort.setSizePolicy(sizePolicy)
        self.ComPort.setStyleSheet("selection-background-color: rgb(114, 159, 207);")
        self.ComPort.setObjectName("ComPort")
        self.gridLayout.addWidget(self.ComPort, 4, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 7, 0, 1, 1)
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setObjectName("Exit")
        self.gridLayout.addWidget(self.Exit, 17, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 15, 0, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout)
        Settings.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Settings)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 541, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.menuFile.setFont(font)
        self.menuFile.setStyleSheet("selection-background-color: rgb(114, 159, 207);")
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        Settings.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Settings)
        self.statusbar.setObjectName("statusbar")
        Settings.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(Settings)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(Settings)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave_Config = QtWidgets.QAction(Settings)
        self.actionSave_Config.setObjectName("actionSave_Config")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuOptions.addAction(self.actionSave_Config)
        self.menuOptions.setStyleSheet("selection-background-color: rgb(114, 159, 207);")
        self.menuOptions.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "At Terminal"))
        self.Start.setText(_translate("Settings", "Start"))
        self.label_6.setText(_translate("Settings", "Log Name"))
        self.label_9.setText(_translate("Settings", "Baud rate"))
        self.Baudrate.setItemText(0, _translate("Settings", "115200"))
        self.Baudrate.setItemText(1, _translate("Settings", "57600"))
        self.Baudrate.setItemText(2, _translate("Settings", "19200"))
        self.Baudrate.setItemText(3, _translate("Settings", "9600"))
        self.Baudrate.setItemText(4, _translate("Settings", "4800"))
        self.label_8.setText(_translate("Settings", "Mode"))
        self.ReadMode.setItemText(0, _translate("Settings", "ASCII"))
        self.label.setText(_translate("Settings", "Pulling Mode"))
        self.PullMode.setItemText(0, _translate("Settings", "New Line"))
        self.label_2.setText(_translate("Settings", "Serial Port"))
        self.ChangeDir.setText(_translate("Settings", "Change Log Dir"))
        self.checkBox_2.setText(_translate("Settings", "Night Mode"))
        self.checkBox.setText(_translate("Settings", "Log Enabled"))
        self.LogRotation.setText(_translate("Settings", "Log Rotation"))
        self.label_4.setText(_translate("Settings", "MB"))
        self.UpdatePortList.setText(_translate("Settings", "Update port list"))
        self.Exit.setText(_translate("Settings", "Exit"))
        self.menuFile.setTitle(_translate("Settings", "File"))
        self.menuOptions.setTitle(_translate("Settings", "Options"))
        self.actionExit.setText(_translate("Settings", "Exit"))
        self.actionSave_Config.setText(_translate("Settings", "Save Config"))
        self.actionAbout.setText(_translate("Settings", "About"))

class SelectPort(QMainWindow):
    """docstring for SelectPort"""
    def __init__(self):
        super().__init__()
        self.version="0.1"

        self.list_of_window = list()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.setup_options()
        #Draw the box
        self.show()

        #Properties
        self.properties = dict()
        # Exit button
        self.ui.actionExit.triggered.connect(self.exit_app)
        # About button
        self.ui.actionAbout.triggered.connect(self.show_about)
        #Save config:
        self.ui.actionSave_Config.triggered.connect(self.show_config)
        #handle Update port list
        self.ui.UpdatePortList.clicked.connect(self.update_port_list)
        #handle change directory
        self.ui.ChangeDir.clicked.connect(self.change_log_dir)
        #handle Start
        self.properties = self.ui.Start.clicked.connect(self.start)
        #handle exit
        self.ui.Exit.clicked.connect(self.exit_app)


    def exit_app(self):
        """
        Exit
        """
        self.close()

    def setup_options(self):
        # setup the list of COMPorts
        self.set_listofcomports(get_list_ports())
        
        # Handel Config
        try:
            config_file = config_utils.read_config()    
        except Exception as e:
            print(e)
            config_file = False

        if config_file:
            # set up log bacse on config
            if 'log_dir' in config_file and config_file['log_dir']:
                if not os.path.exists(config_file['log_dir']):
                    os.makedirs(config_file['log_dir'])
                self.ui.LogDir.setText(config_file['log_dir'])
            else:
                self.ui.LogDir.setText(self.make_log_dir())
            # set up baudrate base on config
            if 'baudrate' in config_file and config_file['baudrate']:
                self.ui.Baudrate.setCurrentIndex(config_utils.get_baudrate_index(config_file['baudrate']))

            # set up font base on config
            if 'font' in config_file and config_file['font']:
                self.ui.fontComboBox_2.setCurrentIndex(self.ui.fontComboBox_2.findText(config_file['font']))
            if 'font_size' in config_file and config_file['font_size']:
                self.ui.FontSize.setValue(config_file['font_size'])
            # setup nightmode and log base on config
            # night mode:
            if 'nightmode' in config_file:
                if not config_file['nightmode']:
                    self.ui.checkBox_2.setChecked(False)
            # config setting
            if 'logenabled' in config_file:
                if not config_file['logenabled']:
                    self.ui.checkBox.setChecked(False)

            if 'log_rotaion_enabled' in config_file:
                if not config_file['log_rotaion_enabled']:
                    self.ui.LogRotation.setChecked(False)

            if 'log_rotation_size' in config_file:
                if isinstance(config_file['log_rotation_size'],int):
                    self.ui.LogSize.setValue(config_file['log_rotation_size'])

        else:
            self.ui.LogDir.setText(self.make_log_dir())
            self.ui.Baudrate.setCurrentIndex(0)
            self.ui.checkBox_2.setChecked(True)
            self.ui.checkBox.setChecked(True)
        
        # Setup defaul log name
        self.ui.LogName.setText(self.make_log_name())

    def update_port_list(self):
        """
        Update list of comports
        """
        self.ui.ComPort.clear()
        self.set_listofcomports(get_list_ports())
        return


    def set_listofcomports(self,list_of_ports_string):
        """
        Set the list of coports inside ComPort
        """
        for port in list_of_ports_string:
            self.ui.ComPort.addItem(port)

    def get_comport_selected(self):
        """
        Get from drop box selected Comport
        find name of comport by looking though list of devices
        """
        if self.ui.ComPort.currentText():
            for name in self.ui.ComPort.currentText().split():
                if name in get_list_device():
                    return name
                else:
                    return None
        else:
            print("NONE")
            return None

    def change_log_dir(self):
        """
        Set log directory
        """
        path_to_dir = QFileDialog.getExistingDirectory()
        self.ui.LogDir.setText(path_to_dir)

    def get_log_dir(self):
        """
        Get log directory set in text box LogDir
        if emtpy return None
        """
        if self.ui.LogDir.text():
            return self.ui.LogDir.text()
        else:
            return None

    def get_log_name(self):
        """
        Get Log name
        if empty return None
        """
        if self.ui.LogName.text():
            return self.ui.LogName.text()
        else:
            return None

    def get_baud_rate(self):
        """
        Get configured baud-rate
        """
        return self.ui.Baudrate.currentText()

    def get_mode(self):
        """
        get mode ASCII or Hex-Binary
        """
        return self.ui.ReadMode.currentText()

    def get_pull_mode(self):
        """
        Get pulling mode
        """
        return self.ui.PullMode.currentText()

    def get_font(self):
        """
        """
        return self.ui.fontComboBox_2.currentText()

    def get_font_size(self):
        """
        """
        return self.ui.FontSize.value()
    
    def get_night_mode(self):
        """
        """
        return self.ui.checkBox_2.isChecked()
    def get_logenabled(self):
        """
        """
        return self.ui.checkBox.isChecked()

    def get_logrotation(self):
        """
        """
        return self.ui.LogRotation.isChecked()

    def get_logrotationsize(self):
        """
        """
        return self.ui.LogSize.value()

    def make_log_dir(self):
        #Make current working dir a log director
        log_dir = os.path.join(os.getcwd(),"log")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return log_dir

    def make_log_name(self):
        #use pc time stamp to make a defualt log name
        return str(datetime.now().strftime('%Y%m%d_%H%M%S'))

    def start(self):
        """
        Generate dictonary of properties
        """
        properties_dict = dict()
        comport = self.get_comport_selected()
        properties_dict.update({"comport":comport})
        log_dir = self.get_log_dir()
        properties_dict.update({"log_dir":log_dir})
        log_name = self.get_log_name()
        properties_dict.update({"log_name":log_name})
        baudrate = self.get_baud_rate()
        properties_dict.update({"baudrate":baudrate})
        mode = self.get_mode()
        properties_dict.update({"mode":mode})
        pullmode = self.get_pull_mode()
        properties_dict.update({"pullmode":pullmode})
        nightmode = self.get_night_mode()
        properties_dict.update({"nightmode":nightmode})
        logenabled = self.get_logenabled()
        properties_dict.update({"logenabled":logenabled})
        font_selected=self.get_font()
        properties_dict.update({"font":font_selected})
        font_size=self.get_font_size()
        properties_dict.update({"font_size":font_size})
        log_rotaion_enabled=self.get_logrotation()
        properties_dict.update({"log_roation":log_rotaion_enabled})
        log_rotation_size = self.get_logrotationsize()
        properties_dict.update({"log_rotation_size":log_rotation_size})
        

        #Next Window
        serial = SerialWindow(properties_dict)
        self.list_of_window.append(serial)
        serial.show()
        self.close()
        
        return properties_dict

    def show_about(self):
        msg = QMessageBox()
        msg.setWindowTitle("About AT Terminal")
        msg.setText("AT Terminal Created by Sam Ahrar\nVersion{0}".format(self.version))
        x = msg.exec_()

    def show_config(self):
        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.RestoreDefaults | QMessageBox.Cancel)
        if config_utils.read_config():
            string_to_show="Current Settings Saved:\n\n"+str(config_utils.read_config()).replace(",","\n")
            msg.setDetailedText("Configuration File:\n{0}\n{1}".format(
            config_utils.get_path_config_file(),string_to_show))
        else:
            msg.setDetailedText("No Config file found.\nSave Current config to start.")

        current_logpath = self.get_log_dir()
        current_baudrate = self.get_baud_rate()
        current_font = self.get_font()
        current_font_size = str(self.get_font_size())
        if self.get_night_mode():
            current_nightmode = "On"
        else:
            current_nightmode = "Off"
        if self.get_logenabled():
            current_logsetting = "On"
        else:
            current_logsetting = "Off"
        if self.get_logrotation():
            current_logrotation = "On"
            log_rotation_size = self.get_logrotationsize()
        else:
            current_logrotation = "off"
            log_rotation_size = "-"
        msg.setWindowTitle("Current Configuration:")
        msg.setText("Log Path: {0}\nBaudrate: {1}\nFont: {2}-{5}\nNight Mode: {3}\nLogging: {4}\nLog Rotation: {6} at {7} MB"
        .format(current_logpath,current_baudrate,current_font,current_nightmode,current_logsetting,current_font_size,
            current_logrotation,log_rotation_size))
        #msg.buttonClicked.connect(save_config_handler)
        msg.buttonClicked.connect(self.save_config_handler)
        retval = msg.exec_()
        
        #x = msg.exec_()
    def save_config_handler(self,action):
        if "Cancel" in action.text():
            return
        elif "OK" in action.text():
            print("Save config")
            properties_dict = dict()
            log_dir = self.get_log_dir()
            properties_dict.update({"log_dir":log_dir})
            baudrate = self.get_baud_rate()
            properties_dict.update({"baudrate":baudrate})
            font_selected=self.get_font()
            properties_dict.update({"font":font_selected})
            font_size=self.get_font_size()
            properties_dict.update({"font_size":font_size})
            nightmode = self.get_night_mode()
            properties_dict.update({"nightmode":nightmode})
            logenabled = self.get_logenabled()
            properties_dict.update({"logenabled":logenabled})

            log_rotaion_enabled=self.get_logrotation()
            properties_dict.update({"log_roation":log_rotaion_enabled})
            log_rotation_size = self.get_logrotationsize()
            properties_dict.update({"log_rotation_size":log_rotation_size})
            
            config_utils.save_confg(properties_dict)
        elif "Restore Defaults" in action.text():
            config_utils.restore_defaults()
            self.setup_options()
        else:
            print(action.text())
            pass

