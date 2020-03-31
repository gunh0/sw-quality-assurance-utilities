from django.urls import path
from . import views

app_name = 'qualityauto'

urlpatterns =[
	path('', views.qualityauto, name='qualityauto'),
]