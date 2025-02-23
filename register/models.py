from django.db import models

# Create your models here.
class signup(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    country=models.CharField(max_length=10)
    mob=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=50)

class login(models.Model):
    mob=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=50)