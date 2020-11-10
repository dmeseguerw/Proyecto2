from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/',LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('register/',views.register, name='register'),
    path('register_admin/',views.register_admin, name='register_admin'),
    path('profile/',views.profile,name='profile'),
]