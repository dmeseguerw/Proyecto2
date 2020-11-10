from django.db import models


GENDERS = [
    ('M', 'Male'),
    ('F','Female'),
    ('U','Unknown'),
]

class Client(models.Model):
    username = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    mail = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    tel = models.PositiveIntegerField(blank=True)
class Pet(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1,choices=GENDERS)
    age = models.PositiveIntegerField(blank=True)
    species = models.CharField(max_length=20)