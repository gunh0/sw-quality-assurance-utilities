import json
from django.db import models

# Create your models here.
class RedmineDefects(models.Model):
    number = models.PositiveIntegerField(default=0)
    project = models.TextField(blank=True)
    proj_type = models.TextField(blank=True)
    proj_status = models.TextField(blank=True)
    priority = models.TextField(blank=True)
    title = models.TextField(blank=True)
    author = models.TextField(blank=True)
    master = models.TextField(blank=True)
    category = models.TextField(blank=True)
    target_version = models.TextField(blank=True)
    change = models.TextField(blank=True)
    start_time = models.TextField(blank=True)
    deadline = models.TextField(blank=True)

    # This is for basic and custom serialisation to return it to client as a JSON.
    @property
    def to_dict(self):
        data = {
            'number': json.loads(self.number),
            'title': json.loads(self.title),
            'change': json.loads(self.change),
            'start_time':json.loads(self.start_time)
        }
        return data

    def __str__(self):
        return self.title