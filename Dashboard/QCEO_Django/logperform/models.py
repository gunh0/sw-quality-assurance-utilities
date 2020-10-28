from django.db import models

# Create your models here.
class Logagent(models.Model):
	product = models.CharField('제품명', max_length=30)
	version = models.CharField('버전', max_length=30)
	logpath = models.CharField('로그경로', max_length=50)

class Loglist(models.Model):
	product = models.CharField('제품명', max_length=30)
	version = models.CharField('버전', max_length=30)
	whitelist = models.TextField('허용문구', blank=True)
	blacklist = models.TextField('비허용문구', blank=True)
	
class Performance(models.Model):
	timestamp = models.DateTimeField('시간', null=True, blank=True)
	agent = models.CharField('에이전트', max_length=30, blank=True)
	cpu = models.CharField('전체CPU사용량', max_length=30, blank=True)
	memory = models.CharField('전체메모리사용량', max_length=30, blank=True)
	p1cpu = models.CharField('p1CPU사용량', max_length=30, blank=True)
	p1memory = models.CharField('p1메모리사용량', max_length=30, blank=True)
	p2cpu = models.CharField('p2CPU사용량', max_length=30, blank=True)
	p2memory = models.CharField('p2메모리사용량', max_length=30, blank=True)
	p3cpu = models.CharField('p3CPU사용량', max_length=30, blank=True)
	p3memory = models.CharField('p3메모리사용량', max_length=30, blank=True)
	p4cpu = models.CharField('p4CPU사용량', max_length=30, blank=True)
	p4memory = models.CharField('p4메모리사용량', max_length=30, blank=True)
	p5cpu = models.CharField('p5CPU사용량', max_length=30, blank=True)
	p5memory = models.CharField('p5메모리사용량', max_length=30, blank=True)

class Performagent(models.Model):
	ostype = models.CharField('OS', max_length=20, blank=True)
	process1 = models.CharField('프로세스1', max_length=20, blank=True)
	process2 = models.CharField('프로세스2', max_length=20, blank=True)
	process3 = models.CharField('프로세스3', max_length=20, blank=True)
	process4 = models.CharField('프로세스4', max_length=20, blank=True)
	process5 = models.CharField('프로세스5', max_length=20, blank=True)