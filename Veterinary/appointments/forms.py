from django import forms
from .models import Appointments

class AppForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = [
            'veterinary',
            'date',
            'time',
            'pet',
            'reason',
        ]
        labels = {
            'veterinary' : 'Veterinary',
            'date':'Date',
            'time': 'Time',
            'pet':'Pet',
            'reason':'Reason',
        }