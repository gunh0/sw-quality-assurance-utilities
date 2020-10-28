from django.urls import path
from . import views

app_name = 'logperform'

urlpatterns =[
	path('', views.logperform, name='logperform'),
	path('ajax/', views.performdata, name='performdata'),
	path('delete/', views.agentdelete, name='agentdelete'),
	path('datadelete/', views.performdatadelete, name='performdatadelete'),
]