# EXCEPTIONS try-except

try:
	fh = open('ch_1_linesER.txt')
	for line in fh.readlines():
		print(line)
# except:
	# print('Smth bad happened')

except IOError as e:
	print('Error is: {}'.format(e))