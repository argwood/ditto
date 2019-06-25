import os
USERDIRS = "./user_directories"

def get_user_libs(user_id):
	return "\n".join(["""children of user directory"""])

def get_user_dir(user_id):
	if str(user_id) in [name for subdir,dirs,files in os.walk(USERDIRS, topdown=False) for name in dirs]:
		return True
	else:
		print("Cannot find user dir.. making one")

	"""
	for subdir, dirs, files in os.walk(USERDIRS, topdown=False):
		for name in dirs:
			print(name)
	"""