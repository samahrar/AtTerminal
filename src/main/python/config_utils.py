import os,json


def make_config_dir():
    #Make current working dir a config director
    config_dir = os.path.join(os.getcwd(),"configuration")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    return config_dir
def get_path_config_file():
	config_dir = make_config_dir()
	config_file = os.path.join(config_dir,"application_config.json")
	return config_file

def read_config():
	config_file = get_path_config_file()
	if os.path.exists(config_file):
		return read_json_config()
	else:
		return False

def get_baudrate_index(baudrate):
		av_baudrate = ["115200","57600","19200","9600","4800"]
		return av_baudrate.index(baudrate)

def save_confg(properties_dict):
	properties_dict = properties_dict
	config_file= get_path_config_file()
	#json_object = json.dumps(properties_dict, indent = 4)
	with open(config_file, "w") as file:  
		json.dump(properties_dict, file) 

def read_json_config():
	config_file= get_path_config_file()
	with open(config_file) as file:
		config_dict = json.load(file)
	return config_dict

def restore_defaults():
	config_file = get_path_config_file()
	if os.path.exists(config_file):
  		os.remove(config_file)