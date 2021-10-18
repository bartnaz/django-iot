from django.urls import path
from . import views

# this path('home', views.home, name='user-home') will allow to get it from this url http://localhost:8008/user/home

urlpatterns = [
    path('home', views.home, name='user-home'),
    path('rejestracja', views.register, name='registration'),
    path('logowanie', views.login, name='login')
]
