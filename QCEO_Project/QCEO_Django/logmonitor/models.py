from django.db import models

# Create your models here.
class Monitoringproduct(models.Model):
	OSTYPE = (
		('Windows', 'Windows'),
		('Unix/Linux', 'Unix/Linux'),
	)
	product = models.CharField('제품', max_length=30, unique=True)
	ostype = models.CharField('운영체제', choices=OSTYPE, max_length=30, unique=True)
	logpath = models.CharField('로그경로', max_length=100, unique=True)
	logname = models.CharField('파일이름', max_length=20, unique=True)
	user = models.CharField('아이디', max_length=30, blank=True)
	host = models.CharField('호스트', max_length=30, blank=True)
	pw = models.CharField('비밀번호', max_length=30, blank=True)

class Defectloglist(models.Model):
	PRODUCT = (
		('SecuMS', 'SecuMS'),
		('OmniGuard', 'OmniGuard'),
		('FOSSGuard', 'FOSSGuard'),
		('Athene', 'Athene'),
	)
	product = models.CharField('제품', choices=PRODUCT, max_length=30)
	word = models.TextField('결함문구', unique=True)
	marked = models.BooleanField('등록', default=False)
