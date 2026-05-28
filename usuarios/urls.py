from django.urls import path
from . import views


urlpatterns = [
    path('nuevo_usuario/', views.nuevo_usuario, name='nuevo_usuario'),
    path('', views.get_usuarios, name='usuarios')
]
