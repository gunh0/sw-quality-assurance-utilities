from django.db import models

# Create your models here.
class Tracking(models.Model):
	product = models.CharField('제품', max_length=30)
	version = models.CharField('버전', max_length=20)
	client = models.CharField('고객사', max_length=20)
	content = models.TextField('결함현황')
	list = models.TextField('결함목록', blank=True)
	miss = models.TextField('점검시놓침')
	impossible = models.TextField('점검시불가')
	is_deleted = models.BooleanField('등록', default=False)

class BestDefact(models.Model):
	num = models.IntegerField('번호')
	item = models.CharField('대항목', max_length=10)
	miditem = models.CharField('중항목', max_length=10)
	subitem = models.CharField('소항목', max_length=10)
	content = models.TextField('내용')
	reference = models.TextField('참고항목')
	case = models.FileField('케이스 생성', upload_to='case/', blank=True)
	is_deleted = models.BooleanField('등록', default=False)