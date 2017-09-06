# USING STRINGS

def main():
	s = 'This is 1 string!'
	print(s)

	s = r'This is 2 string!'
	print(s)

	# format() - method in string object.
	n = 3
	s = 'This is {} string!'.format(n)
	print(s)
	# This is a way was done in PYTHON 3 !!!
	# it will be dropped in next update.
	n = 4
	s = 'This is %s string!' % n
	print(s)

	# \ - save from newline
	s = """\
this is 5 string
line after line
of text and more
text.
"""
	print(s)







if __name__ == '__main__': main()