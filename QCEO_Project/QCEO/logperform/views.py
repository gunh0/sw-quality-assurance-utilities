import os
import sys
import json
import datetime
from time import mktime
from django.core.serializers.json import DjangoJSONEncoder
from django.core.files import File
from django.shortcuts import render
from django.http import HttpResponse
from .models import Performance, Performagent
from .forms import ReserveForm

# Create your views here.
def logperform(request) :
	if request.method == 'POST':
		form = ReserveForm(request.POST)
		if form.is_valid():
			Performagent(
				ostype=request.POST['ostype'],
				process1=request.POST['process1'],
				process2=request.POST['process2'],
				process3=request.POST['process3'],
				process4=request.POST['process4'],
			).save()
	else:
		form = ReserveForm()

	agentdata = [{'timestamp':mktime(data.timestamp.timetuple()), 'agent':data.agent, 'cpus':[data.cpu, data.p1cpu, data.p2cpu, data.p3cpu, data.p4cpu, data.p5cpu], 'mems':[data.memory, data.p1memory, data.p2memory, data.p3memory, data.p4memory, data.p5memory]} for data in Performance.objects.all()]
	agents = [{'agentname':data['ostype'], 'process1':data['process1'], 'process2':data['process2'], 'process3':data['process3'], 'process4':data['process4']} for data in Performagent.objects.values('ostype', 'process1', 'process2', 'process3', 'process4', 'process5' )]
	
	return render(request, 'logperform/logperform.html', {'agentdata':agentdata, 'form':form, 'agents':agents})


def performdata(request):

	agentdata = [{'timestamp':mktime(data.timestamp.timetuple()), 'agent':data.agent, 'cpus':[data.cpu, data.p1cpu, data.p2cpu, data.p3cpu, data.p4cpu, data.p5cpu], 'mems':[data.memory, data.p1memory, data.p2memory, data.p3memory, data.p4memory, data.p5memory]} for data in Performance.objects.all()]

	return HttpResponse(json.dumps({'agentdata':agentdata}), content_type='application/json')


def agentdelete(request):
	delobj = Performagent.objects.get(ostype=request.POST['ostype'])
	delobj.delete()
	return render(request, 'logperform/agentdelete.html', {})


def performdatadelete(request):
	Performance.objects.all().delete()
	return render(request, 'logperform/performdatadelete.html', {})