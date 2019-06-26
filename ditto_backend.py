import os, requests
USERDIRS = "./user_directories"


def get_user_dir_path(user_id):
	"""
	Usage: Get the path to a users directory, and create one if it doesn't exist already

	Parameters:
		user_id (int or string): the unique token for each user provided by discord.py

	Returns:
		user_dir_path (string): a string representing the path from root to user's unique directory
	"""
	if str(user_id) in [name for subdir,dirs,files in os.walk(USERDIRS, topdown=False) for name in dirs]:
		return os.path.join(USERDIRS, str(user_id))
	else:
		print("Cannot find user dir.. making one")
<<<<<<< HEAD
		create_user_dir(user_id)
		return False

def create_user_dir(dir_name):
	print("Created directory for {user_id}".format(dir_name))
=======
		return create_user_dir(os.path.join(USERDIRS, str(user_id)))

def create_user_dir(path):
	"""
	Usage: Creates a unique directory based on a path including a unique user_id

	Parameters:
		path (str): a string that includes a unique user id e.g.: ./user-directors/user_id

	Returns:	
		path (str): a string that includes a unique user id e.g.: ./user-directors/user_id
	"""
	try:
		os.mkdir(path)
	except OSError:
		print("Failed to create User Directory with " + path)
	else:
		print("Created directory {path_to_dir}".format(path_to_dir=path)) 
	return path

def get_user_libs(user_id):
	user_dir_path = get_user_dir_path(user_id)
	libs = [name for subdir, dirs, _ in os.walk(user_dir_path, topdown=False) for name in dirs]
	return libs

def create_lib(user_id, lib_name):
	try:
		os.mkdir(os.path.join(USERDIRS, str(user_id), lib_name))
	except OSError:
		print("Failed to make {} for {}".format(lib_name, user_id))
	else:
		print("Successfully created {} for {}".format(lib_name, user_id))
		return "Success!"

def add_img_to_lib(user_id, lib_name, img_name, attachment_url):
	pass

def get_random_image(user_id, lib_name):
	pass

def get_lib_image(user_id, lib_name, img_name):
	pass
>>>>>>> origin/drey
