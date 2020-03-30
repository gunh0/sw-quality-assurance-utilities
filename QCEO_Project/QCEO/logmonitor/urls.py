from django.urls import path
from . import views

app_name = 'logmonitor'

urlpatterns =[
	path('', views.logmonitorset, name='logmonitorset'),
]