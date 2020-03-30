from django.db import models
from django.utils import timezone
# Create your models here.

class Autotest(models.Model):
	PATHS = (
		('/home/qceo/windowshare/Linux', 'Linux'),
		('/home/qceo/windowshare/Solaris_intel', 'Solaris'),
		('/home/qceo/windowshare/UNIX', 'UNIX'),
	)
	project = models.CharField('프로젝트', max_length=30)
	testname = models.CharField('테스트명', max_length=30)
	total = models.IntegerField('전체폴더개수')
	starttime = models.DateTimeField('테스트시간')
	path = models.CharField('경로', max_length=100, choices=PATHS, blank=True)
	file = models.FileField('보고서', blank=True)
	is_deleted = models.BooleanField('등록', default=True)
	
class Testreserve(models.Model):
	STATES = (
		('예약', '예약'),
		('접수', '접수'),
		('진행', '진행'),
		('완료', '완료'),
	)
	name = models.CharField('예약자명', max_length=30)
	reservetime = models.DateTimeField('예약시간', default=timezone.now)
	starttime = models.DateTimeField('희망시작시간', default=timezone.now)
	project = models.CharField('프로젝트명', max_length=30)
	memo = models.TextField('메모', blank=True)
	state = models.CharField('상태', max_length=2, choices=STATES, default='예약')
	is_deleted = models.BooleanField('등록', default=True)