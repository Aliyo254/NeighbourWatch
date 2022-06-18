from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Neighbourhood(models.Model):
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    population=models.IntegerField()
    admin=models.ForeignKey(User,on_delete=models.CASCADE)

