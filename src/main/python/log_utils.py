from datetime import datetime

class log_files(object):
	"""docstring for log_files"""
	def __init__(self, log_name,rotation_size=5000000):
		super(log_files, self).__init__()
		self.path_serial_log = log_name +".log"
		self.path_info_log = log_name+"_info" +".log"
		self.renew_logs_flag = False
		self.log_rev = 0
		self.serial_log_file = open(self.path_serial_log, 'w+')
		self.serial_info_file = open(self.path_info_log, 'w+')
		#5 mg
		self.rotation_size = rotation_size
	def renew_logs(self):
		self.log_rev += 1
		while self.path_serial_log[-1:].isnumeric():
			#num=num+self.path_serial_log[-1:]
			self.path_serial_log=self.path_serial_log[:-1]
			self.path_info_log=self.path_info_log[:-1]
		else:
			self.path_serial_log = self.path_serial_log+ str(self.log_rev)
			self.path_info_log = self.path_info_log + str(self.log_rev)
			self.serial_log_file = open(self.path_serial_log, 'w+')
			self.serial_info_file = open(self.path_info_log, 'w+')
			return
		self.path_serial_log=self.path_serial_log+ str(self.log_rev)
		self.path_info_log=self.path_info_log + str(self.log_rev)
		self.serial_info_file = open(self.path_info_log, 'w+')
		self.serial_log_file = open(self.path_serial_log, 'w+')
		self.renew_logs_flag = False

def log_line(line, serial_log_file, serial_info_file):
	"""Log one line"""
	serial_log_file.write(line+"\r\n")
	serial_log_file.flush()

	info_line ="[" + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')) +"]" +" - " + line
	serial_info_file.write(info_line+"\r\n")
	serial_info_file.flush()
	return True
