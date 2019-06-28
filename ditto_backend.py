import os, requests, shutil
import random
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
	"""
	Usage: get all libraries for a specific user
	
	Parameters:
		user_id (int or string): the unique token for each user provided by discord.py
	
	Returns:
		libs (str): a list of all libraries
	"""
	user_dir_path = get_user_dir_path(user_id)
	libs = [name for subdir, dirs, _ in os.walk(user_dir_path, topdown=False) for name in dirs]
	return libs

def get_lib_images(user_id, lib_name):
	"""
	Usage: get all images for a specific library of a user
	
	Parameters:
		user_id (int or string): the unique token for each user provided by discord.py
		lib_name (str): the name of the library the user wishes to save the image to
	
	Returns:
		images (str): a list of all images
	"""
	lib_path = os.path.join(get_user_dir_path(user_id), lib_name)
	images = [name for subdir, _, files in os.walk(lib_path, topdown=False) for name in files]
	return images

def create_lib(user_id, lib_name):
	try:
		os.mkdir(os.path.join(USERDIRS, str(user_id), lib_name))
	except OSError:
		print("Failed to make {} for {}".format(lib_name, user_id))
	else:
		print("Successfully created {} for {}".format(lib_name, user_id))
		return "Success!"

def add_img_to_lib(user_id, lib_name, img_name, attachment_url):
	"""
	Usage: Downloads content from an given url and saves it to the path ./user_directories/user_id/lib_name/img_name

	Parameters:
		user_id (str or int): the unique token for each user provided by discord.py
		lib_name (str): the name of the library the user wishes to save the image to
		img_name (str): the name of the image the user wishes to save the file under
		attachment_url (str): the url to the discord media attachment
	
	Returns:
		bool result: True if successful, False if failed
	"""
	user_id = str(user_id)
	file_name = os.path.join(USERDIRS, user_id, lib_name, "{}.jpg".format(img_name))
	req = requests.get(attachment_url, stream=True)
	if req.status_code == 200:
		with open(file_name, 'wb') as f:
			req.raw.decode_content = True
			shutil.copyfileobj(req.raw, f)
		return True
	else:
		return False

	
def get_random_image(user_id, lib_name):
	file_name = ""
	for root, _, files in os.walk(os.path.join(USERDIRS, str(user_id), lib_name)):
		file_name = os.path.join(root, random.choice(files))
	return file_name


def get_lib_image(user_id, lib_name, img_name):
	"""
	Usage: Retrieve a direct path to the media requested by user

	Parameters:
		user_id (str or int): the unique token for each user provided by discord.py
		lib_name (str): the name of the library the user wishes to save the image to
		img_name (str): the name of the image the user wishes to save the file under

	Returns:
		if successful | file_path (str): the direct filepath to the image 
		else | error_message (str)

	"""
	file_path = os.path.join(USERDIRS, str(user_id), lib_name, img_name + ".jpg")
	if os.path.exists(file_path) and os.path.isfile(file_path):
		return file_path
	else:
		return ("Image {} does not exist.".format(img_name))

def remove_image(user_id, lib_name, img_name):
	"""
	Usage: Remove an image from a library

	Parameters:
		user_id (str or int): the unique token for each user provided by discord.py
		lib_name (str): the name of the library the user wishes to remove from
		img_name (str): the name of the image the user wishes to remove

	Returns:
		if successful | True
		else | False

	"""
	file_path = get_lib_image(user_id, lib_name, img_name)
	if file_path:
		os.remove(file_path)
		return True
	else:
		return False

def remove_lib(user_id, lib_name):
	"""
	Usage: Remove an image from a library

	Parameters:
		user_id (str or int): the unique token for each user provided by discord.py
		lib_name (str): the name of the library the user wishes to remove from

	Returns:
		if successful | True
		else | False

	"""
	dir_path = os.path.join(get_user_dir_path(user_id), lib_name)
	if os.path.isdir(dir_path) and os.path.exists(dir_path):
		shutil.rmtree(dir_path)
		return True
	else:
		return False
