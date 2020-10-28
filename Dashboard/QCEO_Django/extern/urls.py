from django.urls import path
#from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views
from . import views

app_name = 'extern'

urlpatterns =[
	#path('', login, {'template_name': 'extern/login.html'}, name='index'),
	path('', auth_views.LoginView.as_view(template_name='extern/login.html'), name='index'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('product/<int:product_id>', views.product, name='product'),
	#path('logout/', logout, {'template_name': 'extern/logout.html'}, name='logout'),
	path('logout/', auth_views.LoginView.as_view(template_name='extern/logout.html'), name='logout'),
	path('dashboard/sendmail', views.sendmail, name='sendmail'),
	path('product/<int:product_id>/sendmail', views.productsendmail, name='productsendmail'),
]