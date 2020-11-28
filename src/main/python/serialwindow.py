from serialoutline import QMainWindow,Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QWidget, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QTimer, Qt
import serial
from datetime import datetime
import sys,os
from log_utils import log_files,log_line
from commandhistory import CommandHistory

class SerialWindow(QMainWindow):
    """docstring for """
    def __init__(self, comport_dic):
        super(SerialWindow, self).__init__()
        self.list_of_window = list()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #setup lists
        self.commandlist = list()
        #Setup properties
        self.comport = comport_dic['comport']
        self.log_dir = comport_dic['log_dir']
        self.log_name = comport_dic['log_name']
        self.baudrate = comport_dic['baudrate']
        self.mode = comport_dic['mode']
        self.pullmode = comport_dic['pullmode']
        self.nightmode = comport_dic['nightmode']
        self.logenabled = comport_dic['logenabled']
        self.font = comport_dic['font']
        self.font_size = comport_dic['font_size']
        self.log_roation=comport_dic['log_roation']
        self.log_rotation_size=comport_dic['log_rotation_size']
        if self.nightmode:
            self.ui.set_night_mode(self)

        self.ui.set_font(self.font,self.nightmode,self.font_size)
        #Log file
        if self.logenabled:
            self.log_name = os.path.join(self.log_dir,self.log_name)
            if self.log_roation :
                self.log = log_files(self.log_name,self.log_rotation_size)
            else:
                self.log = log_files(self.log_name)

        #setup timer 10 milisecond timer
        self.uart_timer = QTimer()
        self.uart_timer.setInterval(10)
        self.uart_timer.timeout.connect(self.uart_rx)
        #setup one second timer
        self.one_sec_timer = QTimer()
        self.one_sec_timer.setInterval(1000)
        self.one_sec_timer.timeout.connect(self.one_sec_handler)
        #Setup Serial
        self.serial = None
        self.serial_running = None
        self.start_serial(self.comport,self.baudrate)
        self.ui.SerialStatus.setText(QtCore.QCoreApplication.translate("MainWindow", comport_dic['comport']))

        self.setup_buttons()

        #Start timer and show window
        self.uart_timer.start()
        self.one_sec_timer.start()
        self.show()

    def setup_buttons(self):
        # Connect buttons to functions
        self.ui.SuspendSerial.clicked.connect(self.handle_disconnect_resume)
        self.ui.SendAt.clicked.connect(self.handle_send)
        self.ui.AtCommandLine.returnPressed.connect(self.handle_send)
        self.ui.ClearScreen.clicked.connect(self.clear_text_box)
        self.ui.Exit.clicked.connect(self.close_and_exit)
        self.ui.PrintLogInfo.clicked.connect(self.print_log_files)
        self.ui.CommandHistory.clicked.connect(self.display_command_history)
        self.ui.PrevSendAt.clicked.connect(self.handle_prev_send_at)

    def test(self):
        print("Key Press")
    
    def start_serial(self,comport,baudrate):
        """
        setup serial port, Start Serial Com
        """
        if not isinstance(baudrate,int):
            baudrate = int(baudrate)
        try:
            self.serial = serial.Serial(port=comport,baudrate=baudrate,timeout=0.4)
            self.print_banner()
        except Exception as e:
            print("start_serial")
            print(e)
            self.bot_print_error("FAILED OPENNING COMPORT")
            self.set_serial_stopped()
            return
        
        self.set_serial_running()

    def shutdown_serial(self):
        """
        Shutdown serial
        """
        self.serial.close()
        self.set_serial_stopped()

    def set_serial_running(self):
        """
        Call When serial is running
        """
        self.serial_running = True

    def set_serial_stopped(self):
        """
        Call when stopping serial
        """
        self.serial_running = False

    def print_to_box(self,line,bg_color=None,txt_color=None):
        """
        Any time printing to SerialOutput box
        """
        style = ""
        custom_text =""
        if txt_color:
            style = "color:#{0};".format(txt_color)
        if bg_color:
            style = style + " background-color:#{0}".format(bg_color)

        if txt_color or bg_color:
            custom_text = "<span style=\" {0};\" >".format(style)
            line=line.replace(" ","&nbsp;")
            custom_text=custom_text + line
            custom_text=custom_text + "</span>"
            self.ui.SerialOutput.append(custom_text)
        else:
            self.ui.SerialOutput.append(line)
        # move cursor to end if following line
        if self.ui.FollowLog.isChecked():
            self.ui.SerialOutput.moveCursor(QtGui.QTextCursor.End)

    def uart_rx(self):
        """
        Read Uart, this is function running on timer
        """
        try:
            line = self.read_uart()
        except Exception as e:
            self.bot_print_error("FAILED OPENNING COMPORT")
            self.set_serial_stopped()
            return

        if line:
            self.print_to_box(line,False,False)
            self.line_handler(line)
        else:
            pass

    def one_sec_handler(self):
        #Read Config for color code here:
        #Rotate logs here
        if self.logenabled:
            if os.stat(self.log.path_serial_log).st_size > self.log.rotation_size and self.log_roation:
                self.log.renew_logs()
        

    def line_handler(self,line):
        """
        Any Action on Line handle here
        """
        if self.logenabled:
            log_line(line,self.log.serial_log_file, self.log.serial_info_file)
        else:
            pass
        return

    def read_uart(self):
        """
        Read Uart base on configuration
        """
        try:
            if self.serial_running and self.serial.in_waiting and self.serial.is_open:
                line = self.serial.readline()
                line = line.decode("ascii","backslashreplace")
                return line.rstrip()
            else:
                return None
        except Exception as e:
            print("read_uart")
            print(e)
            self.bot_print_error("COMPORT Disconnected")
            self.handle_disconnect_resume()


    def handle_disconnect_resume(self):
        """
        Disconnect, Reconnect button
        """
        if self.serial_running:
            # disconnect the serial so it is open to other processes
            self.shutdown_serial()
            #Stop timer
            self.uart_timer.stop()
            self.ui.SuspendSerial.setText(QtCore.QCoreApplication.translate("MainWindow", "Resume ComPort"))
            self.ui.SerialStatus.setText(QtCore.QCoreApplication.translate("MainWindow", self.comport+" Suspended"))
            self.ui.SerialStatus.setStyleSheet("color : red;")
        else:
            self.start_serial(self.comport,self.baudrate)
            self.uart_timer.start()
            self.ui.SuspendSerial.setText(QtCore.QCoreApplication.translate("MainWindow", "Suspend ComPort"))
            self.ui.SerialStatus.setText(QtCore.QCoreApplication.translate("MainWindow", self.comport))
            self.ui.SerialStatus.setStyleSheet("color : green;")

    def handle_send(self):
        """
        Send box, and send button
        """
        command = self.ui.AtCommandLine.text()
        result = self.send_to_uart(command)
        if result:
            self.ui.AtCommandLine.clear()
            self.add_command_to_drop_down(command)
    
    def send_to_uart(self,command):
        """
        Send directly to serial
        """
        if self.serial_running and self.serial.is_open:
            self.serial.write(str.encode(command+"\r\n"))
            self.commandlist.append(command)
            
            return True
        else:
            return None

    def add_command_to_drop_down(self,command):
        self.ui.PrevCommand.addItem(command)

    def clear_text_box(self):
        """
        Clear the SerialOutput box
        """
        self.ui.SerialOutput.clear()


    def close_and_exit(self):
        """
        Close the application
        """
        if self.serial_running:
            self.shutdown_serial()    
        sys.exit()

    def bot_print(self,message):
        """
        Any bot created message
        """
        self.print_to_box(message,"005596","ffffff")

    def bot_print_error(self,message):
        """
        Any bot created message
        """
        self.print_to_box(message,"c21313","ffffff")

    def print_log_files(self):
        """
        Get current logs
        """
        if self.logenabled:
            self.bot_print(self.log.path_serial_log)

    def print_banner(self):
        """
        print terminal banner
        """
        banner="Serial port => {0:5} | Log Name => {1:5}".format(self.comport,self.log_name)
        if self.logenabled:
            log_line(banner+"\r\n",self.log.serial_log_file, self.log.serial_info_file)
        self.bot_print(banner)

    def display_command_history(self):
        command_history = CommandHistory(self.commandlist,self.nightmode)
        self.list_of_window.append(command_history)
        command_history.show()

    def read_prev_command(self):
        return self.ui.PrevCommand.currentText()

    def handle_prev_send_at(self):
        command = self.read_prev_command()
        if command:
            self.send_to_uart(command)
