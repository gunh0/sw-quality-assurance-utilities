from datetime import date, timedelta, datetime
import datetime
import re
import math
import numpy as np
import smtplib
from email.mime.text import MIMEText
from django.shortcuts import render
from dataproc.models import Data, Process, Company, Totalquality, Productquality
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Count

# Create your views here.
@login_required
def dashboard(request):
	days = [date.today() - timedelta(x) for x in range(4, -1, -1)]
		
	# 전체품질 : 날짜 입력되지 않았을 경우 - 5일치, 날짜 입력 받아서 지정기간 품질 출력
	sdate = days[0].strftime("%Y-%m-%d") # 기본 시작날짜 - 5일전
	edate = days[4].strftime("%Y-%m-%d") # 기본 끝날짜 - 오늘



	if request.POST: # 입력된 날짜대로 지정 기간설정
		sdate = request.POST.get('sdate')
		edate = request.POST.get('edate')
	# 설정된 기간만큼 전체품질 현황 출력
	termset = Totalquality.objects.filter(date__range=(sdate, edate)).values('manualtest', 'process', 'faulty', 'date').order_by('date') #설정된 기간만큼 manualtest(수동테스트), process(프로세스), faulity(결함율)을 가져옴
	qualities = [{'date':term['date'].strftime("%m/%d"), 'value':term['manualtest'] + term['process'] + term['faulty']} for term in termset] # 날짜와 가져온 값들을 더해서 리스트로 묶음
		
	#등록된 프로젝트 프로레스 출력
	processbars = []
	project_set = Process.objects.values('project','version', 'start', 'end', 'firststep', 'secondstep', 'thirdstep', 'file', 'is_deleted') # 프로젝트 관련정보 가져오기
	for project in project_set:
		totaldays = int(re.findall('\d+', str(project['end']-project['start']))[0]) # 전체기간 계산
		fstepdays = int(re.findall('\d+', str(project['firststep']-project['start']))[0]) # 개발 기간 계산
		sstepdays = int(re.findall('\d+', str(project['secondstep']-project['firststep']))[0]) # 품질점검 기간 계산
		tstepdays = int(re.findall('\d+', str(project['thirdstep']-project['secondstep']))[0]) # 패키징 기간 계산
		estepdays = int(re.findall('\d+', str(project['end']-project['thirdstep']))[0]) # 설치 기간 계산
		currentdays = int(re.findall('\d+', str(date.today()-project['start']))[0]) # 시작일부터 현재까지 지난 기간 계산
		
		nowper = str(round((currentdays / totaldays) * 100)) # 전체기간중 지난 기간 비율로 환산
		if int(nowper) > 100: nowper = '100' # 100퍼센트가 넘어가면 100퍼센트로 고정
		fdays = str(math.floor((fstepdays / totaldays) * 100)) # 개발기간 비율 계산
		sdays = str(math.floor((sstepdays / totaldays) * 100)) # 품질점검 기간 비율 계산
		tdays = str(math.floor((tstepdays / totaldays) * 100)) # 패키징 기간 비율 계산
		edays = str(math.floor((estepdays / totaldays) * 100)) # 설치 기간 비율 계산

		processbars.append({
			'project':project['project'], # 프로젝트 명
			'version':project['version'], # 버전 정보
			'firststep':project['firststep'], # 개발기간 비율
			'secondstep':project['secondstep'], # 품질점검 기간 비율
			'thirdstep':project['thirdstep'], # 패키징 기간 비율
			'end':project['end'], # 설치 기간 비율
			'fdays':fdays, # 개발 시작 날짜
			'sdays':sdays, # 품질점검 시작 날짜
			'tdays':tdays, # 패키징 시작 날짜
			'edays':edays, # 설치 시작 날짜
			'nowper':nowper, # 오늘까지 지난 날들의 전체 퍼센트
			'file':project['file'], # 업로드한 보고서
			'is_deleted':project['is_deleted'], # 등록/등록해제
		})
	

	defectsdate = datetime.datetime.strptime(sdate, "%Y-%m-%d")
	defectedate = datetime.datetime.strptime(edate, "%Y-%m-%d")
	totalterm = int((defectedate-defectsdate).days)
	print(totalterm)

	#전체 결함 및 제품별 결함 출력
	data = [{'value':str(Data.objects.filter(inputdate__icontains=(defectsdate+datetime.timedelta(days=x)).strftime("%m-%d")).count()), 'date': str((defectsdate+datetime.timedelta(days=x)).strftime("%m-%d"))} for x in range(0, totalterm+1)] # 전체결함 출력
	p1 = [{'value':str(Data.objects.filter(project__icontains='SecuMS', inputdate__icontains=(defectsdate+datetime.timedelta(days=x)).strftime("%m-%d")).count()), 'date': str((defectsdate+datetime.timedelta(days=x)).strftime("%m-%d"))} for x in range(0, totalterm+1)] # SecuMS 결함 출력
	p2 = [{'value':str(Data.objects.filter(project__icontains='UniTy UNIX', inputdate__icontains=(defectsdate+datetime.timedelta(days=x)).strftime("%m-%d")).count()), 'date': str((defectsdate+datetime.timedelta(days=x)).strftime("%m-%d"))} for x in range(0, totalterm+1)] # OmniGuard Unix 결함 출력	
	p3 = [{'value':str(Data.objects.filter(project__icontains='UAC for Windows(SE)', inputdate__icontains=(defectsdate+datetime.timedelta(days=x)).strftime("%m-%d")).count()), 'date': str((defectsdate+datetime.timedelta(days=x)).strftime("%m-%d"))} for x in range(0, totalterm+1)] # OmniGuard windows 결함 출력
	p4 = [{'value':str(Data.objects.filter(project__icontains='FOSSGuard', inputdate__icontains=(defectsdate+datetime.timedelta(days=x)).strftime("%m-%d")).count()), 'date': str((defectsdate+datetime.timedelta(days=x)).strftime("%m-%d"))} for x in range(0, totalterm+1)] # FOSSGuard 결함 출력
	p5 = [{'value':str(Data.objects.filter(project__icontains='Athena Dev', inputdate__icontains=(defectsdate+datetime.timedelta(days=x)).strftime("%m-%d")).count()), 'date': str((defectsdate+datetime.timedelta(days=x)).strftime("%m-%d"))} for x in range(0, totalterm+1)] # Athena Dev 결함 출력

	return render(request, 'extern/dashboard.html', {'datas':data, 'p1s':p1, 'p2s':p2, 'p3s':p3, 'p4s':p4, 'p5s':p5, 'processbars':processbars, 'qualities':qualities, 'sdate':sdate, 'edate':edate})
	
	
