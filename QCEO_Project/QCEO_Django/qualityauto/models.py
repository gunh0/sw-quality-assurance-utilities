from django.db import models

# Create your models here.
class TestColorS(models.Model):
	class Meta:
		verbose_name_plural = 'TestColorS'
	version = models.CharField('제품버전', max_length=20, unique=True)
	case = models.FileField('테스트결과', upload_to='testcolor/testcolors/')
	is_deleted = models.BooleanField('등록', default=False)


class TestColorA(models.Model):
	class Meta:
		verbose_name_plural = 'TestColorA'
	version = models.CharField('제품버전', max_length=20, unique=True)
	case = models.FileField('테스트결과', upload_to='testcolor/testcolora/')
	is_deleted = models.BooleanField('등록', default=False)


class AutomationProgram(models.Model):
	name = models.CharField('이름', max_length=20, unique=True)
	program = models.FileField('프로그램', upload_to='programs/')
