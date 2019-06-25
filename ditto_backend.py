import os
USERDIRS = "./user_directories"


def get_user_dir_path(user_id):
	if str(user_id) in [name for subdir,dirs,files in os.walk(USERDIRS, topdown=False) for name in dirs]:
		return os.path.join(USERDIRS, str(user_id))
	else:
		print("Cannot find user dir.. making one")
		return create_user_dir(os.path.join(USERDIRS, str(user_id)))

def create_user_dir(path):
	print("Created directory {path_to_dir}".format(path_to_dir=path))
	return path

def get_user_libs(user_id):
	user_dir_path = get_user_dir_path(user_id)
	libs = [name for subdir, dirs, _ in os.walk(user_dir_path, topdown=False) for name in dirs]
	return libs

def create_lib(user_id, lib_name):
	pass

def add_img_to_lib(user_id, lib_name):
	pass

def get_random_image(user_id, lib_name):
	pass

def get_lib_image(user_id, lib_name, img_name):
	pass