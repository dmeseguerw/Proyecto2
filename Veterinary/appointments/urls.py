from django.urls import path

from . import views

app_name = 'appointments'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('app', views.app, name='app'),                 
    path('contact', views.contact, name='contact'),
    path('confirm', views.confirm, name='confirm'),
    path('summary', views.summary, name='summary'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('checklog', views.checklog, name='checklog'),
    path('usernewapp', views.usernewapp, name='usernewapp'),
    path('adminsum', views.adminsum, name='adminsum'),
    path('reguser', views.reguser, name='reguser'),
    path('regadmin', views.regadmin, name='regadmin'),
    path('checkadminreg', views.checkadminreg, name='checkadminreg'),
    path('checkuserreg', views.checkuserreg, name='checkuserreg'),
]