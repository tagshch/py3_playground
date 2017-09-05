#
# SHELL
#

import os
import shutil

from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():

	filePath = "test.txt"

	# duplicate existing file
	if(path.exists(filePath)):
		src = path.realpath(filePath)
		head, tail = path.split(src)

		print('Path:', head)
		print('File:', tail)

		dst = src + '.bak'

		# copy file
		shutil.copy(src, dst)
		# copy over permissions, modification times, and other
		shutil.copystat(src, dst)

		# rename
		os.rename(filePath, 'copied_' + filePath)
		os.rename("copied_test.txt", filePath)

		# ZIP archive
		shutil.make_archive('test', 'zip', head)

		# more fine-grained control over ZIP files
		with ZipFile("testzip.zip", "w") as newzip:
			newzip.write(filePath)
			newzip.write(filePath + ".bak")



if __name__ == '__main__':
	main()