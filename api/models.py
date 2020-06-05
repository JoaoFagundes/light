from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    birthday = models.DateField()

class Salary(models.Model):
    date = models.DateField()
    value = models.FloatField()
    discounts = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
