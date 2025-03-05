from django.db import models

# Create your models here.
class signup(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    country=models.CharField(max_length=10)
    mob=models.IntegerField()
    pin=models.CharField(max_length=10, null=True, blank=True)
    email=models.EmailField()
    password=models.CharField(max_length=50)

