#
# FILES
#

def main():
	# open and write
	f1 = open('test.txt', 'w+')

	# write to file
	for i in range(10):
		f1.write('This is line %d\r\n' % (i+1))

	# close file when done
	f1.close()

	# open and append
	f2 = open('test.txt', 'a+')
	f2.write('Appended string!')
	f2.close()

	# open and read
	f3 = open('test.txt', 'r')

	if f3.mode == 'r':
		content = f3.read()
		print('Content:\n','\r' + content)

	f3.close()

	# open and read lines
	f4 = open('test.txt', 'r')

	if f4.mode == 'r':
		# read line by line
		lines = f4.readlines()
		print('Readlines:', lines)

	f4.close()




if __name__ == '__main__':
	main()
