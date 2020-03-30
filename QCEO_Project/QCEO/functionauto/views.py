import json
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from functionauto.models import Autotest, Testreserve
from .forms import ReserveForm

# Create your views here.

@login_required
def functionauto(request):
	form = ReserveForm()
	if 'reserve' in request.POST:
		form = ReserveForm(request.POST)
		if form.is_valid():
			form.save()
			form = ReserveForm()

	elif 'mount' in request.POST:
		os.system('sudo mount -a')

	datas = []
	num = 0
	testsets = Autotest.objects.values("project", "testname", "total",	"starttime", "path", "file")
	totalnum = Autotest.objects.all().count()
	for testset in testsets:
		if testset['path']:
			dirpath = testset['path']
			dirs = []
			for filename in os.listdir(dirpath):
				full_filename = os.path.join(dirpath, filename)
				if os.path.isdir(full_filename):
					dirs.append(filename)
			if len(dirs) != 0:
				dirlen = round(testset['total']/len(dirs)) * 100
			else:
				dirlen = 0
			datas.append({"num":str(num), "project":testset["project"], "testname":testset["testname"], "total":testset["total"], "starttime":testset["starttime"], "dirlen":dirlen, "file":testset["file"]})
			num = num + 1

	reserves = Testreserve.objects.values("project", "name", "state", "starttime", "reservetime")
		
	return render(request, 'functionauto/functionauto.html', {'datas':datas, 'totalnum':totalnum, 'form':form, 'reserves':reserves})


@login_required
def processbars(request):
	datas = []
	num = 0
	testsets = Autotest.objects.values("project", "testname", "total",	"starttime", "path")
	totalnum = Autotest.objects.all().count()
	for testset in testsets:
		dirpath = testset['path']
		dirs = []
		for filename in os.listdir(dirpath):
			full_filename = os.path.join(dirpath, filename)
			if os.path.isdir(full_filename):
				dirs.append(filename)
		dirlen = len(dirs)
		datas.append({"num":str(num), "project":testset["project"], "testname":testset["testname"], "total":str(testset["total"]), "starttime":str(testset["starttime"]), "dirlen":dirlen})
		num = num + 1
	return HttpResponse(json.dumps({'datas':datas, 'totalnum':totalnum}), content_type='application/json')


def noreport(request):
	print("test")
	return render(request, 'functionauto/noreport.html', {'return':0})
