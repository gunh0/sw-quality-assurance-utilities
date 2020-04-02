from django.contrib import admin
from .models import RedmineDefects

# Register your models here.
class RedmineDefects_Admin(admin.ModelAdmin):
	list_per_page = 1
	list_display = ('number','title')

admin.site.register(RedmineDefects, RedmineDefects_Admin)