from django.contrib import admin
from .models import Performance, Performagent

# Register your models here.

class PerformanceAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('agent', 'cpu', 'memory')
	search_fields = ('agent', 'cpu', 'memory')

admin.site.register(Performance, PerformanceAdmin)


class PerformagentAdmin(admin.ModelAdmin):
	list_per_page = 10

admin.site.register(Performagent, PerformagentAdmin)
