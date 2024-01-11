from django.db import models

# Create your models here.

class Finch (models. Model):
    name= models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    gender = models.TextField(max_length=250)
    color = models.CharField(max_length=100)

def __str__(self):
    return self.name