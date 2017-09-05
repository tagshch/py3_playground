#
# PATHS
#
import time
import datetime

import os
from os import path

def main():

	# os name
	print(os.name)

	# Check file existence and type
	filePath = "test.txt"
	print('Item exists:', path.exists(filePath))
	print('Item is a file:', path.isfile(filePath))
	print('Item is a directory:', path.isdir(filePath))

	# Work with file paths
	print("Item's path", path.realpath(filePath))
	print("Item's path and name", path.split(path.realpath(filePath)))

	# Get the modification time
	mtime = path.getmtime(filePath)

	t1 = time.ctime(mtime)
	print('Item modification time:', t1)
	t2 = datetime.datetime.fromtimestamp(mtime)
	print('Item modification time:', t2)

	# Calculate how long ago item was modificated
	td = datetime.datetime.now() - datetime.datetime.fromtimestamp(mtime)
	print('Item modification time ago', td)
	print('Item modification time ago', td.total_seconds(), 'sec')




if __name__ == '__main__':
	main()

