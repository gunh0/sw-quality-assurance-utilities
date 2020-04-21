from django.db import models


class Board(models.Model):
    part = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    passfail = models.CharField(max_length=200)
    checkcnt = models.CharField(max_length=200)
    defectcnt = models.CharField(max_length=200)

    def __str__(self):
        return "부문: " + self.part + ", 버전: " + self.version + ", 적합/부적합: " + self.passfail
