import socketserver
import os
import re
import datetime
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QCEO.settings")
django.setup()

from logperform.models import Performance

class RequestHandler(socketserver.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(1024).strip().decode('euc-kr')
		tmps = re.findall('\d*\.?\d+', self.data)
		datas = ['']*13
		for i, x in enumerate(tmps):
			datas[i+1] = x
		
		print(datas)

		Performance(
			timestamp = datetime.datetime.now(),
			agent = self.data.split()[0],
			cpu = datas[1],
			memory = datas[2],
			p1cpu = datas[3],
			p1memory = datas[4],
			p2cpu = datas[5],
			p2memory = datas[6],
			p3cpu = datas[7],
			p3memory = datas[8],
			p4cpu = datas[9],
			p4memory = datas[10],
			p5cpu = datas[11],
			p5memory = datas[12],
		).save()

if __name__ == '__main__':
	host, port = "192.168.120.166", 4000
	obj = socketserver.TCPServer((host, port), RequestHandler)
	obj.serve_forever()

'''
import socketserver
import os
import re
import datetime
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QCEO.settings")
django.setup()

from logperform.models import Performance


class RequestHandler(socketserver.BaseRequestHandler):
	def handle(self):
		self.data = self.request.recv(1024).strip().decode('euc-kr')
		print(Performance(
			timestamp = datetime.datetime.now(),
			agent = self.data.split()[0],
			cpu = re.findall('\d*\.?\d+', self.data)[1],
			memory = re.findall('\d*\.?\d+', self.data)[2]
		).save())

if __name__ == '__main__':
	host, port = "192.168.120.166", 4000
	obj  = socketserver.TCPServer((host, port), RequestHandler)
	obj.serve_forever()
'''