@login_required
def product(request, product_id):
	products = ['SecuMS', 'OmniGuard Unix', 'OmniGuard Windows', 'FOSSGuard', 'Athena']
	projectnames = ['SecuMS', 'UniTy UNIX', 'UAC for Windows(SE)', 'FOSSGuard', 'Athena Dev']
	product = products[product_id-1]
	projectname = projectnames[product_id-1]

	days = [date.today() - timedelta(x) for x in range(4, -1, -1)]
	# 전체품질 : 날짜 입력되지 않았을 경우 - 5일치, 날짜 입력 받아서 지정기간 품질 출력
	sdate = days[0].strftime("%Y-%m-%d") # 기본 시작날짜 - 5일전
	edate = days[4].strftime("%Y-%m-%d") # 기본 끝날짜 - 오늘
	if request.POST: # 입력된 날짜대로 지정 기간설정
		sdate = request.POST.get('sdate')
		edate = request.POST.get('edate')

	# 설정된 기간만큼 전체품질 현황 출력
	termset = Productquality.objects.filter(product__icontains=product, date__range=(sdate, edate)).values('manualtest', 'process', 'faulty', 'date').order_by('date')
	qualities = [{'date':term['date'].strftime("%m/%d"), 'value':term['manualtest'] + term['process'] + term['faulty']} for term in termset]
	
	# 고객사 결함현황
	allclient = Data.objects.filter(project__icontains=projectname, inputdate__date=date.today()).values('client').distinct().annotate(num=Count('client')).order_by('client')  # 전체 고객사명을 뽑음
	clientdatas = list({'client':select_cli['client'], 'num':select_cli['num']} for select_cli in allclient if select_cli['client'] != "사내")

	#등록된 프로젝트 프로세스 출력
	processbars = []
	project_set = Process.objects.filter(project__icontains=product).values('project','version', 'start', 'end', 'firststep', 'secondstep', 'thirdstep', 'file', 'is_deleted') # 프로젝트 관련정보 가져오기
	for project in project_set:
		totaldays = int(re.findall('\d+', str(project['end']-project['start']))[0])
		fstepdays = int(re.findall('\d+', str(project['firststep']-project['start']))[0])
		sstepdays = int(re.findall('\d+', str(project['secondstep']-project['firststep']))[0])
		tstepdays = int(re.findall('\d+', str(project['thirdstep']-project['secondstep']))[0])
		estepdays = int(re.findall('\d+', str(project['end']-project['thirdstep']))[0])
		currentdays = int(re.findall('\d+', str(date.today()-project['start']))[0])
		
		nowper = str(round((currentdays / totaldays) * 100))
		if int(nowper) > 100: nowper = '100'
		fdays = str(math.floor((fstepdays / totaldays) * 100))
		sdays = str(math.floor((sstepdays / totaldays) * 100))
		tdays = str(math.floor((tstepdays / totaldays) * 100))
		edays = str(math.floor((estepdays / totaldays) * 100))

		processbars.append({
			'project':project['project'],
			'version':project['version'],
			'firststep':project['firststep'],
			'secondstep':project['secondstep'],
			'thirdstep':project['thirdstep'],
			'end':project['end'],
			'fdays':fdays,
			'sdays':sdays,
			'tdays':tdays,
			'edays':edays,
			'nowper':nowper,
			'file':project['file'],
			'is_deleted':project['is_deleted'],
		})
	
	# 제품 현재 결함 수
	defectsdate = datetime.datetime.strptime(sdate, "%Y-%m-%d")
	defectedate = datetime.datetime.strptime(edate, "%Y-%m-%d")
	totalterm = int((defectedate-defectsdate).days)

	defects=[{'value':str(Data.objects.filter(project__icontains=projectname, inputdate__icontains=(defectsdate+datetime.timedelta(days=x)).strftime("%m-%d")).count()), 'date': str((defectsdate+datetime.timedelta(days=x)).strftime("%m-%d"))} for x in range(0, totalterm+1)]
	
	# 결함 수정중인 담당자 현황
	allprogrammers = Company.objects.filter(project=projectname, role='PG').distinct().values_list('name').order_by('name')
	programmers = list(Data.objects.filter(charge__in=allprogrammers, inputdate__date=date.today()).values('charge').distinct().annotate(num=Count('charge')))

	# 수정 확인중인 담당자 현황
	allmanagers = Company.objects.filter(project=projectname, role='MG').distinct().values_list('name').order_by('name')
	managers = list(Data.objects.filter(charge__in=allmanagers, inputdate__date=date.today()).values('charge').distinct().annotate(num=Count('charge')))

	# 장기간 미처리 및 미정리
	handlings = [] # 장기간 미처리 저장을 위한 리스트
	arranges = [] # 장기간 미정리 저장을 위한 리스트
	
	orderedset = Data.objects.filter(inputdate__date=date.today()).values('num', 'charge', 'startdate').order_by('startdate') # 결함을 뽑아 결함 등록날짜가 오래된 순으로 정렬
	for ordered in orderedset:
		for select_programmer in allprogrammers: # 결함의 등록날짜가 오래된 순으로 정렬된 리스트에서 프로그래머 이름이 있으면 날짜를 계산하여 저장
			if ordered['charge'] == select_programmer[0]:
				handlings.append({'id':ordered['num'], 'name':ordered['charge'], 'days':re.findall('\d+', str(date.today()-ordered['startdate']))[0]})

		for select_manager in allmanagers: # 결함의 등록날짜가 오래된 순으로 정렬된 리스트에서 담당자 이름이 있으면 날짜를 계산하여 저장
			if ordered['charge'] == select_manager[0]:
				arranges.append({'id':ordered['num'], 'name':ordered['charge'], 'days':re.findall('\d+', str(date.today()-ordered['startdate']))[0]})

	return render(request, 'extern/product.html', {'product':product, 'clientdatas':clientdatas, 'processbars':processbars, 'qualities':qualities, 'defects':defects, 'programmers':programmers, 'managers':managers, 'handlings':handlings[0:7], 'arranges':arranges[0:7], 'sdate':sdate, 'edate':edate, 'product_id':product_id})


