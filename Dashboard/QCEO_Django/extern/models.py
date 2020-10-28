from django.db import models

# Create your models here.
class additional(models.Model):
	goal = models.IntegerField('목표매출', null=True, blank=True)
	currnet = models.IntegerField('현재매출', null=True, blank=True)
	motto = models.CharField('좌우명', max_length=30)