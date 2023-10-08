from django.db import models

# Create your models here.
class Product(models.Model):
    ProductID = models.IntegerField()
    name = models.TextField()
