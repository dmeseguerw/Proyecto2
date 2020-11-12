
from django.db import models


GENDERS = [
    ('M', 'Male'),
    ('F','Female'),
    ('U','Unknown'),
]

HOURS = [
    ('7-8','7 am - 8 am'),
    ('8-9','8 am - 9 am'),
    ('9-10','9 am - 10 am'),
    ('10-11','10 am - 11 am'),
    ('11-12','11 am - 12 pm'),
    ('12-1','12 pm - 1 pm'),
    ('1-2','1 pm - 2 pm'),
    ('2-3','2 pm - 3 pm'),
    ('3-4','3 pm - 4 pm'),
    ('4-5','4 pm - 5 pm'),
]

class Veterinary(models.Model):
    username = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    telephone = models.PositiveIntegerField()
    
    def __str__(self):
        return "Dr: "+self.name

class Client(models.Model):
    username = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    telephone = models.PositiveIntegerField()

    def __str__(self):
        return "Client: "+self.name

class Pet(models.Model):
    owner = models.ForeignKey(Client,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1,choices=GENDERS)
    age = models.PositiveIntegerField()
    species = models.CharField(max_length=20)

    def __str__(self):
        return "Pet: "+self.name+" ("+self.species+", "+self.gender+"), Owner: "+self.owner.name

# Las citas tienen un model
class Appointments(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    veterinary = models.ForeignKey(Veterinary,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=5,choices=HOURS)
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE)
    reason = models.CharField(max_length=30)
    req_date = models.DateTimeField()

    def __str__(self):
        return "Vet: "+self.veterinary.name+", Client: "+self.client.name+", Date: "+str(self.date)