from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Patient(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100,default='NA')
    age = models.IntegerField(default=-1)
    Weight = models.FloatField(default=-1.0)
    Address = models.TextField(default='NA')
    Contact = models.CharField(max_length=10,default='NA')
    # User = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

class Doctor(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100,default='NA')
    type = models.CharField(max_length=1, default = 'D')

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    type = models.CharField(max_length=10, default='Doctor')
    time = models.DateTimeField(default=timezone.now)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,default=None)
    doctor = models.ForeignKey(Doctor, max_length=10, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.doctor.name + " " + self.time






