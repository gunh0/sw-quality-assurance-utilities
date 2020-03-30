from django.contrib import admin
from .models import Defectloglist, Monitoringproduct

# Register your models here.
class MonitoringproductAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('product',)

admin.site.register(Monitoringproduct, MonitoringproductAdmin)

class DefectloglistAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('product', 'word', 'marked')

admin.site.register(Defectloglist, DefectloglistAdmin)
