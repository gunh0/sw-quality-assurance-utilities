import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QCEO.settings")

import django
django.setup()

import datetime
import csv
from dataproc.models import Data


matrix = []

filename = 'issues' + datetime.datetime.now().strftime('%m%d') + '.csv'
f = open('/home/qceo/issues/secums/'+filename, 'r')
rdr = csv.reader(f)
for line in rdr:
	matrix.append(line)
		
f.close()

for x in range(1, len(matrix)-1): 
	for y in range(11, 14):
		if matrix[x][y]=="":
			matrix[x][y] = '1999/01/01'
			
for x in range(1, len(matrix)-1): 
	if matrix[x][14]=="":
		matrix[x][14] = '사내'

for x in range(1, len(matrix)-1): 
	Data(
		num=int(matrix[x][0]),
		project=matrix[x][1],
		type=matrix[x][2],
		state=matrix[x][3],
		realize=matrix[x][4],
		priority=matrix[x][5],
		subject=matrix[x][6],
		author=matrix[x][7],
		charge=matrix[x][8],
		category=matrix[x][9],
		targetversion=matrix[x][10],
		change=datetime.datetime.strptime(matrix[x][11], "%Y/%m/%d %H:%M"),
		startdate=datetime.datetime.strptime(matrix[x][12], "%Y/%m/%d").date(),
		enddate=datetime.datetime.strptime(matrix[x][13], "%Y/%m/%d").date(),
		client=matrix[x][14],
		degree=matrix[x][15],
		#inputdate=datetime.datetime(2018, 5, 23, 9, 0)
	).save()

matrix = []
#omniguard unix
filename = 'issues' + datetime.datetime.now().strftime('%m%d') + '.csv'
f = open('/home/qceo/issues/omniguardunix/'+filename, 'r') #웹에서 직접 다운받은 것은 인코딩 필요 , encoding='euc-kr')
rdr = csv.reader(f)
for line in rdr:
	matrix.append(line)
		
f.close()
	
print(matrix)

for x in range(1, len(matrix)-1): 
	for y in range(10, 13):
		if matrix[x][y]=="":
			matrix[x][y] = '1999/01/01'
			
for x in range(1, len(matrix)-1): 
	if matrix[x][13]=="":
		matrix[x][13] = '사내'

for x in range(1, len(matrix)-1): 
	Data(
		num=int(matrix[x][0]),
		project=matrix[x][1],
		type=matrix[x][2],
		state=matrix[x][3],
		priority=matrix[x][4],
		subject=matrix[x][5],
		author=matrix[x][6],
		charge=matrix[x][7],
		category=matrix[x][8],
		targetversion=matrix[x][9],
		change=datetime.datetime.strptime(matrix[x][10], "%Y/%m/%d %H:%M"),
		startdate=datetime.datetime.strptime(matrix[x][11], "%Y/%m/%d").date(),
		enddate=datetime.datetime.strptime(matrix[x][12], "%Y/%m/%d").date(),
		client=matrix[x][13],
		degree=matrix[x][14],
		#inputdate=datetime.datetime(2018, 5, 23, 9, 0)
	).save()

matrix = []
#omniguard windows
filename = 'issues' + datetime.datetime.now().strftime('%m%d') + '.csv'
f = open('/home/qceo/issues/omniguardwindows/'+filename, 'r') #웹에서 직접 다운받은 것은 인코딩 필요 , encoding='euc-kr')
rdr = csv.reader(f)
for line in rdr:
	matrix.append(line)
		
f.close()
	
print(matrix)

for x in range(1, len(matrix)-1): 
	for y in range(10, 13):
		if matrix[x][y]=="":
			matrix[x][y] = '1999/01/01'
			
for x in range(1, len(matrix)-1): 
	if matrix[x][13]=="":
		matrix[x][13] = '사내'

for x in range(1, len(matrix)-1): 
	Data(
		num=int(matrix[x][0]),
		project=matrix[x][1],
		type=matrix[x][2],
		state=matrix[x][3],
		priority=matrix[x][4],
		subject=matrix[x][5],
		author=matrix[x][6],
		charge=matrix[x][7],
		category=matrix[x][8],
		targetversion=matrix[x][9],
		change=datetime.datetime.strptime(matrix[x][10], "%Y/%m/%d %H:%M"),
		startdate=datetime.datetime.strptime(matrix[x][11], "%Y/%m/%d").date(),
		enddate=datetime.datetime.strptime(matrix[x][12], "%Y/%m/%d").date(),
		client=matrix[x][13],
		degree=matrix[x][14],
		#inputdate=datetime.datetime(2018, 5, 23, 9, 0)
	).save()

matrix = []
#fossguard
filename = 'issues' + datetime.datetime.now().strftime('%m%d') + '.csv'
f = open('/home/qceo/issues/fossguard/'+filename, 'r') #웹에서 직접 다운받은 것은 인코딩 필요 , encoding='euc-kr')
rdr = csv.reader(f)
for line in rdr:
	matrix.append(line)
		
f.close()
	
print(matrix)

for x in range(1, len(matrix)-1): 
	for y in range(10, 13):
		if matrix[x][y]=="":
			matrix[x][y] = '1999/01/01'
			
for x in range(1, len(matrix)-1): 
	if matrix[x][13]=="":
		matrix[x][13] = '사내'

for x in range(1, len(matrix)-1): 
	Data(
		num=int(matrix[x][0]),
		project=matrix[x][1],
		type=matrix[x][2],
		state=matrix[x][3],
		priority=matrix[x][4],
		subject=matrix[x][5],
		author=matrix[x][6],
		charge=matrix[x][7],
		category=matrix[x][8],
		targetversion=matrix[x][9],
		change=datetime.datetime.strptime(matrix[x][10], "%Y/%m/%d %H:%M"),
		startdate=datetime.datetime.strptime(matrix[x][11], "%Y/%m/%d").date(),
		enddate=datetime.datetime.strptime(matrix[x][12], "%Y/%m/%d").date(),
		client=matrix[x][13],
		degree=matrix[x][14],
		#inputdate=datetime.datetime(2018, 5, 23, 9, 0)
	).save()

matrix = []
#athena
filename = 'issues' + datetime.datetime.now().strftime('%m%d') + '.csv'
f = open('/home/qceo/issues/athena/'+filename, 'r') #웹에서 직접 다운받은 것은 인코딩 필요 , encoding='euc-kr')
rdr = csv.reader(f)
for line in rdr:
	matrix.append(line)
		
f.close()
	
print(matrix)

for x in range(1, len(matrix)-1): 
	for y in range(10, 13):
		if matrix[x][y]=="":
			matrix[x][y] = '1999/01/01'
			
for x in range(1, len(matrix)-1): 
	if matrix[x][13]=="":
		matrix[x][13] = '사내'

for x in range(1, len(matrix)-1): 
	Data(
		num=int(matrix[x][0]),
		project=matrix[x][1],
		type=matrix[x][2],
		state=matrix[x][3],
		priority=matrix[x][4],
		subject=matrix[x][5],
		author=matrix[x][6],
		charge=matrix[x][7],
		category=matrix[x][8],
		targetversion=matrix[x][9],
		change=datetime.datetime.strptime(matrix[x][10], "%Y/%m/%d %H:%M"),
		startdate=datetime.datetime.strptime(matrix[x][11], "%Y/%m/%d").date(),
		enddate=datetime.datetime.strptime(matrix[x][12], "%Y/%m/%d").date(),
		client=matrix[x][13],
		degree=matrix[x][14],
		#inputdate=datetime.datetime(2018, 5, 23, 9, 0)
	).save()