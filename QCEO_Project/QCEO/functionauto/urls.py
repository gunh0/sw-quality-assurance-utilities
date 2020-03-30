from django.urls import path
from . import views

app_name = 'functionauto'

urlpatterns =[
	path('', views.functionauto, name='functionauto'),
	path('ajax/', views.processbars, name='processbars'),
	path('noreport/', views.noreport, name='noreport'),
]