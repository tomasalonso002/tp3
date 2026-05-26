
from django.urls import path, include
from . import views

urlpatterns=[
    path("", views.saludo, name='saludo'),
    path("despedir/", views.despedir, name='despedir')
]