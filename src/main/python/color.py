class color_config(object):
	def __init__(self,path_to_config):
		self.path_to_config = path_to_config
		self.dic_config = {}

	def read_color_config(self):
		self.dic_config={}
		#Need to protect with try incase OS/another PID is holding the file.
		try:
			fd = open(self.path_to_config)
			list_of_lines=[]
			for line in fd.read().splitlines():
				if "#" in line:
					pass
				else:
					if line not in list_of_lines:
						list_of_lines.append(line.lower())
			fd.close()
			for i in list_of_lines:
				string = i.split("=")[0]
				color = i.split("=")[1]
				self.dic_config[string]=color
		except:
			pass
		return

	def get_color_of_key(self,line):
		color = None
		print(line)
		for key in self.dic_config:
			if line.lower() in key.lower():
				color = self.dic_config[key]
		return color

test_color=color_config("test.cfg")
test_color.read_color_config()
print(test_color.dic_config)
print(test_color.get_color_of_key("test1"))
print("---")
print(test_color.get_color_of_key("gps"))
print("---")
print(test_color.get_color_of_key("test"))
print("---")
print(test_color.get_color_of_key("cell"))
print("---")