def sendmail(request):
	if request.POST:
		if request.POST.get('email'):
			html = '''
			<h1>전체 품질</h1>
				<div class="vGraph" style="padding:20px 0;">
					<ul style="margin:0; padding:0; height:200px; border:1px solid #ddd; border-top:0; border-right:0; font-size:11px; font-family:Tahoma, Geneva, sans-serif; list-style:none;">
					'''

			sdate = request.POST.get('sdate')
			edate = request.POST.get('edate')

			defectsdate = datetime.datetime.strptime(sdate, "%Y-%m-%d")
			defectedate = datetime.datetime.strptime(edate, "%Y-%m-%d")
			totalterm = int((defectedate-defectsdate).days)

			termset = Totalquality.objects.filter(date__range=(sdate, edate)).values('manualtest', 'process', 'faulty', 'date').order_by('date')
			for term in termset:
				tdate = term['date'].strftime("%m/%d")
				tqual = str(term['manualtest'] + term['process'] + term['faulty'])

				html = html + '''
						<li style="float:left; display:inline; height:100%; margin:0 1%; position:relative; text-align:center; white-space:nowrap;">
							<span class="gTerm" style="position:relative; display:inline-block; width:100%; height:20px; line-height:20px; margin:0 -100% -20px 0; padding:200px 0 0 0; vertical-align:bottom; color:#767676; font-weight:bold;">
							''' + tdate +  '''
							</span>
							<span class="gBar" style="position:relative; display:inline-block; width:100%; margin:-1px 0 0 0; border:1px solid #ccc; border-bottom:0; background:#bde1f9; vertical-align:bottom; height: ''' + tqual + '''%;">
								<span style="position:absolute; width:100%; top:-20px; left:0; color:#767676;"> ''' + tqual + '''</span>
							</span>
						</li>
						'''


			html = html + '''
					</ul>
				</div><br /><br />
				'''
			
			processbars = []
			project_set = Process.objects.values('project','version', 'start', 'end', 'firststep', 'secondstep', 'thirdstep', 'file', 'is_deleted') # 프로젝트 관련정보 가져오기
			for project in project_set:
				totaldays = int(re.findall('\d+', str(project['end']-project['start']))[0])
				fstepdays = int(re.findall('\d+', str(project['firststep']-project['start']))[0])
				sstepdays = int(re.findall('\d+', str(project['secondstep']-project['firststep']))[0])
				tstepdays = int(re.findall('\d+', str(project['thirdstep']-project['secondstep']))[0])
				estepdays = int(re.findall('\d+', str(project['end']-project['thirdstep']))[0])
				currentdays = int(re.findall('\d+', str(date.today()-project['start']))[0])
				
				nowper = str(round((currentdays / totaldays) * 100))
				if int(nowper) > 100: nowper = '100'
				fdays = str(math.floor((fstepdays / totaldays) * 100))
				sdays = str(math.floor((sstepdays / totaldays) * 100))
				tdays = str(math.floor((tstepdays / totaldays) * 100))
				edays = str(math.floor((estepdays / totaldays) * 100))

				processbars.append({
					'project':project['project'],
					'version':project['version'],
					'firststep':project['firststep'],
					'secondstep':project['secondstep'],
					'thirdstep':project['thirdstep'],
					'end':project['end'],
					'fdays':fdays,
					'sdays':sdays,
					'tdays':tdays,
					'edays':edays,
					'nowper':nowper,
					'file':project['file'],
					'is_deleted':project['is_deleted'],
				})
			
			html = html + '''
				<h1>진행중인 프로세스</h1>
				<ul>
				'''
			for processbar in processbars:
				html = html + '''
					<li class="iGraph" style="white-space:nowrap; line-height:normal;">
				''' + processbar['project'] + " " + processbar['version'] + '''
						<span class="gBar" style="display:inline-block; width:250px; height:14px; margin:0 5px 0 0; border:1px solid #ccc; background:#e9e9e9; font-size:11px;"><span class="gAction" style="width: ''' + processbar['nowper'] +'''%; display:inline-block; height:14px; border:1px solid #8c9bac; background:#99a6b6; margin:-1px;"></span></span>
						<span class="gPercent" style="font:16px Arial, Helvetica, sans-serif; color:#ccc;"><strong style="font-size:18px; color:#e88b30;">''' + processbar['nowper'] +'''</strong>%</span>
					</li>
				'''
			html = html + '''
				</ul><br /><br />
			'''

			
			html = html + '''
				<h1>전체 결함</h1>
			'''
				
			datas = [{'value':str(Data.objects.filter(inputdate__icontains=(defectsdate+datetime.timedelta(days=x)).strftime("%m-%d")).count()), 'date': str((defectsdate+datetime.timedelta(days=x)).strftime("%m-%d"))} for x in range(0, totalterm+1)] # 전체결함 출력

			for data in datas:
				html = html + '''
						<li style="float:left; display:inline; height:100%;position:relative; text-align:center; white-space:nowrap;">
							<span class="gTerm" style="position:relative; display:inline-block; width:100%; height:20px; line-height:20px; margin:0 -100% -20px 0; padding:200px 0 0 0; vertical-align:bottom; color:#767676; font-weight:bold;">
							''' + data['date'] +  '''
							</span>
							<span class="gBar" style="position:relative; display:inline-block; width:100%; margin:-1px 0 0 0; border:1px solid #ccc; border-bottom:0; background:#e9e9e9; vertical-align:bottom; height: ''' + str(int(data['value'])/10) + '''px;">
								<span style="position:absolute; width:100%; top:-20px; left:0; color:#767676;"> ''' + data['value'] + '''개</span>
							</span>
						</li>
						'''


			html = html + '''
					</ul>
				</div><br /><br /><br />
				'''
			msg = MIMEText(html, 'html')
			msg['Subject'] = "[QCEO] " + sdate + " ~ " + edate + " 전체 품질"
			msg['To'] = request.POST.get("email")
			msg['From'] = "kimmin20111@gmail.com"

			s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			s.login("kimmin20111@gmail.com", "1qa2ws3ed!")
			s.sendmail("kimmin20111@gmail.com", msg['To'], msg.as_string())
			s.quit()

			return render(request, 'extern/email.html', {'return':0})

		else: 
			return render(request, 'extern/email.html', {'return':1})

	else: 
		return HttpResponse("Wrong Access")


