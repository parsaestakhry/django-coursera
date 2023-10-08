from django.db import models
from django import forms
# create your models here
class Reservation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    contact = models.CharField('Phone number' , max_length=300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)
    
    def __str__(self) -> str:
        return self.name + " - " +  str(self.time)
    
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
