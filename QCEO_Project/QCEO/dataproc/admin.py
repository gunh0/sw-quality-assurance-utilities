from django.contrib import admin
from dataproc.models import Data, Process, Company, Totalquality, Productquality
# Register your models here.

#admin.site.register(Data)

class CompanyAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('name', 'email', 'project', 'role')
	search_fields = ('name', 'project', 'role')

admin.site.register(Company, CompanyAdmin)


class ProcessAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('id', 'project', 'version', 'start', 'end', 'is_deleted')
	search_fields = ('id', 'project', 'start', 'end')

admin.site.register(Process, ProcessAdmin)

class TotalqualityAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('id', 'manualtest', 'process', 'faulty', 'date')

admin.site.register(Totalquality, TotalqualityAdmin)

class ProductqualityAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('id', 'product', 'manualtest', 'process', 'faulty', 'date')	
	search_fields = ('id', 'product')


admin.site.register(Productquality, ProductqualityAdmin)