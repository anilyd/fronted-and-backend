from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    salary=models.FloatField()
    city=models.CharField(max_length=50)
    state=models.TextField()
    def __str__(self):
        return self.name
#Login model
class LoginAuth(models.Model):
    lid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username