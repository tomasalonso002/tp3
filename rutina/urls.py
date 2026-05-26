from django.urls import path
from . import views


urlpatterns = [

    # LISTAR RUTINAS
    path(
        '',
        views.rutinas,
        name='rutinas'
    ),

    # CREAR RUTINA
    path(
        'nueva/',
        views.crear_rutina,
        name='crear_rutina'
    ),

    # EDITAR RUTINA
    path(
        'editar/<int:id>/',
        views.editar_rutina,
        name='editar_rutina'
    ),

    # ELIMINAR RUTINA
    path(
        'eliminar/<int:id>/',
        views.eliminar_rutina,
        name='eliminar_rutina'
    ),

    # REGISTRO
    path(
        'register/',
        views.registrarse,
        name='register'
    ),
]