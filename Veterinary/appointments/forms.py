from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import *

class AppForm(forms.ModelForm):
    prefix='appform'
    class Meta:
        model = Appointments
        fields = [
            'veterinary',
            'date',
            'time',
            'pet',
            'reason',
        ]
        widgets = {
            'date':DatePickerInput(),
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