from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# this path('home', views.home, name='user-home') will allow to get it from this url http://localhost:8008/user/home

urlpatterns = [
    path('home', views.home, name='user-home'),
    path('rejestracja', views.register, name='registration'),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('logowanie', views.login, name='login')
]
