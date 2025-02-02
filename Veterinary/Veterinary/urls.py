"""Veterinary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
# from django.conf.urls import url, include
# from Appointments import views
#from accounts import views as acc_v
#from Veterinary import views as VetViews
urlpatterns = [
    #path('', VetViews.login_redirect, name='login_redirect'),
    #path('account/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    #path('',include('accounts.urls')),
    path('', include('appointments.urls')),
    
]