def productsendmail(request, product_id):
	products = ['SecuMS', 'OmniGuard Unix', 'OmniGuard Windows', 'FOSSGuard', 'Athena']
	projectnames = ['SecuMS', 'UniTy UNIX', 'UAC for Windows(SE)', 'FOSSGuard', 'Athena Dev']
	product = products[product_id-1]
	projectname = projectnames[product_id-1]
	if request.POST:
		if request.POST.get('email'):
			html = '''
			<h1> ''' + product + ' 품질현황'
			html = html + '''
				</h1>
				<div class="vGraph" style="padding:20px 0;">
					<ul style="margin:0; padding:0; height:200px; border:1px solid #ddd; border-top:0; border-right:0; font-size:11px; font-family:Tahoma, Geneva, sans-serif; list-style:none;">
					'''

			sdate = request.POST.get('sdate')
			edate = request.POST.get('edate')

			defectsdate = datetime.datetime.strptime(sdate, "%Y-%m-%d")
			defectedate = datetime.datetime.strptime(edate, "%Y-%m-%d")
			totalterm = int((defectedate-defectsdate).days)

			termset = Productquality.objects.filter(product__icontains=product, date__range=(sdate, edate)).values('manualtest', 'process', 'faulty', 'date').order_by('date')
			for term in termset:
				tdate = term['date'].strftime("%m/%d")
				tqual = str(term['manualtest'] + term['process'] + term['faulty'])

				html = html + '''
						<li style="float:left; display:inline; height:100%; margin:0 1%; position:relative; text-align:center; white-space:nowrap;">
							<span class="gTerm" style="position:relative; display:inline-block; width:100%; height:20px; line-height:20px; margin:0 -100% -20px 0; padding:200px 0 0 0; vertical-align:bottom; color:#767676; font-weight:bold;">
							''' + tdate +  '''
							</span>
							<span class="gBar" style="position:relative; display:inline-block; width:100%; margin:-1px 0 0 0; border:1px solid #ccc; border-bottom:0; background:#bde1f9; vertical-align:bottom; height: ''' + tqual + '''%;">
								<span style="position:absolute; width:100%; top:-20px; left:0; color:#767676;"> ''' + tqual + '''</span>
							</span>
						</li>
						'''
			html = html + '''
					</ul>
				</div><br /><br />
				'''
			
			processbars = []
			project_set = Process.objects.filter(project__icontains=product).values('project','version', 'start', 'end', 'firststep', 'secondstep', 'thirdstep', 'file', 'is_deleted') # 프로젝트 관련정보 가져오기
			for project in project_set:
				totaldays = int(re.findall('\d+', str(project['end']-project['start']))[0])
				fstepdays = int(re.findall('\d+', str(project['firststep']-project['start']))[0])
				sstepdays = int(re.findall('\d+', str(project['secondstep']-project['firststep']))[0])
				tstepdays = int(re.findall('\d+', str(project['thirdstep']-project['secondstep']))[0])
				estepdays = int(re.findall('\d+', str(project['end']-project['thirdstep']))[0])
				currentdays = int(re.findall('\d+', str(date.today()-project['start']))[0])
				
				nowper = str(round((currentdays / totaldays) * 100))
				if int(nowper) > 100: nowper = '100'
				fdays = str(math.floor((fstepdays / totaldays) * 100))
				sdays = str(math.floor((sstepdays / totaldays) * 100))
				tdays = str(math.floor((tstepdays / totaldays) * 100))
				edays = str(math.floor((estepdays / totaldays) * 100))

				processbars.append({
					'project':project['project'],
					'version':project['version'],
					'firststep':project['firststep'],
					'secondstep':project['secondstep'],
					'thirdstep':project['thirdstep'],
					'end':project['end'],
					'fdays':fdays,
					'sdays':sdays,
					'tdays':tdays,
					'edays':edays,
					'nowper':nowper,
					'file':project['file'],
					'is_deleted':project['is_deleted'],
				})
			
			html = html + '''
				<h1>진행중인 프로세스</h1>
				<ul>
				'''
			for processbar in processbars:
				html = html + '''
					<li class="iGraph" style="white-space:nowrap; line-height:normal;">
				''' + processbar['project'] + " " + processbar['version'] + '''
						<span class="gBar" style="display:inline-block; width:250px; height:14px; margin:0 5px 0 0; border:1px solid #ccc; background:#e9e9e9; font-size:11px;"><span class="gAction" style="width: ''' + processbar['nowper'] +'''%; display:inline-block; height:14px; border:1px solid #8c9bac; background:#99a6b6; margin:-1px;"></span></span>
						<span class="gPercent" style="font:16px Arial, Helvetica, sans-serif; color:#ccc;"><strong style="font-size:18px; color:#e88b30;">''' + processbar['nowper'] +'''</strong>%</span>
					</li>
				'''
			html = html + '''
				</ul><br /><br />
			'''
			html = html + '''
				<h1>제품 결함 수</h1>
				<ul style="overflow:hidden; height:130px">
			'''
				
			datas = [{'value':str(Data.objects.filter(project__icontains=projectname, inputdate__icontains=(defectsdate+datetime.timedelta(days=x)).strftime("%m-%d")).count()), 'date': str((defectsdate+datetime.timedelta(days=x)).strftime("%m-%d"))} for x in range(0, totalterm+1)] # 전체결함 출력
			
			for data in datas:
				print(data['date'], data['value'])
				html = html + '''
						<li style="float:left; display:inline; height:100%;position:relative; text-align:center; white-space:nowrap;">
							<span class="gTerm" style="position:relative; display:inline-block; width:100%; height:20px; line-height:20px; margin:0 -100% -20px 0; padding:100px 0 0 0; vertical-align:bottom; color:#767676; font-weight:bold;">
							''' + data['date'] +  '''
							</span>
							<span class="gBar" style="position:relative; display:inline-block; width:100%; margin:-1px 0 0 0; border:1px solid #ccc; border-bottom:0; background:#e9e9e9; vertical-align:bottom; height: ''' + str(int(data['value'])/10) + '''px;">
								<span style="position:absolute; width:100%; top:-20px; left:0; color:#767676;"> ''' + data['value'] + '''개</span>
							</span>
						</li>
						'''


			html = html + '''
					</ul>
				</div><br /><br /><br />
				'''
			
			# 결함 수정중인 담당자 현황
			allprogrammers = Company.objects.filter(project=projectname, role='PG').distinct().values_list('name').order_by('name')
			programmers = list(Data.objects.filter(charge__in=allprogrammers, inputdate__date=date.today()).values('charge').distinct().annotate(num=Count('charge')))

			# 수정 확인중인 담당자 현황
			allmanagers = Company.objects.filter(project=projectname, role='MG').distinct().values_list('name').order_by('name')
			managers = list(Data.objects.filter(charge__in=allmanagers, inputdate__date=date.today()).values('charge').distinct().annotate(num=Count('charge')))

			# 장기간 미처리 및 미정리
			handlings = [] # 장기간 미처리 저장을 위한 리스트
			arranges = [] # 장기간 미정리 저장을 위한 리스트
			
			orderedset = Data.objects.filter(inputdate__date=date.today()).values('num', 'charge', 'startdate').order_by('startdate') # 결함을 뽑아 결함 등록날짜가 오래된 순으로 정렬
			for ordered in orderedset:
				for select_programmer in allprogrammers: # 결함의 등록날짜가 오래된 순으로 정렬된 리스트에서 프로그래머 이름이 있으면 날짜를 계산하여 저장
					if ordered['charge'] == select_programmer[0]:
						handlings.append({'id':ordered['num'], 'name':ordered['charge'], 'days':re.findall('\d+', str(date.today()-ordered['startdate']))[0]})

				for select_manager in allmanagers: # 결함의 등록날짜가 오래된 순으로 정렬된 리스트에서 담당자 이름이 있으면 날짜를 계산하여 저장
					if ordered['charge'] == select_manager[0]:
						arranges.append({'id':ordered['num'], 'name':ordered['charge'], 'days':re.findall('\d+', str(date.today()-ordered['startdate']))[0]})

			

			html = html + '''
			<h1>결함 수정중인 담당자 현황</h1>
			<div class="vGraph" style="padding:20px 0;">
				<ul style="margin:0; padding:0; height:200px; border:1px solid #ddd; border-top:0; border-right:0; font-size:11px; font-family:Tahoma, Geneva, sans-serif; list-style:none;">
				'''

			for programmer in programmers:
				html = html + '''
						<li style="float:left; display:inline; height:100%; margin:0 1%; position:relative; text-align:center; white-space:nowrap;">
							<span class="gTerm" style="position:relative; display:inline-block; width:100%; height:20px; line-height:20px; margin:0 -100% -20px 0; padding:200px 0 0 0; vertical-align:bottom; color:#767676; font-weight:bold;">
							''' + programmer['charge'] +  '''
							</span>
							<span class="gBar" style="position:relative; display:inline-block; width:100%; margin:-1px 0 0 0; border:1px solid #ccc; border-bottom:0; background:#b1debc; vertical-align:bottom; height: ''' + str(programmer['num']) + '''%;">
								<span style="position:absolute; width:100%; top:-20px; left:0; color:#767676;"> ''' + str(programmer['num']) + '''</span>
							</span>
						</li>
						'''
			html = html + '''
					</ul>
				</div><br /><br />
				'''

			html = html + '''
			<h1>수정 확인중인 담당자 현황</h1>
			<div class="vGraph" style="padding:20px 0;">
				<ul style="margin:0; padding:0; height:200px; border:1px solid #ddd; border-top:0; border-right:0; font-size:11px; font-family:Tahoma, Geneva, sans-serif; list-style:none;">
				'''

			for manager in managers:
				html = html + '''
						<li style="float:left; display:inline; height:100%; margin:0 1%; position:relative; text-align:center; white-space:nowrap;">
							<span class="gTerm" style="position:relative; display:inline-block; width:100%; height:20px; line-height:20px; margin:0 -100% -20px 0; padding:200px 0 0 0; vertical-align:bottom; color:#767676; font-weight:bold;">
							''' + manager['charge'] +  '''
							</span>
							<span class="gBar" style="position:relative; display:inline-block; width:100%; margin:-1px 0 0 0; border:1px solid #ccc; border-bottom:0; background:#e4bbbb; vertical-align:bottom; height: ''' + str(manager['num']) + '''%;">
								<span style="position:absolute; width:100%; top:-20px; left:0; color:#767676;"> ''' + str(manager['num']) + '''</span>
							</span>
						</li>
						'''
			html = html + '''
					</ul>
				</div><br /><br />
				'''





			msg = MIMEText(html, 'html')
			msg['Subject'] = "[QCEO] " + sdate + " ~ " + edate + " " + product + " 품질"
			msg['To'] = request.POST.get("email")
			msg['From'] = "kimmin20111@gmail.com"

			s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			s.login("kimmin20111@gmail.com", "1qa2ws3ed!")
			s.sendmail("kimmin20111@gmail.com", msg['To'], msg.as_string())
			s.quit()

			return render(request, 'extern/email.html', {'return':0})

		else: 
			return render(request, 'extern/email.html', {'return':1})

	else: 
		return HttpResponse("Wrong Access")