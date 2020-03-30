import os
import sys
import json
from random import randint
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models import Defectloglist, Monitoringproduct
# Create your views here.

def logmonitorset(request):
	product = Monitoringproduct.objects.values('user', 'host', 'pw', 'product', 'ostype', 'logpath', 'logname').first()
	defectwords = Defectloglist.objects.values('word')
	regedwords = Defectloglist.objects.filter(marked=True).values('id','word')
	defectlogs = []

	if 'create' in request.POST:
		Monitoringproduct.objects.filter().delete()
		Monitoringproduct(
			user = request.POST['id'],
			host = request.POST['host'],
			pw = request.POST['pw'],
			product = request.POST['product'],
			ostype = request.POST['ostype'],
			logpath = request.POST['logpath'].replace("\\", "\\\\"),
			logname = request.POST['logname'],
		).save()
		product = Monitoringproduct.objects.values('user', 'host', 'pw', 'product', 'ostype', 'logpath', 'logname').first()
	
	elif 'check' in request.POST:
		if product['ostype'] == "Windows":
			os.system("/home/qceo/QCEO/scripts/windowschk.sh "  + product['host'] + " " + product['user'] + " " + product['pw'] + ' "' + product['logpath'] + '" ' + product['logname'])
		else :
			os.system("/home/qceo/QCEO/scripts/unixlinuxchk.sh " + product['user'] + "@"+ product['host'] + " " + product['pw'] + ' "' + product['logpath'] + '" ' + product['logname'])
	
	elif 'register' in request.POST:
		for s in defectwords:
			if request.POST['reglog'] == s['word']:
				print(s)
				return render(request, 'logmonitor/defectworderror.html', {'return':0})
		Defectloglist(word=request.POST['reglog']).save()
		defectwords = Defectloglist.objects.values('word')

	elif 'unmark' in request.POST:
		selectedlog = request.POST['id']
		Defectloglist.objects.filter(id=selectedlog).update(marked=False)

	elif 'log' in request.POST:
		selectedlog = request.POST['defectlist']
		Defectloglist.objects.filter(word=selectedlog).update(marked=True)

	elif 'update' in request.POST:
		if product['ostype'] == "Windows":
			os.system("/home/qceo/QCEO/scripts/windowsgetlog.sh "  + product['host'] + " " + product['user'] + " " + product['pw'] + ' "' + product['logpath'] + '" ' + product['logname'])
		else :
			os.system("/home/qceo/QCEO/scripts/unixlinuxgetlog.sh " + product['user'] + "@"+ product['host'] + " " + product['pw'] + ' "' + product['logpath'] + '" ' + product['logname']) 		#scp로 로그파일 가져와서 결함 문구 리스트랑 비교하고 걸리는 것들을 리스트에 저장
		filterwords = list(Defectloglist.objects.filter(marked=True).values_list('word', flat=True))
		colorset = ['FF0000', 'FFB200', 'FFF200', '37FF00', '00FFE1', '00E1FF', '0055FF', 'B600FF', 'FF00E9', '9B0096']
		matrix = []
		with open("/home/qceo/QCEO/agentlogs/" + product['logname'], 'rb') as f:
			lines = f.readlines()
			for i, line in enumerate(lines):
				try:
					matrix.append("[Line" + str(i+1) + ".] " +line.decode("utf-8"))
				except:
					pass

		defectlogs = []
		for i, filterwords in enumerate(filterwords):
			for x in matrix:
				if x.find(filterwords) != -1:
					defectlogs.append('<span style="color:#' + colorset[i] + '">' + x + "</span>")

	return render(request, 'logmonitor/logmonitor.html', {'defectwords':defectwords, 'regedwords':regedwords, 'product':product, 'defectlogs':defectlogs})
