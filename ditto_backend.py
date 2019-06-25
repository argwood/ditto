import os
USERDIRS = "./user_directories"

def get_user_libs(user_id):
	return "\n".join(["""children of user directory"""])

def get_user_dir(user_id):
	if str(user_id) in [name for subdir,dirs,files in os.walk(USERDIRS, topdown=False) for name in dirs]:
		return True
	else:
		print("Cannot find user dir.. making one")
		create_user_dir(user_id):
		return False

def create_user_dir(dir_name):
	print("Created directory for {user_id}".format(dir_name))