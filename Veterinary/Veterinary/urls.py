
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new
from Appointments import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.register, name="register"),  # <-- added
    # path('', include("main.urls")),
    # path('', include("django.contrib.auth.urls")), # <-- added
    path('', views.init, name='init'), # new,
    path('home/', views.home, name='home'), # new,
    path('new/', views.new, name='new'),
    path('delete/', views.delete, name='delete'),
    path('check/', views.check, name='check'),
    path('check/<int:pk>', views.check, name='check'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]

