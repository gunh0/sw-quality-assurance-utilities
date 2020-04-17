from django.db import models

class RedPaser(models.Model):
    num = models.IntegerField()
    project = models.CharField(max_length=20,blank=True)       # 프로젝트
    category = models.CharField(max_length=20,blank=True)      # 유형
    state = models.CharField(max_length=20,blank=True)         # 상태
    priority = models.CharField(max_length=20,blank=True)      # 우선순위
    title = models.CharField(max_length=200)                   # 제목
    author = models.CharField(max_length=10,blank=True)        # 저자
    master = models.CharField(max_length=10,blank=True)        # 담당자
    change = models.CharField(max_length=20,blank=True)        # 변경
    start = models.CharField(max_length=20,blank=True)         # 시작시간

    def __str__(self):
        return self.title