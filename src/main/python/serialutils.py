import serial.tools.list_ports
import string

def get_list_ports():
	"""
	retunr list of ports string with description
	"""
	list_ports_string = list()
	for port in serial.tools.list_ports.comports():
		list_ports_string.append(str(port))
	return list_ports_string

def get_list_device():
	"""
	return list of device to feed to serial 
	"""
	list_of_device = list()
	for port in serial.tools.list_ports.comports():
		list_of_device.append(port.device)
	return list_of_device

