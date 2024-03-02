from django.db import models

# Create your models here.
class Student (models.Model):
    name : str = models.CharField(max_length=100)
    roll: int = models.IntegerField()
    city :str = models.CharField(max_length=100)