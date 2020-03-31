from django.contrib import admin
from analysis.models import Tracking, BestDefact

# Register your models here.
class TrackingAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('product', 'version', 'client', 'is_deleted')

admin.site.register(Tracking, TrackingAdmin)


class BestDefactAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('num', 'item', 'miditem', 'subitem', 'is_deleted')

admin.site.register(BestDefact, BestDefactAdmin)
