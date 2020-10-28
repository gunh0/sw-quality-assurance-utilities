from django.contrib import admin
from functionauto.models import Autotest, Testreserve
# Register your models here.


class AutotestAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('project', 'testname', 'total', 'starttime', 'path')

admin.site.register(Autotest, AutotestAdmin)


class TestreserveAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('name', 'project', 'state', 'reservetime', 'starttime')

admin.site.register(Testreserve, TestreserveAdmin)
