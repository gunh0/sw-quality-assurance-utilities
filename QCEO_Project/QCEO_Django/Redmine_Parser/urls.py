from django.urls import path

from . import views

urlpatterns = [
    path('', views.DataList.as_view()),
    path('<int:pk>/', views.DataDetail.as_view()),
]