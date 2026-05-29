from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.rutinas, name='rutinas'), 
    path('crear/', views.crear_rutina, name='crear_rutina'),
    path('editar/<int:id>/', views.editar_rutina, name='editar_rutina'),
    path('<int:id>/eliminar/', views.eliminar_rutina, name='eliminar_rutina'),
=======
    path('rutinas/', views.crear_rutina, name='crear_rutina'),
>>>>>>> main
]