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
    path('adminnewapp', views.adminnewapp, name='adminnewapp'),
    path('adminsum', views.adminsum, name='adminsum'),
    path('reguser', views.reguser, name='reguser'),
    path('regadmin', views.regadmin, name='regadmin'),
    path('checkadminreg', views.checkadminreg, name='checkadminreg'),
    path('checkuserreg', views.checkuserreg, name='checkuserreg'),
    path('userdelapp/<int:question_id>', views.userdelapp, name='userdelapp'),
    path('usermodapp/<int:question_id>', views.usermodapp, name='usermodapp'),
    path('usersavechanges/<int:question_id>', views.usersavechanges, name='usersavechanges'),
    path('admindelapp/<int:question_id>', views.admindelapp, name='admindelapp'),
    path('adminmodapp/<int:question_id>', views.adminmodapp, name='adminmodapp'),
    path('adminsavechanges/<int:question_id>', views.adminsavechanges, name='adminsavechanges'),
    path('adminusersum', views.adminusersum, name='adminusersum'),
    path('adminpetsum', views.adminpetsum, name='adminpetsum'),
    path('adminvetsum', views.adminvetsum, name='adminvetsum'),
    path('adminconfirm', views.adminconfirm, name='adminconfirm'),
    path('adminadminreg', views.adminadminreg, name='adminadminreg'),
    path('adminuserreg', views.adminuserreg, name='adminuserreg'),
    path('adminpetreg', views.adminpetreg, name='adminpetreg'),
    path('checkpetreg', views.checkpetreg, name='checkpetreg'),

]