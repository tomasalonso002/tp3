from django.urls import path
from . import views


urlpatterns = [
    path('', views.nuevo_usuarios, name='usuarios'),
    path('register/', views.register, name='register'),
]
