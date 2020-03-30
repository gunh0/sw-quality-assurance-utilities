import os

dirpath = 'Z:\\'

for filename in os.listdir(dirpath):
	full_filename = os.path.join(dirpath, filename)
	if os.path.isdir(full_filename):
		print(filename)