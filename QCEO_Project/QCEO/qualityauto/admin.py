from django.contrib import admin
from .models import TestColorS, TestColorA, AutomationProgram

# Register your models here.
class TestColorSAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('version', 'case', 'is_deleted')

admin.site.register(TestColorS, TestColorSAdmin)


class TestColorAAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('version', 'case', 'is_deleted')

admin.site.register(TestColorA, TestColorAAdmin)

class AutomationProgramAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('name', 'program')

admin.site.register(AutomationProgram, AutomationProgramAdmin)