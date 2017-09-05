#
# WEB DATA
#

import urllib3
import json
from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
	def handle_comment(self, data):
		if data:
			pos = self.getpos()
			print('handler_comment:', data, 'at line', pos[0], 'at position', pos[1])


def htmlCode():
	http = urllib3.PoolManager()

	res = http.request("GET", "http://knbase.org/8")

	if(res.status == 200):
		parser = MyHtmlParser()
		parser.feed(res.data.decode("utf-8"))

		try:
			parser.handle_comment()
		except:
			print('Some fucked error with no args!')


def jsonCode():
	http = urllib3.PoolManager()
	res = http.request("GET", "https://api.hh.ru/vacancies")
	print('\nRESPONSE:', res.status, res.headers, res.data, '\n')

	pojo = json.loads(res.data.decode('utf-8'))
	print('JSON ERRORS:', pojo['errors'])


def main():
	# === JSON ===
	# jsonCode()

	# === HTML ===
	htmlCode()


if __name__ == "__main__":
	main()
