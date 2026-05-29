from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD
    path('', views.nuevo_usuarios, name='usuarios'),
    path('register/', views.register, name='register'),
=======
    path('nuevo_usuario/', views.nuevo_usuario, name='nuevo_usuario'),
    path('', views.get_usuarios, name='get_usuarios'),
    path('borrar_usuario/<int:id>', views.borrar_usuario, name='borrar_usuario'),
    path('editar_usuario/<int:id>', views.editar_usuario, name='editar_usuario')

>>>>>>> main
]
