from django.db import models
from django.utils import timezone

# Create your models here.
class Data(models.Model):
	num = models.IntegerField('번호')
	project = models.CharField('프로젝트', max_length=30)
	type = models.CharField('유형', max_length=10)
	state = models.CharField('상태', max_length=15)
	realize = models.CharField('구현', max_length=4, blank=True)
	priority = models.CharField('우선순위', max_length=8)
	subject = models.TextField('제목')
	author = models.TextField('저자', max_length=6)
	charge = models.TextField('담당자', max_length=6)
	category = models.TextField('범주', max_length=8, blank=True)
	targetversion = models.TextField('목표버전', max_length=20, blank=True)
	change = models.DateTimeField('변경', null=True, blank=True)
	startdate = models.DateField('시작시간', null=True, blank=True)
	enddate = models.DateField('완료기한', null=True, blank=True)
	client = models.TextField('고객사', max_length=20, blank=True)
	degree = models.TextField('결함등급', max_length=10, blank=True)
	inputdate = models.DateTimeField(default=timezone.now)

class Process(models.Model):
	class Meta:
		verbose_name_plural = 'Processes'
	PROJECT_SET = (
		('SecuMS', 'SecuMS'),
		('OmniGuard Unix', 'OmniGuard Unix'),
		('OmniGuard Windows', 'OmniGuard Windows'),
		('FOSSGuard', 'FOSSGuard'),
		('Athena', 'Athena'),
	)
	project = models.CharField('프로젝트',choices=PROJECT_SET, max_length=30)
	version = models.CharField('버전', max_length=30)
	start = models.DateField('프로세스시작일')
	firststep = models.DateField('개발마감일')
	secondstep = models.DateField('품질점검마감일')
	thirdstep = models.DateField('패키징마감일')
	end = models.DateField('설치마감일(프로세스마감일)')
	file = models.FileField('보고서', blank=True)
	is_deleted = models.BooleanField('등록', default=True)

class Company(models.Model):
	class Meta:
		verbose_name_plural = 'Company'
	ROLES = (
		('PG', '개발자'),
		('MG', '관리자'),
		('EC', '기타'),
	)
	PROJECT_SET = (
		('SecuMS', 'SecuMS'),
		('UniTy UNIX', 'OmniGuard Unix'),
		('UAC for Windows(SE)', 'OmniGuard Windows'),
		('FOSSGuard', 'FOSSGuard'),
		('Athena Dev', 'Athena'),
	)
	name = models.CharField('이름', max_length=10)
	email = models.EmailField('이메일', blank=True)
	project = models.CharField('프로젝트', choices=PROJECT_SET, max_length=30, blank=True)
	role = models.CharField('역할', max_length=2, choices=ROLES, blank=True)

	
class Totalquality(models.Model):
	class Meta:
		verbose_name_plural = 'Totalqualities'
	manualtest = models.IntegerField("수동테스트")
	process = models.IntegerField("프로세스")
	faulty = models.IntegerField("결함도")
	date = models.DateField("날짜")

class Productquality(models.Model):
	PROJECT_SET = (
		('SecuMS', 'SecuMS'),
		('OmniGuard Unix', 'OmniGuard Unix'),
		('OmniGuard Windows', 'OmniGuard Windows'),
		('FOSSGuard', 'FOSSGuard'),
		('Athena', 'Athena'),
	)
	class Meta:
		verbose_name_plural = 'Productqualities'
	product = models.CharField('프로젝트',choices=PROJECT_SET, max_length=30)
	manualtest = models.IntegerField("수동테스트")
	process = models.IntegerField("프로세스")
	faulty = models.IntegerField("결함도")
	date = models.DateField("날짜")