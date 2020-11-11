from django.contrib import admin
from .models import Veterinary,Client,Pet,Appointments
# Register your models here.
admin.site.register(Veterinary)
admin.site.register(Client)
admin.site.register(Pet)
admin.site.register(Appointments)