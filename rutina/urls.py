from django.urls import path
from . import views

urlpatterns = [
    path('rutinas/', views.crear_rutina, name='crear_rutina'),
]