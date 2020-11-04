from django.db import models

# Create your models here.

GENDERS = [
    ('M', 'Male'),
    ('F','Female'),
    ('U','Unknown'),
]

class Owner(models.Model):
    pass

class Pet(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1,choices=GENDERS)
    age = models.PositiveIntegerField(blank=True)
    species = models.CharField(max_length=20)