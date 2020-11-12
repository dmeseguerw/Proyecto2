from django.urls import path

from . import views

app_name = 'appointments'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('app', views.app, name='app'),                 #FIXME change to apps
    path('contact', views.contact, name='contact'),
    path('confirm', views.confirm, name='confirm'),
    path('summary', views.summary, name='summary'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('checklog', views.checklog, name='checklog'),
]