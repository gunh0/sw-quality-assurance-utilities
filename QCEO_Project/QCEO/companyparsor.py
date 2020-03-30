import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "QCEO.settings")

import django
django.setup()

import datetime
import csv
from dataproc.models import Company


matrix = []

f = open('C:\\Users\\User\\Desktop\\Project\\address.csv', 'r')
rdr = csv.reader(f)
for line in rdr:
		matrix.append(line)
		
f.close()
	
print(matrix)

for x in range(1, len(matrix)-1): 
	print(matrix[x][1], matrix[x][6])

for x in range(1, len(matrix)-1): 
	print(x)
	Company(
		name=matrix[x][1],
		email=matrix[x][6],
	).save()