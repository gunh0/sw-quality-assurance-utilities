from django.contrib import admin
from extern.models import additional

# Register your models here

class AdditionalAdmin(admin.ModelAdmin):
	list_per_page = 1
	list_display = ('goal', 'currnet', 'motto')

admin.site.register(additional, AdditionalAdmin)