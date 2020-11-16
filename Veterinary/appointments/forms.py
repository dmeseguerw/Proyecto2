from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from .models import *
from datetime import datetime

class AdminAppForm(forms.ModelForm):
    prefix='appform'
    class Meta:
        model = Appointments
        fields = [
            'client',
            'veterinary',
            'date',
            'time',
            'reason',
        ]
        widgets = {
            'date':DatePickerInput(),
        }
        


class AppForm(forms.ModelForm):
    prefix='appform'
    class Meta:
        model = Appointments
        fields = [
            'veterinary',
            'date',
            'time',
            'reason',
        ]
        widgets = {
            'date':DatePickerInput(),
        }
        

class AdminPetForm(forms.ModelForm):
    prefix='adminpetform'
    class Meta:
        model = Pet
        fields = [
            'owner',
            'name',
            'gender',
            'age',
            'species',
        ]
        labels = {
            'owner': 'Owner',
            'name':'Name',
            'gender':'Gender',
            'age':'Age',
            'species':'Species',
        }
class PetForm(forms.ModelForm):
    prefix='petform'
    class Meta:
        model = Pet
        fields = [
            'name',
            'gender',
            'age',
            'species',
        ]
        labels = {
            'name':'Name',
            'gender':'Gender',
            'age':'Age',
            'species':'Species',
        }

class UserLogForm(forms.ModelForm):
    prefix='userlogform'
    class Meta:
        model = Client
        fields = [
            'username',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }

class UserRegForm(forms.ModelForm):
    prefix='userregform'
    class Meta:
        model = Client
        fields = [
            'username',
            'name',
            'email',
            'password',
            'telephone',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }

class AdminRegForm(forms.Form):
    prefix='userregform'
    username = forms.CharField(max_length=10)
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(max_length=20,widget=forms.PasswordInput())
    telephone = forms.IntegerField()
    admin_pwd=forms.CharField(max_length=20,widget=forms.PasswordInput())
