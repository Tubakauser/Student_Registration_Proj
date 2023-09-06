from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    gen = models.CharField(max_length=50)
    stuClass = models.TextField()
    reg = models.TextField()
    test = models.FloatField()
